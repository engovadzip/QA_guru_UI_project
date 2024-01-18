import allure
from skvot_boardshop_project_tests.pages.catalogue_page import catalogue_page_action
from skvot_boardshop_project_tests.pages.main_page import main_page_action
from skvot_boardshop_project_tests.pages.products_page import products_page_action


@allure.story('Проверка добавления товара в корзину')
def test_check_add_to_cart_n_clear_the_cart(category):
    with allure.step('Открытие главной страницы интернет-магазина "Сквот"'):
        main_page_action.open_main_page()

    with allure.step('Закрытие поп-апа выбора города'):
        main_page_action.close_city_choose_window()

    with allure.step('Нажатие на "Весь каталог"'):
        main_page_action.open_catalogue_menu()

    with allure.step(f'Открытие каталога категории "{category}"'):
        catalogue_page_action.open_catalogue_category(category)
        catalogue_page_action.check_opened_catalogue_category(category)

    with allure.step('Выбор наличия товаров в выбранном магазине'):
        products_page_action.select_shop('Интернет магазин')
        products_page_action.check_selected_shop('Интернет магазин')

    with allure.step('Добавление случайного товара в корзину'):
        products_page_action.open_random_product_and_check_its_info()
        products_page_action.add_product_to_cart_and_check_it_is_there()

    with allure.step('Удаление всех товаров из корзины'):
        products_page_action.clear_cart_and_check_it_is_clear()
