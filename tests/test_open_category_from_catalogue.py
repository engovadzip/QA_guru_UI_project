import allure
from ..skvot_boardshop_UI_project_tests.pages.catalogue_page import catalogue_page_action
from ..skvot_boardshop_UI_project_tests.pages.main_page import main_page_action


@allure.story('Открытие категории из "Весь каталог"')
def test_open_category_from_catalogue(category):
    with allure.step('Открытие главной страницы интернет-магазина "Сквот"'):
        main_page_action.open_main_page()

    with allure.step('Закрытие поп-апа выбора города'):
        main_page_action.close_city_choose_window()

    with allure.step('Нажатие на "Весь каталог"'):
        main_page_action.open_catalogue_menu()

    with allure.step(f'Открытие каталога категории "{category}"'):
        catalogue_page_action.open_catalogue_category(category)
        catalogue_page_action.check_opened_catalogue_category(category)
