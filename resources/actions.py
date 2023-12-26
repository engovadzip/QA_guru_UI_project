from selene import browser, have

class Elements:
    city_choose_xp = '//a[contains(text(), "Нет, выбрать другой город")]'

el = Elements()

class Actions:
    def choose_city(self, city):
        browser.element(el.city_choose_xp).click()
        browser.element(f'//b[text()="{city.capitalize()}"]').click()

    def correct_city(self, city):
        browser.element('.information__title').should(have.text(f"{city.capitalize()}"))