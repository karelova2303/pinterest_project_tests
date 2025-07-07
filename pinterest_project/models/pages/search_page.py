from allure_commons._allure import step
from selene import browser, be


class SearchPage:
    def __init__(self):
        self.search_box_input = browser.element('[data-test-id="search-box-input"]')
        self.search_pin = browser.element('[data-test-id="pin"]')
        self.search_suggestion = browser.element('#SuggestionGroup-Option-1-0')

        self.filter_button = browser.element('[data-test-id="one-bar-module-0"] > [type="button"]')
        self.filter_by_video = browser.element('#Видео')
        self.filter_confirm_button = browser.element('[data-test-id="filter-confirm-button"]')
        self.video_pin = browser.element('[data-test-id="pinrep-video"]')


    def click_search_input(self):
        with step('Кликнуть строку поиска'):
            self.search_box_input.click()

    def typing_text_for_search(self, value):
        with step('Ввести текст'):
            self.search_box_input.set_value(value).press_enter()

    def click_search_suggestion(self):
        with step('Кликнуть первую картинку'):
            self.search_suggestion.click()

    def should_be_visible_pin(self):
        with step('Отображаются пины'):
            self.search_pin.should(be.visible)

    def click_filter_button(self):
        self.filter_button.click()

    def select_filter_by_video(self):
        with step('Выбрать радиобаттон "Видео" в меню фильтра'):
            self.click_filter_button()
            self.filter_by_video.click()
            self.filter_confirm_button.click()

    def should_be_visible_video_pin(self):
        with step('Отображаются пины с видео'):
            self.video_pin.should(be.visible)