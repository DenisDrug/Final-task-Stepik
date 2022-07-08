import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en, ru ....")


@pytest.fixture(scope="function")
def driver(request):
    options = Options()
    user_language = request.config.getoption("language")
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=options)
    print("\nstart driver for test..")
    yield driver
    print("\nquit driver..")
    driver.quit()

