from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://47.116.12.183/login.html")
    page.get_by_placeholder("请输入用户名").fill("yoyo")
    page.get_by_placeholder("请输入密码").fill("aa123456")
    page.get_by_role("button", name="立即登录").click()

    page.get_by_text("我的计划").click()
    page.locator("#btn-add-task").click()

    # select 下拉框
    page.select_option("#project", "接口")

    # 方式1
    # start = page.get_by_text("登录成功用例")
    # target = page.locator("#my_plan")
    # start.drag_to(target)

    # 方式2
    page.drag_and_drop("text=登录成功用例", "#my_plan")

    # 方式3
    start = page.get_by_text("登录成功用例")
    start.hover()
    page.mouse.down()
    target = page.locator("#my_plan")
    target.hover()
    page.mouse.up()

    page.pause()

    context.close()
    browser.close()
