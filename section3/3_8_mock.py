from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()

    page = context.new_page()
    page.goto("http://47.116.12.183/login.html")
    page.get_by_placeholder("请输入用户名").type("test", delay=100)
    page.get_by_placeholder("请输入密码").type("123456", delay=100)

    def handle(route):
        # 状态码改为500 模拟服务器异常
        route.fulfill(status=502)

    # 拦截请求，模拟返回
    page.route("http://47.116.12.183/api/login", handler=handle)

    page.get_by_role("button", name="立即登录").click()

    page.pause()

    context.close()
    browser.close()
