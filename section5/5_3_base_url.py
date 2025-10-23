from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(base_url="https://www.cnblogs.com/")
    page = context.new_page()

    # 打开首页
    page.goto("/")

    # 打开其他页面
    page.goto("/yoyoketang/")

    context.close()
    browser.close()
