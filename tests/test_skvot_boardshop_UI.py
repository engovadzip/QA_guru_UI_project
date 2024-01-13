from selene import be, browser
import allure
from pages import catalogue, products_page

cat = catalogue.Actions()
pr = products_page.Actions()


@allure.story('Добавление и удаление товара из корзины')
def test_add_desired_product_to_cart_n_clear_the_cart(category, product, sort):
    with allure.step('Открытие главной страницы интернет-магазина "Сквот"'):
        browser.open('')
        browser.element('.logo__image')

    with allure.step('Закрытие поп-апа выбора города'):
        browser.element('.close-modal-btn').click()

    with allure.step('Нажатие на "Весь каталог"'):
        cat.open_catalogue_menu()

    with allure.step('Открытие каталога выбранной категории (по умолчанию "Скейтбординг")'):
        cat.open_catalogue_category(category)

    with allure.step('Открытие товаров выбранной категории (по умолчанию "Деки скейтовые")'):
        pr.open_category(product)

    with allure.step('Выбор наличия товаров в выбранном магазине'):
        pr.select_shop('Интернет магазин')

    with allure.step('Сортировка товаров по цене'):
        pr.sort_products(sort)

    with allure.step('Добавление случайного товара в корзину'):
        pr.add_random_product_to_cart()

    with allure.step('Удаление всех товаров из корзины'):
        pr.clear_cart()
