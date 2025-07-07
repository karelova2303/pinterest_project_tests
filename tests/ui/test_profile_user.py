import allure

from pinterest_project.data.data import profile_name, profile_username, follower_count, description, web_site, foto
from pinterest_project.models.app import app


@allure.tag('Web', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Профиль пользователя')
class TestProfileUser:

    @allure.title('Проверка открытия страницы публичного профиля')
    def test_open_public_profile(self, browser_manager, authorization_user, attach_with_test):
        # WHEN
        app.user_page.open_public_profile_user()

        # THEN
        app.user_page.profile_name_should_be_visible(profile_name)
        app.user_page.profile_username_should_be_visible(profile_username)
        app.user_page.following_count_should_be_visible(follower_count)


    @allure.title('Проверка кликабельности иконок общего доступа')
    def test_icons_share_menu_clickable(self, browser_manager, authorization_user, attach_with_test):
        # WHEN
        app.user_page.open_public_profile_user()
        app.user_page.click_share_profile_button()

        # THEN
        app.user_page.copy_link_icon_should_be_clickable()
        app.user_page.whatsapp_icon_should_be_clickable()
        app.user_page.messenger_icon_should_be_clickable()
        app.user_page.facebook_icon_should_be_clickable()
        app.user_page.twitter_icon_should_be_clickable()


    @allure.title('Проверка открытия вкладки "Пины"')
    def test_open_saved_pins(self, browser_manager, authorization_user, attach_with_test):
        # WHEN
        app.user_page.open_profile_user()
        app.user_page.open_pins_tab()

        # THEN
        app.user_page.pins_should_be_visible()


    @allure.title('Проверка открытия вкладки "Доски"')
    def test_open_saved_boards(self, browser_manager, authorization_user, attach_with_test):
        # WHEN
        app.user_page.open_profile_user()
        app.user_page.open_boards_tab()

        # THEN
        app.user_page.boards_should_be_visible()


    @allure.title('Проверка редактирования профиля')
    def test_edit_form_profile_user(self, browser_manager, authorization_user, attach_with_test):
        # WHEN
        app.user_page.open_public_profile_user()
        app.user_page.edit_form_profile(foto, description, web_site)

        # THEN
        app.user_page.data_should_be_saved()
