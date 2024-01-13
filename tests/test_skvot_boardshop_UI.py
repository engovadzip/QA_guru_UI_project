from selene import browser
import allure
from pages import catalogue, products_page

cat = catalogue.Actions()
pr = products_page.Actions()


@allure.step('Открытие главной страницы интернет-магазина "Сквот"')
def test_open_main_page():
    browser.open('')
    browser.element('.logo__image')


@allure.step('Закрытие поп-апа выбора города')
def test_close_popup():
    browser.element('.close-modal-btn').click()


@allure.step('Нажатие на "Весь каталог"')
def test_show_catalogue_menu():
    cat.open_catalogue_menu()


@allure.step('Открытие каталога выбранной категории (по умолчанию "Скейтбординг")')
def test_open_selected_category(category):
    cat.open_catalogue_category(category)


@allure.step('Открытие товаров выбранной категории (по умолчанию "Деки скейтовые")')
def test_open_selected_products_category(product):
    pr.open_category(product)


@allure.step('Выбор наличия товаров в выбранном магазине')
def test_select_shop():
    pr.select_shop('Интернет магазин')


@allure.step('Сортировка товаров по цене')
def test_sort_products(sort):
    pr.sort_products(sort)


@allure.step('Добавление случайного товара в корзину')
def test_add_random_product_to_cart():
    pr.add_random_product_to_cart()


@allure.step('Удаление всех товаров из корзины')
def test_clear_cart():
    pr.clear_cart()
