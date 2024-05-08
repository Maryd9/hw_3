import pytest
from selene import browser


@pytest.fixture( autouse=True)
def browser_config():
    browser.config.window_height = 768
    browser.config.window_width = 1366
    yield
    browser.quit()
