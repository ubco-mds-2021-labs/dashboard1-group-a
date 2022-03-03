# following https://community.plotly.com/t/dash-integration-testing-with-selenium-and-github-actions/43602

from selenium.webdriver.chrome.options import Options


def pytest_setup_options():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    return options
