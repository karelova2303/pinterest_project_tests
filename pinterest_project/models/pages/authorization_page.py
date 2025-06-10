from selene import browser, have, be

from pinterest_project.data.data import test_email, test_pass


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

    def login_of_account(self):
        self.open_homepage()
        self.input_email(test_email)
        self.input_password(test_pass)
        self.click_submit()

    def should_be_authorized_user(self, value):
        self.account_button.click()
        self.account_menu.should(have.text(value))

    def log_out_of_account(self):
        self.open_homepage()
        self.account_button.click()
        self.logout_button.click()

    def should_be_unauthorized_user(self):
        self.login_button.should(be.visible)

    def click_button_logo(self):
        self.button_logo.click()
