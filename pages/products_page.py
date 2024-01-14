from selene import be, browser, command, have, query
from random import randint
import time

class Elements:
    # Боковая панель страницы с товарами
    side_panel_css = '..filter-aside__section'

    # Меню выбора сортировки
    sort_menu_css = '#select_sort .SumoSelect'

    # Наименование товара
    product_css = '.top-item__title'

    # Цена товара
    price_css = '.top-item__price-new'

    # Меню выбора наличия в магазинах
    shop_css = '#select_shop .SumoSelect'

    # Кнопка "Ок" в меню выбора наличия в магазинах
    ok_css = '.btnOk'

    # Кнопка "В корзину" на странице с товаром
    add_to_cart_xp = '//span[text()="В корзину"]'

    # Размер товара (если применимо)
    product_size_css = '.product-size__label'

    # Корзина
    cart_xp = '//div[@class="header__item col-sm-1 header__item--cart js-cart-trigger col-xs-2"]'

    # Окно корзины (открывается при наведении курсора на иконку корзины)
    cart_window_xp = '//div[@class="cart-popup js-cart-popup cart-hover2 cart-popup--opened"]'

    # Наименование товара в корзине
    product_cart_css = '.cart-popup-item__title'

    # Цена товара в корзине
    price_cart_css = '.cart-popup-item__price-new'

    # Кнопка "Очистить корзину"
    clear_xp = '//a[text()="Очистить корзину"]'

    # Заголовок корзины
    cart_title_xp = '.cart-popup__title'

    # Наименование товара на странице с его описанием
    product_page_name_css = '.page-head__title'

    # Цена товара на странице с его описанием
    product_page_price_css = '.product-price__price-new'

el = Elements()

class Actions:
    def open_category(self, category):
        browser.element(f'//a[contains(text(), "{category.capitalize()}") and @data-url]').click()
        browser.element(el.side_panel_css)
        title = browser.element('.breadcrumbs').get(query.text)
        assert category.lower() in title.lower(), f"Открылась категория {title} вместо {category.capitalize()}."

    def sort_products(self, sort):
        browser.element(el.sort_menu_css).click()
        browser.element(f'//label[text()="{sort.lower()}"]').click()
        browser.element(el.side_panel_css)

        prices = browser.all(el.price_css)
        prices = [int(a.get(query.text).rstrip('₽').replace(' ', '')) for a in prices]

        if sort.lower() == 'сначала дешевое':
            assert prices[0] <= prices[2], f'Цена первого товара {prices[0]}, а третьего - {prices[2]} при сортировке "сначала дешевое".'

        if sort.lower() == 'сначала дорогое':
            assert prices[0] >= prices[2], f'Цена первого товара {prices[0]}, а третьего - {prices[2]} при сортировке "сначала дорогое".'

    def select_shop(self, shop):
        browser.element(el.shop_css).click()
        browser.element(f'//label[text()="{shop}"]').click()
        browser.element(el.ok_css).click()
        browser.element(el.side_panel_css)

    def open_random_prouct_info(self):
        products = browser.all(el.product_css)
        product_names = [a.get(query.text).replace('\n', ' ') for a in products]
        prices = browser.all(el.price_css)
        prices = [a.get(query.text) for a in prices]

        i = randint(0, len(products) - 1)
        a = i
        products[a].perform(command.js.scroll_into_view).perform(command.js.click)

        browser.element(f'//*[text()="{product_names[a]}"]')
        browser.element(f'//*[text()="{prices[a]}"]')

        time.sleep(1)

        product_page_name = browser.element(el.product_page_name_css).get(query.text)
        product_page_price = browser.element(el.product_page_price_css).get(query.text).replace(' ', '')

        assert product_page_name.lower() == product_names[
            a].lower(), f'Наименование товара в списке товаров: {product_names[a]}, а на странице: {product_page_name}.'
        assert product_page_price == prices[a].replace(' ', ''), f'Цена товара в списке товаров: {prices[a]}, а на странице: {product_page_price}.'


    def add_product_to_cart(self):
        sizes = browser.all(el.product_size_css)
        if len(sizes) > 0:
            size = sizes[0].get(query.text)
            sizes[0].click()

        product_page_name = browser.element(el.product_page_name_css).get(query.text)
        product_page_price = browser.element(el.product_page_price_css).get(query.text).replace(' ', '')

        browser.element(el.add_to_cart_xp).perform(command.js.click)

        time.sleep(1)

        browser.element(el.cart_xp).hover()
        browser.element(el.cart_window_xp).should(be.present)

        time.sleep(1)

        cart_product = browser.element(el.product_cart_css).get(query.text)
        cart_price = browser.element(el.price_cart_css).get(query.text).replace(' ', '')

        assert cart_product.lower() == product_page_name.lower(), f'В корзину был добавлен товар {product_page_name}, а товар в корзине: {cart_product}.'
        assert cart_price == product_page_price, f'Цена добавленного товара {product_page_price}, а цена в корзине: {cart_price}.'

    def clear_cart(self):
        browser.element(el.cart_xp).hover()
        time.sleep(1)
        browser.element(el.clear_xp).click()
        time.sleep(1)
        browser.element(el.cart_title_xp).should(have.text('Моя корзина пуста'))