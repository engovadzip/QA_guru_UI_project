from selene import browser

class Actions:
    def open_catalogue(self):
        browser.element('.catalog-btn').click()
        browser.element('.catalog')

    def open_catalogue_category(self, category):
        browser.element(f'//a[text()="{category.capitalize()}"]').click()
        browser.element('..filter-aside__section')