from playwright.sync_api import sync_playwright

"""
goto 默认的是 load 事件加载完成
"""

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
    # ["commit", "domcontentloaded", "load", "networkidle"] 默认load
    page.goto("https://playwright.dev/", wait_until="domcontentloaded", timeout=60000)
    # load 可以加载完成
    page.get_by_role("link", name="Community").click()

    page.pause()
