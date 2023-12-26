from selene import be, browser, have
import allure
from resources import actions, catalogue

action = actions.Actions()
cat = catalogue.Actions()


@allure.step('Открытие главной страницы интернет-магазина "Сквот"')
def test_open_main_page():
    browser.open('')

@allure.step('Выбор города Москва')
def test_choose_city():
    action.choose_city('Москва')

@allure.step('Проверка того, что выбран город Москва')
def test_correct_city():
    action.correct_city('Москва')

@allure.step('Нажатие на "Весь каталог"')
def test_show_cat_menu():
    cat.open_catalogue()