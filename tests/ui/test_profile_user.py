import allure
from allure_commons._allure import step

from pinterest_project.data.data import profile_name, profile_username, follower_count, description, web_site
from pinterest_project.models.app import app


@allure.tag('Web', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Профиль пользователя')
class TestProfileUser:

    @allure.title('Проверка отображения публичного профиля')
    def test_should_be_visible_public_profile(self, browser_manager, authorization_user, attach_with_test):
        # WHEN
        with step('Открыть публичный профиль'):
            app.user_page.open_public_profile_user()

        # THEN
        with step('Имя профиля отображается'):
            app.user_page.should_be_visible_profile_name(profile_name)
        with step('Имя пользователя отображается'):
            app.user_page.should_be_visible_profile_username(profile_username)
        with step('Количество подписок отображается'):
            app.user_page.should_be_visible_following_count(follower_count)
        with step('Кнопка "Поделиться" отображается'):
            app.user_page.should_be_visible_share_profile_button()
        with step('Кнопка "Изменить профиль" отображается'):
            app.user_page.should_be_visible_edit_profile_button()
        with step('Вкладка "Созданные" отображается'):
            app.user_page.should_be_visible_created_profile_tab()
        with step('Вкладка "Сохраненные" отображается'):
            app.user_page.should_be_visible_saved_profile_tab()


    @allure.title('Проверка кликабельности иконок общего доступа')
    def test_should_be_visible_share_menu(self, browser_manager, authorization_user, attach_with_test):
        # WHEN
        with step('Открыть публичный профиль'):
            app.user_page.open_public_profile_user()
        with step('Кликнуть кнопку "Поделиться"'):
            app.user_page.click_share_profile_button()

        # THEN
        with step('Иконка "Копировать ссылку" кликабельна'):
            app.user_page.should_be_visible_copy_link_icon()
        with step('Иконка "WhatsApp" кликабельна'):
            app.user_page.should_be_visible_whatsapp_icon()
        with step('Иконка "Messenger" кликабельна'):
            app.user_page.should_be_visible_messenger_icon()
        with step('Иконка "Facebook" кликабельна'):
            app.user_page.should_be_visible_facebook_icon()
        with step('Иконка "X" кликабельна'):
            app.user_page.should_be_visible_twitter_icon()


    @allure.title('Проверка отображения вкладки "Пины"')
    def test_open_saved_pins(self, browser_manager, authorization_user, attach_with_test):
        # WHEN
        with step('Открыть публичный профиль'):
            app.user_page.open_profile_user()
        with step('Кликнуть таб "Пины"'):
            app.user_page.open_pins_tab()

        # THEN
        with step('Сохраненные пины отображаются'):
            app.user_page.should_be_visible_pins()


    @allure.title('Проверка отображения вкладки "Доски"')
    def test_open_saved_boards(self, browser_manager, authorization_user, attach_with_test):
        # WHEN
        with step('Открыть публичный профиль'):
            app.user_page.open_profile_user()
        with step('Кликнуть таб "Доски"'):
            app.user_page.open_boards_tab()

        # THEN
        with step('Сохраненные доски отображаются'):
            app.user_page.should_be_visible_boards()


    @allure.title('Проверка редактирования профиля')
    def test_edit_form_profile_user(self, browser_manager, authorization_user, attach_with_test):
        # WHEN
        with step('Открыть публичный профиль'):
            app.user_page.open_public_profile_user()
        with step('Кликнуть кнопку "Изменить профиль"'):
            app.user_page.click_edit_profile_button()

        with step('Загрузить фото профиля'):
            app.user_page.upload_foto('foto.jpg')
        with step('Добавить текст в поле "Описание"'):
            app.user_page.input_about(description)
        with step('Добавить ссылку в поле "Веб-сайт"'):
            app.user_page.input_website_url(web_site)
        with step('Кликнуть кнопку "Сохранить"'):
                app.user_page.click_done_button()

        # THEN
        with step('Внесенные изменения отображаются'):
            app.user_page.should_be_saved_data()
