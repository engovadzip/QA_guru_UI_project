from selene import be, browser, query


class CataloguePageActions:
    def open_catalogue_category(self, category):
        browser.element(f'//a[contains(text(), "{category.capitalize()}")]').click()
        browser.element('.filter-aside__section').should(be.visible)

    def check_opened_catalogue_category(self, category):
        title = browser.element('.breadcrumbs').get(query.text)
        assert category.lower() in title.lower(), f"Открылась категория {title} вместо {category.capitalize()}."


catalogue_page_action = CataloguePageActions()
