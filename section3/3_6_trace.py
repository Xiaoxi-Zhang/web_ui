from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()

    # 开始追踪
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    page.goto("http://47.116.12.183/login.html")  # load

    page.get_by_placeholder("请输入用户名").fill("test")
    page.get_by_placeholder("请输入密码").fill("123456")
    page.get_by_role("button", name="立即登录").click()

    # 结束追踪
    context.tracing.stop(path="trace.zip")

    context.close()
    browser.close()
