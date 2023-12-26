from selene import browser

class Actions:
    def open_catalogue(self):
        browser.element('.catalog-btn').click()
        browser.element('.catalog')