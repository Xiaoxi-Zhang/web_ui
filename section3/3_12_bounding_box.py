from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://47.116.12.183/login.html")

    btn = page.locator("#loginBtn")
    box = btn.bounding_box()
    print(box)

    page.pause()

    context.close()
    browser.close()
