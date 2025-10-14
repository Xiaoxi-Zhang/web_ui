from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://47.116.12.183/login.html")

    user = page.locator("#username")
    # 聚焦输入框
    user.focus()
    # 键盘输入
    page.keyboard.type("yoyotang", delay=100)
    # 回退
    page.keyboard.press("Backspace")
    # ctr+A
    page.keyboard.press("Control+A")

    page.pause()

    context.close()
    browser.close()
