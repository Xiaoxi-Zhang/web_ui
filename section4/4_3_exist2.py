from playwright.sync_api import sync_playwright, expect


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://47.116.12.183/login.html")
    page.get_by_placeholder("请输入用户名").fill("test")
    page.get_by_placeholder("请输入密码").fill("12")

    # 不能为空，隐藏
    loc1 = page.locator('[data-fv-validator="notEmpty"][data-fv-for="password"]')
    print("loc1:", loc1.count())
    assert loc1.count() >= 1
    # 断言 是否可见
    expect(loc1).to_be_hidden()  # 隐藏

    page.pause()

    context.close()
    browser.close()
