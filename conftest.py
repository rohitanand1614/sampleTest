import pytest
import base64

# @pytest.fixture()
# def edge_options(pytestconfig):
#     edge_options.add_argument("--headless")
#     edge_options.add_argument("--headless")
#     edge_options.add_argument("--headless")

@pytest.fixture
def chrome_options(chrome_options, pytestconfig):
    chrome_options.add_argument("start-maximized")
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    chrome_options.add_experimental_option("debuggerAddress","7070")
    if pytestconfig.getoption('headless'):
        chrome_options.add_argument('--headless')

def pytest_addoption(parser):
    parser.addoption(
        "--headless", action="store_true", default=False, help="headless"
    )
    parser.addoption(
        "--platform", action="store_true", default=False, help="driver name"
    )

@pytest.fixture
def selenium(driver):

    return driver