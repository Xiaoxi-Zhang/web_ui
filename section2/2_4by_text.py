from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://47.116.12.183/login.html")
    # text 文本选择器
    print(page.title())
    page.get_by_text("没有账号？点这注册").click()
    print(page.title())

    # 断言页面上的文本是可见的
    # t = page.get_by_text("注册账号")
    x = page.locator("//*[text()='注册账号']")
    expect(x).to_be_visible()

    page.pause()
    browser.close()
