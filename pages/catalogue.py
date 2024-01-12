from selene import browser, query

class Actions:
    def open_catalogue_menu(self):
        browser.element('.catalog-btn').click()
        browser.element('.catalog')

    def open_catalogue_category(self, category):
        browser.element(f'//a[contains(text(), "{category.capitalize()}")]').click()
        browser.element('..filter-aside__section')
        title = browser.element('.breadcrumbs').get(query.text)
        assert category.lower() in title.lower(), f"Открылась категория {title} вместо {category.capitalize()}."
