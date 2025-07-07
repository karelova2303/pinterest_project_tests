from allure_commons._allure import step
from selene import browser, have, be


class AuthorizationPage:
    def __init__(self):
        self.email = browser.element('#email')
        self.password = browser.element('#password')
        self.submit = browser.element('[data-test-id="registerFormSubmitButton"] > [type="submit"]')

        self.account_button = browser.element('[data-test-id="header-accounts-options-button"]')
        self.account_menu = browser.element('[data-test-id="HeaderAccountsOptionsMenuAccountRep"]')

        self.logout_button = browser.element('[data-test-id="header-menu-options-logout"]')
        self.login_button = browser.element('[data-test-id="simple-login-button"]')

        self.button_logo = browser.element('[data-test-id="pinterest-logo-home-button"] * [aria-label="Главная"]')

    def open_homepage(self):
        browser.open('/')

    def input_email(self, value):
        self.email.set_value(value)

    def input_password(self, value):
        self.password.type(value)

    def click_submit(self):
        self.submit.click()

    def account_login(self, login, password):
        with step('Вход в аккаунт'):
            self.open_homepage()
            self.input_email(login)
            self.input_password(password)
            self.click_submit()

    def user_should_be_authorized(self, value):
        with step(f'Пользователь {value} авторизован'):
            self.account_button.click()
            self.account_menu.should(have.text(value))

    def log_out_of_account(self):
        with step('Выход из аккаунта'):
            self.account_button.click()
            self.logout_button.click()

    def login_button_should_be_visible(self):
        with step('Отображается кнопка "Log in"'):
            self.login_button.should(be.visible)

    def click_button_logo(self):
        with step('Кликнуть кнопку логотипа'):
            self.button_logo.click()
