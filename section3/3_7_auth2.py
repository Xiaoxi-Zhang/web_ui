"""
自动读取auth cookies
"""

from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(
        storage_state="auth/login.json"
    )  # 加载cookies 身份认证

    page = context.new_page()
    page.goto("https://html5.mail.10086.cn/html/mailList.html")  # load

    page.pause()

    context.close()
    browser.close()
