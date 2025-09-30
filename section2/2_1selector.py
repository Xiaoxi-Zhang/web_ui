from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://47.116.12.183/login.html")

    # 1.先定位元素，再输入
    # page.locator("#username").fill("test")
    # page.locator("#password").fill("123456")

    # 2.直接输入，传2个参数
    page.fill("#username", "test")
    page.fill("#password", "123456")
    page.pause()

    # 组合定位  父元素--->子孙元素 css >> css
    page.locator("#login-form >> .btn-block").click()
    # 组合 css >> xpath
    page.locator("#login-form >> //*[@id='loginBtn']").click()
    # 注意xpath  .//  前面的点不需要
    # css >> text
    page.locator("#login-form >> text=立即登录").click()

    page.pause()
    browser.close()
