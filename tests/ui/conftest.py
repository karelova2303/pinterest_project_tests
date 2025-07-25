import os

import allure_commons
import pytest
from dotenv import load_dotenv
from selene import browser, support
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pinterest_project.data.data import test_email, test_pass, account
from pinterest_project.models.app import app
from pinterest_project.utils import attach

DEFAULT_BROWSER_VERSION = '128.0'


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='128.0'
    )


@pytest.fixture(scope='function', autouse=True)
def browser_manager(request):
    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != '' else DEFAULT_BROWSER_VERSION
    options = Options()

    selenoid_capabilities = {
        "browserName": 'chrome',
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": False,
            "enableVideo": True,
        }
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor=f'https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub',
        options=options
    )

    browser.config.driver = driver
    browser.config.base_url = 'https://ru.pinterest.com'
    browser.driver.maximize_window()
    browser.config.timeout = 15.0

    yield

    browser.quit()


@pytest.fixture(scope='function')
def authorization_user(browser_manager):
    app.authorization.account_login(*account)


@pytest.fixture(scope='function')
def attach_with_test():
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext)

    yield browser

    attach.add_screenshot(browser)
    # attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)
