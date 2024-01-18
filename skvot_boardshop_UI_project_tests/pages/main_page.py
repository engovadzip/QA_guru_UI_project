import allure
from selene import be, browser, query

class MainPageActions:
    def open_main_page(self):
        browser.open('')
        browser.element('.logo__image').should(be.present)

    def close_city_choose_window(self):
        browser.element('.close-modal-btn').click()
        browser.element('.close-modal-btn').should(be.hidden)

    def open_catalogue_menu(self):
        browser.element('.catalog-btn').click()
        browser.element('.catalog').should(be.visible)

    def check_products_search(self, search):
        browser.element('.search-btn').click()
        browser.element('.search__input').send_keys(search).press_enter()

        browser.element('.search-btn').should(be.present)
        browser.element('.top-item__title').should(be.present)
        results = browser.all('.top-item__title')

        for result in results:
            assert search.lower() in result.get(query.text).lower(), \
                (f'Произошла ошибка при поиске. В строку поиска передан "{search}". '
                 f'Найденный результат {result.get(query.text)} не соответствует критерию поиска.')


main_page_action = MainPageActions()
