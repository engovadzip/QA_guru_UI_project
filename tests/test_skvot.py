from selene import browser
import allure
from resources import actions, catalogue, products_page

action = actions.Actions()
cat = catalogue.Actions()
pr = products_page.Actions()


@allure.step('Открытие главной страницы интернет-магазина "Сквот"')
def test_open_main_page():
    browser.open('')


@allure.step('Выбор города Москва')
def test_choose_city():
    action.choose_city('Москва')


@allure.step('Нажатие на "Весь каталог"')
def test_show_catalogue_menu():
    cat.open_catalogue_menu()


@allure.step('Открытие категории "Скейтбординг"')
def test_open_skate_category(category):
    cat.open_catalogue_category(category)


@allure.step('Открытие категории "Деки скейтовые"')
def test_open_decks_category(product):
    pr.open_category(product)


@allure.step('Выбор наличия товаров в интернет-магазине')
def test_select_shop():
    pr.select_shop('Интернет магазин')


@allure.step('Сортировка товаров по цене')
def test_sort_products(sort):
    pr.sort_products(sort)


@allure.step('Добавление случайного товара в корзину')
def test_add_random_product_to_cart(sort):
    pr.add_random_product_to_cart()


@allure.step('Удаление всех товаров из корзины')
def test_clear_cart(sort):
    pr.clear_cart()