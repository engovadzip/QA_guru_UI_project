import allure
from skvot_boardshop_project_tests.pages.main_page import main_page_action
from skvot_boardshop_project_tests.pages.products_page import products_page_action


@allure.story('Проверка соответствия наименования и цены случайного товара в результатах поиска '
              'наименованию и цене на странице с его описанием')
def test_correct_product_description_from_search(search):
    with allure.step('Открытие главной страницы интернет-магазина "Сквот"'):
        main_page_action.open_main_page()

    with allure.step('Закрытие поп-апа выбора города'):
        main_page_action.close_city_choose_window()

    with allure.step('Проверка работы поиска товаров'):
        main_page_action.check_products_search(search)

    with allure.step('Проверка наименования и цены товара на странице с его описанием'):
        products_page_action.open_random_product_and_check_its_info()
