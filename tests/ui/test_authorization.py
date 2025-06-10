import allure
from allure_commons._allure import step

from pinterest_project.data.data import test_email
from pinterest_project.models.app import app


@allure.tag('Web', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Проверка авторизации пользователя')
@allure.title('Авторизация пользователя')
def test_should_be_authorized_user(browser_manager, attach_with_test):
    # WHEN
    with step('Вход в аккаунт'):
        app.authorization.login_of_account()

    # THEN
    with step(f'Пользователь {test_email} авторизован'):
        app.authorization.should_be_authorized_user(f'{test_email}')


@allure.tag('Web', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Проверка авторизации пользователя')
@allure.title('Разлогинивание пользователя')
def test_should_be_logged_out_user(browser_manager, attach_with_test):
    # WHEN
    with step('Выход из аккаунта'):
        app.authorization.log_out_of_account()

    # THEN
    with step('Пользователь не авторизован'):
        app.authorization.should_be_unauthorized_user()
