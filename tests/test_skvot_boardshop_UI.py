from selene import be, browser
import allure
from pages import catalogue, products_page
import time

cat = catalogue.Actions()
pr = products_page.Actions()


@allure.story('Проверка работы поиска товаров')
def test_check_search(search):
    with allure.step('Открытие главной страницы интернет-магазина "Сквот"'):
        browser.open('')
        browser.element('.logo__image').should(be.present)

    with allure.step('Закрытие поп-апа выбора города'):
        browser.element('.close-modal-btn').click()

    with allure.step('Проверка работы поиска товаров'):
        cat.check_search(search)


@allure.story('Проверка соответствия наименования и цены случайного товара в результатах наименованию и цене на странице с его описанием')
def test_correct_product_description_from_search(search):
    with allure.step('Открытие главной страницы интернет-магазина "Сквот"'):
        browser.open('')
        browser.element('.logo__image').should(be.present)

    with allure.step('Закрытие поп-апа выбора города'):
        browser.element('.close-modal-btn').click()

    with allure.step('Проверка работы поиска товаров'):
        cat.check_search(search)

    with allure.step('Проверка наименования и цены товара на странице с его описанием'):
        pr.open_random_prouct_info()


@allure.story('Открытие категории из "Весь каталог"')
def test_open_category_from_catalogue(category):
    time.sleep(3)

    with allure.step('Открытие главной страницы интернет-магазина "Сквот"'):
        browser.open('')
        browser.element('.logo__image').should(be.present)

    with allure.step('Закрытие поп-апа выбора города'):
        browser.element('.close-modal-btn').click()

    with allure.step('Нажатие на "Весь каталог"'):
        cat.open_catalogue_menu()

    with allure.step(f'Открытие каталога категории "{category}"'):
        cat.open_catalogue_category(category)


@allure.story('Открытие выбранной категории товаров')
def test_open_products_category(category, product):
    with allure.step('Открытие главной страницы интернет-магазина "Сквот"'):
        browser.open('')
        browser.element('.logo__image').should(be.present)

    with allure.step('Закрытие поп-апа выбора города'):
        browser.element('.close-modal-btn').click()

    with allure.step('Нажатие на "Весь каталог"'):
        cat.open_catalogue_menu()

    with allure.step(f'Открытие каталога категории "{category}"'):
        cat.open_catalogue_category(category)

    with allure.step(f'Открытие категории товаров {product}'):
        pr.open_category(product)


@allure.story('Проверка сортировки товаров')
def test_check_products_sorting(category, sort):
    with allure.step('Открытие главной страницы интернет-магазина "Сквот"'):
        browser.open('')
        browser.element('.logo__image').should(be.present)

    with allure.step('Закрытие поп-апа выбора города'):
        browser.element('.close-modal-btn').click()

    with allure.step('Нажатие на "Весь каталог"'):
        cat.open_catalogue_menu()

    with allure.step(f'Открытие каталога категории "{category}"'):
        cat.open_catalogue_category(category)

    with allure.step(f'Сортировка товаров по признаку "{sort}"'):
        pr.sort_products(sort)


@allure.story('Проверка соответствия наименования и цены случайного товара в списке товаров наименованию и цене на странице с его описанием')
def test_correct_product_description_from_products_list(category):
    with allure.step('Открытие главной страницы интернет-магазина "Сквот"'):
        browser.open('')
        browser.element('.logo__image').should(be.present)

    with allure.step('Закрытие поп-апа выбора города'):
        browser.element('.close-modal-btn').click()

    with allure.step('Нажатие на "Весь каталог"'):
        cat.open_catalogue_menu()

    with allure.step(f'Открытие каталога категории "{category}"'):
        cat.open_catalogue_category(category)

    with allure.step('Проверка наименования и цены товара на странице с его описанием'):
        pr.open_random_prouct_info()


@allure.story('Проверка добавления товара в корзину')
def test_check_add_to_cart_n_clear_the_cart(category):
    with allure.step('Открытие главной страницы интернет-магазина "Сквот"'):
        browser.open('')
        browser.element('.logo__image').should(be.present)

    with allure.step('Закрытие поп-апа выбора города'):
        browser.element('.close-modal-btn').click()

    with allure.step('Нажатие на "Весь каталог"'):
        cat.open_catalogue_menu()

    with allure.step(f'Открытие каталога категории "{category}"'):
        cat.open_catalogue_category(category)

    with allure.step('Выбор наличия товаров в выбранном магазине'):
        pr.select_shop('Интернет магазин')

    with allure.step('Добавление случайного товара в корзину'):
        pr.open_random_prouct_info()
        pr.add_product_to_cart()

    with allure.step('Очистка корзины'):
        pr.clear_cart()


@allure.story('Проверка добавления товара выбранной категории в корзину из отсортированного списка')
def test_check_add_to_cart_from_sorted_list(category, product, sort):
    with allure.step('Открытие главной страницы интернет-магазина "Сквот"'):
        browser.open('')
        browser.element('.logo__image').should(be.present)

    with allure.step('Закрытие поп-апа выбора города'):
        browser.element('.close-modal-btn').click()

    with allure.step('Нажатие на "Весь каталог"'):
        cat.open_catalogue_menu()

    with allure.step(f'Открытие каталога категории "{category}"'):
        cat.open_catalogue_category(category)

    with allure.step(f'Открытие категории товаров {product}'):
        pr.open_category(product)

    with allure.step('Выбор наличия товаров в выбранном магазине'):
        pr.select_shop('Интернет магазин')

    with allure.step(f'Сортировка товаров по признаку "{sort}"'):
        pr.sort_products(sort)

    with allure.step('Добавление случайного товара в корзину'):
        pr.open_random_prouct_info()
        pr.add_product_to_cart()

    with allure.step('Удаление всех товаров из корзины'):
        pr.clear_cart()
