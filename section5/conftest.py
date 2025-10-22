from playwright.sync_api import sync_playwright
import pytest


@pytest.fixture(scope="session")
def context_chrome():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    yield context
    # 实现用例执行完后，关闭浏览器上下文和浏览器
    context.close()
    browser.close()
    p.stop()
