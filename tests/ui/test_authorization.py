import allure

from pinterest_project.data.data import test_email, test_pass, account
from pinterest_project.models.app import app


@allure.tag('Web', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Проверка авторизации пользователя')
class TestAuthorization:

    @allure.title('Авторизация пользователя')
    def test_user_should_be_authorized(self, browser_manager, attach_with_test):
        # WHEN
        app.authorization.account_login(*account)

        # THEN
        app.authorization.user_should_be_authorized(f'{test_email}')


    @allure.title('Разлогинивание пользователя')
    def test_user_should_be_logged_out(self, browser_manager, authorization_user, attach_with_test):
        # WHEN
        app.authorization.log_out_of_account()

        # THEN
        app.authorization.login_button_should_be_visible()
