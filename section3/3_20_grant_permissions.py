from playwright.sync_api import sync_playwright, expect


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    # 设置允许 'cacmera', 'microphone' 权限
    context.grant_permissions(["cacmera", "microphone"])
    page = context.new_page()
    page.goto("http://47.116.12.183/login.html")

    page.pause()

    context.close()
    browser.close()
