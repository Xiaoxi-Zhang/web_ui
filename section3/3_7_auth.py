from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://html5.mail.10086.cn/")  # load

    page.get_by_text("账号登录").click()
    page.get_by_placeholder("移动认证账号/手机号/别名").fill("13149230717")
    page.get_by_placeholder("密码").fill("ZXXld@146192")
    page.locator('//*[@id="chkSimlogin"]').click()

    with page.expect_navigation(url="**/html/mailList.html*"):
        page.get_by_role("button", name="登录").click()

    # 保存cookies   auth目录不会自动创建
    context.storage_state(path="auth/login.json")

    context.close()
    browser.close()
