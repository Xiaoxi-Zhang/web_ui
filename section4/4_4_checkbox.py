from playwright.sync_api import sync_playwright, expect


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("file:///D:/Project/web_ui/section4/demo.html")

    # radio 的状态
    print(page.locator("#man").is_checked())
    print(page.locator("#man").is_enabled())
    print(page.locator("#no").is_checked())
    print(page.locator("#no").is_enabled())

    # checkbox 的状态
    print(page.is_checked("#a3"))
    print(page.is_enabled("#a3"))
    print(page.is_checked("#a4"))
    print(page.is_enabled("#a4"))

    # 如何勾选
    page.locator("#a1").check()  # 勾选
    page.locator("#a3").uncheck()  # 不勾选

    page.pause()

    context.close()
    browser.close()
