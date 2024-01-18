import allure
from skvot_boardshop_project_tests.pages.catalogue_page import catalogue_page_action
from skvot_boardshop_project_tests.pages.main_page import main_page_action
from skvot_boardshop_project_tests.pages.products_page import products_page_action


@allure.story('Открытие выбранной категории товаров')
def test_open_products_category(category, product):
    with allure.step('Открытие главной страницы интернет-магазина "Сквот"'):
        main_page_action.open_main_page()

    with allure.step('Закрытие поп-апа выбора города'):
        main_page_action.close_city_choose_window()

    with allure.step('Нажатие на "Весь каталог"'):
        main_page_action.open_catalogue_menu()

    with allure.step(f'Открытие каталога категории "{category}"'):
        catalogue_page_action.open_catalogue_category(category)
        catalogue_page_action.check_opened_catalogue_category(category)

    with allure.step(f'Открытие категории товаров {product}'):
        products_page_action.open_product_category(product)

    with allure.step('Проверка категории товаров'):
        products_page_action.check_opened_product_category(product)
