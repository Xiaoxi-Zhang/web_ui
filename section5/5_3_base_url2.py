from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(base_url="http://47.116.12.183")
    page = context.new_page()

    # 打开首页
    page.goto("/register.html")
    print(page.title())

    # 打开其他页面
    page.goto("/login.html")
    print(page.title())

    context.close()
    browser.close()
