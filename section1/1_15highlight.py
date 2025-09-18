from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.baidu.com")
    page.get_by_text("新闻").highlight()  # 高亮
    page.wait_for_timeout(200000)
