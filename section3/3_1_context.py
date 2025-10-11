from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    context2 = browser.new_context()
    page1 = context.new_page()
    page1.goto("https://www.baidu.com")

    page2 = context.new_page()
    page2.goto("https://www.taobao.com")

    page3 = context2.new_page()
    page3.goto("https://www.taobao.com")

    page4 = context2.new_page()
    page4.goto("https://www.taobao.com")

    print(page1.title())
    print(page2.title())
    print(page3.title())
    print(page4.title())

    page1.pause()
