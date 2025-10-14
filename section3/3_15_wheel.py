from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.jianshu.com/")

    # page.mouse.wheel(0, 400)
    for i in range(50):
        page.mouse.wheel(0, 100)
        page.wait_for_timeout(500)

    page.pause()

    context.close()
    browser.close()
