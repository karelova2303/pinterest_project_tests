import allure_commons
import pytest
from selene import browser, support

from pinterest_project.models.app import app
from pinterest_project.utils import attach


@pytest.fixture(scope='session')
def browser_manager():
    browser.config.base_url = 'https://ru.pinterest.com'
    browser.driver.maximize_window()
    browser.config.timeout = 15.0

    yield

    browser.quit()

@pytest.fixture(scope='class')
def authorization_user(browser_manager):
    app.authorization.login_of_account()

    yield

    app.authorization.log_out_of_account()

@pytest.fixture(scope='function')
def attach_with_test():
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext)

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)