from playwright.sync_api import sync_playwright, expect


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://47.116.12.183/login.html")
    page.get_by_placeholder("请输入用户名").fill("test")
    page.get_by_placeholder("请输入密码").fill("1232222")

    print(page.locator("#error").is_visible())
    page.get_by_role("button", name="立即登录").click()

    # 断言元素的文本值
    loc_error = page.locator("#error")
    expect(loc_error).to_have_text("服务器异常！")  # 绝对匹配文本

    # 包含文本值
    expect(loc_error).to_contain_text("服务器")  # 包含文本

    # 判断文本显示
    loc_text = page.get_by_text("服务器异常！")
    expect(loc_text).to_be_visible()

    page.pause()

    context.close()
    browser.close()
