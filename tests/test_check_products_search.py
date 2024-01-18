import allure
from ..skvot_boardshop_UI_project_tests.pages.main_page import main_page_action


@allure.story('Проверка работы поиска товаров')
def test_check_products_search(search):
    with allure.step('Открытие главной страницы интернет-магазина "Сквот"'):
        main_page_action.open_main_page()

    with allure.step('Закрытие поп-апа выбора города'):
        main_page_action.close_city_choose_window()

    with allure.step('Проверка работы поиска товаров'):
        main_page_action.check_products_search(search)
