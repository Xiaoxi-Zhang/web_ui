from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
    page.goto("http://47.116.12.183/login.html")  # load

    # 点按钮

    # 显式等待
    with page.expect_navigation(url="**/register.html"):
        page.get_by_text("点这注册").click()  # 触发新的导航

    # 新的页面继续操作
    # page.wait_for_load_state("networkidle")  # 等待页面加载完成
    page.get_by_label("用 户 名:").fill("testuser")

    page.pause()
