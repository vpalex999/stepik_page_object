import os
import pytest
from selenium import webdriver

GECKO_DRIVER_PATH = os.path.normpath(
    'drivers/geckodriver-v0.30.0-win64/geckodriver.exe')


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store',
                     default='firefox', help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store',
                     default='en', help='Choose language: en or ru')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    browser = None
    if browser_name == 'chrome':
        print('\nstart chrome browser for test...')
        browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        print('\nstart firefox browser for test...')
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', user_language)
        fp.update_preferences()
        browser = webdriver.Firefox(
            executable_path=GECKO_DRIVER_PATH, firefox_profile=fp)
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield browser
    print("\nquit browser..")
    browser.quit()
