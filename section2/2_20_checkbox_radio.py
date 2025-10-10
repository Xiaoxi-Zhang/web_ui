from playwright.sync_api import sync_playwright, expect


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
    page.goto("file:///D:/Project/web_ui/section2/checkbox.html")

    # 1.radio 选中
    page.locator("#woman").click()
    print(page.locator("#woman").is_checked())
    expect(page.locator("#woman")).to_be_checked()

    page.pause()
