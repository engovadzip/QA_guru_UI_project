from selene import be, browser, query

class Actions:
    def open_catalogue_menu(self):
        browser.element('.catalog-btn').click()
        browser.element('.catalog')

    def open_catalogue_category(self, category):
        browser.element(f'//a[contains(text(), "{category.capitalize()}")]').click()
        browser.element('..filter-aside__section')
        title = browser.element('.breadcrumbs').get(query.text)
        assert category.lower() in title.lower(), f"Открылась категория {title} вместо {category.capitalize()}."

    def check_search(self, search):
        browser.element('.search-btn').click()
        browser.element('//input[@placeholder="Введите слово для поиска"]').send_keys(search).press_enter()

        browser.element('.top-item__title').should(be.present)
        results = browser.all('.top-item__title')

        for result in results:
            assert search.lower() in result.get(query.text).lower(), \
                f'Произошла ошибка при поиске. В строку поиска передан "{search}". Найденный результат {result.get(query.text)} не соответствует критерию поиска.'