from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = browser.new_page()
    page.goto("http://47.116.12.183/login.html")
    page.get_by_placeholder("请输入用户名").type("test", delay=100)
    page.get_by_placeholder("请输入密码").type("123456", delay=100)
    page.get_by_role("button", name="立即登录").click()

    # 点击新增模块
    page.get_by_text("新增模块").click()
    # form
    page.get_by_label("模块名称:").fill("AI助手模块")

    # 方法1  page.locator().select_option()
    # page.get_by_label("所属项目:").select_option("6f4d86ae")
    # page.get_by_label("模块描述:").fill("desc")

    # 方法2  page.select_option('selector', 'xxx')
    page.select_option("#project", "6f4d86ae")

    page.pause()

    context.close()
    browser.close()
