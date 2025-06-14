import allure
from allure_commons._allure import step

from pinterest_project.data.data import text_search
from pinterest_project.models.app import app

@allure.tag('Web', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Строка поиска')
class TestSearch:

    @allure.title('Проверка поиска по введенному тексту')
    def test_search_on_input_name(self, browser_manager, authorization_user, attach_with_test):
        # WHEN
        with step('Кликнуть кнопку логотипа'):
            app.authorization.click_button_logo()
        with step('Кликнуть строку поиска'):
            app.search_page.click_search_input()
        with step('Ввести текст'):
            app.search_page.typing_text_for_search(text_search)

        # THEN
        with step('Отображаются пины'):
            app.search_page.should_be_visible_pin()

    @allure.title('Проверка поиска при выборе из меню "Идеи для вас"')
    def test_search_on_suggestion(self, browser_manager, authorization_user, attach_with_test):
        # WHEN
        with step('Кликнуть кнопку логотипа'):
            app.authorization.click_button_logo()
        with step('Кликнуть строку поиска'):
            app.search_page.click_search_input()
        with step('Кликнуть первую картинку'):
            app.search_page.click_search_suggestion()

        # THEN
        with step('Отображаются пины'):
            app.search_page.should_be_visible_pin()

    @allure.title('Проверка поиска с установленным фильтром')
    def test_search_by_filter(self, browser_manager, authorization_user, attach_with_test):
        # WHEN
        with step('Кликнуть кнопку логотипа'):
            app.authorization.click_button_logo()
        with step('Кликнуть строку поиска'):
            app.search_page.click_search_input()
        with step('Кликнуть первую картинку'):
            app.search_page.click_search_suggestion()
        with step('Выбрать радиобаттон "Видео" в меню фильтра'):
            app.search_page.select_filter_by_video()

        # THEN
        with step('Отображаются пины с видео'):
            app.search_page.should_be_visible_video_pin()