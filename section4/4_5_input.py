from playwright.sync_api import sync_playwright, expect


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://47.116.12.183/login.html")
    username = page.get_by_label("用 户 名:")

    # step1
    print(username.is_editable())  # 是否可编辑状态
    expect(username).to_be_editable()

    # step2
    username.fill("hello world")
    print(username.input_value())  # 获取输入框的值
    expect(username).to_have_value("hello world")

    # step3
    username.clear()  # 清空输入框
    print(username.input_value())
    expect(username).to_have_value("")

    username_help_block = page.locator(
        '[data-fv-validator="notEmpty"][data-fv-for="username"]'
    )
    print(username_help_block.is_visible())
    print(username_help_block.text_content())
    expect(username_help_block).to_be_visible()
    expect(username_help_block).to_have_text("不能为空")

    # 登录按钮
    loc_login_btn = page.get_by_text("立即登录")
    expect(loc_login_btn).to_be_disabled()  # 按钮不可用

    page.pause()

    context.close()
    browser.close()
