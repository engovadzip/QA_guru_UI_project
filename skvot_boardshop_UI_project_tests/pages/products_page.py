from selene import be, browser, command, have, query
from random import randint


class ProductPageActions:
    def __init__(self):
        self.side_panel_css = '.filter-aside__section'
        self.sort_menu_css = '#select_sort .SumoSelect'
        self.product_css = '.top-item__title'
        self.price_css = '.top-item__price-new'
        self.shop_css = '#select_shop .SumoSelect'
        self.ok_css = '.btnOk'
        self.add_to_cart_css = '.goods_buy'
        self.product_size_css = '.product-size__label'
        self.cart_css = '.cart-btn'
        self.cart_window_css = '.cart-popup__header'
        self.product_cart_css = '.cart-popup-item__title'
        self.price_cart_css = '.cart-popup-item__price-new'
        self.clear_css = '.cart-popup__clean'
        self.cart_title_xp = '.cart-popup__title'
        self.product_page_name_css = '.page-head__title'
        self.product_page_price_css = '.product-price__price-new'

    def open_product_category(self, category):
        browser.element(f'//a[contains(text(), "{category.capitalize()}") and @data-url]').click()
        browser.element(self.side_panel_css).should(be.visible)

    def check_opened_product_category(self, category):
        title = browser.element('.breadcrumbs').get(query.text)
        assert category.lower() in title.lower(), f"Открылась категория {title} вместо {category.capitalize()}."

    def sort_products(self, sort):
        browser.element(self.sort_menu_css).click()
        browser.element(f'//label[text()="{sort.lower()}"]').click()
        browser.element(self.sort_menu_css).should(have.text(f"{sort.lower()}"))
        browser.element(self.side_panel_css).should(be.visible)

    def check_sorting(self, sort):
        prices = browser.all(self.price_css)
        prices = [int(a.get(query.text).rstrip('₽').replace(' ', '')) for a in prices]

        if sort.lower() == 'сначала дешевое':
            assert prices[0] <= prices[
                2], f'Цена первого товара {prices[0]}, а третьего - {prices[2]} при сортировке "сначала дешевое".'

        if sort.lower() == 'сначала дорогое':
            assert prices[0] >= prices[
                2], f'Цена первого товара {prices[0]}, а третьего - {prices[2]} при сортировке "сначала дорогое".'

    def select_shop(self, shop):
        browser.element(self.shop_css).click()
        browser.element(f'//label[text()="{shop}"]').click()
        browser.element(self.ok_css).click()
        browser.element(self.side_panel_css).should(be.visible)

    def check_selected_shop(self, shop):
        browser.element(self.shop_css).should(have.text(f"{shop}"))

    def open_random_product_and_check_its_info(self):
        products = browser.all(self.product_css)
        product_names = [a.get(query.text).replace('\n', ' ') for a in products]
        prices = browser.all(self.price_css)
        prices = [a.get(query.text) for a in prices]

        i = randint(0, len(products) - 1)
        a = i
        products[a].perform(command.js.scroll_into_view).perform(command.js.click)

        browser.element(f'//*[text()="{product_names[a]}"]')
        browser.element(f'//*[text()="{prices[a]}"]')

        product_page_name = browser.element(self.product_page_name_css).get(query.text)
        product_page_price = browser.element(self.product_page_price_css).get(query.text).replace(' ', '')

        assert product_page_name.lower() == product_names[
            a].lower(), f'Наименование товара в списке товаров: {product_names[a]}, а на странице: {product_page_name}.'
        assert product_page_price == prices[a].replace(' ', ''), \
            f'Цена товара в списке товаров: {prices[a]}, а на странице: {product_page_price}.'

    def add_product_to_cart_and_check_it_is_there(self):
        sizes = browser.all(self.product_size_css)
        if len(sizes) > 0:
            sizes[0].click()

        product_page_name = browser.element(self.product_page_name_css).get(query.text)
        product_page_price = browser.element(self.product_page_price_css).get(query.text).replace(' ', '')

        browser.element(self.add_to_cart_css).click()

        browser.element(self.cart_css).hover()
        browser.element(self.cart_window_css).should(be.present)

        cart_product = browser.element(self.product_cart_css).get(query.text)
        cart_price = browser.element(self.price_cart_css).get(query.text).replace(' ', '')

        assert cart_product.lower() == product_page_name.lower(), \
            f'В корзину был добавлен товар {product_page_name}, а товар в корзине: {cart_product}.'
        assert cart_price == product_page_price, \
            f'Цена добавленного товара {product_page_price}, а цена в корзине: {cart_price}.'

    def clear_cart_and_check_it_is_clear(self):
        browser.element(self.cart_css).hover()
        browser.element(self.clear_css).click()
        browser.element(self.cart_title_xp).should(have.text('Моя корзина пуста'))


products_page_action = ProductPageActions()
