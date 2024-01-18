import allure
from ..skvot_boardshop_UI_project_tests.pages.catalogue_page import catalogue_page_action
from ..skvot_boardshop_UI_project_tests.pages.main_page import main_page_action
from ..skvot_boardshop_UI_project_tests.pages.products_page import products_page_action


@allure.story('Проверка сортировки товаров')
def test_check_products_sorting(category, sort):
    with allure.step('Открытие главной страницы интернет-магазина "Сквот"'):
        main_page_action.open_main_page()

    with allure.step('Закрытие поп-апа выбора города'):
        main_page_action.close_city_choose_window()

    with allure.step('Нажатие на "Весь каталог"'):
        main_page_action.open_catalogue_menu()

    with allure.step(f'Открытие каталога категории "{category}"'):
        catalogue_page_action.open_catalogue_category(category)
        catalogue_page_action.check_opened_catalogue_category(category)

    with allure.step(f'Сортировка товаров по признаку "{sort}"'):
        products_page_action.sort_products(sort)
        products_page_action.check_sorting(sort)
