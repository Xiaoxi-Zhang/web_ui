"""
内置定位方法
- page.get_by_text() 通过文本内容定位。
- page.get_by_label() 通过关联标签的文本定位表单控件。
- page.get_by_placeholder() 按占位符定位输入。
- page.get_by_title() 通过标题属性定位元素。
- page.get_by_role() 通过显式和隐式可访问性属性进行定位。
- page.get_by_alt_text() 通过替代文本定位元素，通常是图像。
- page.get_by_test_id() 根据 data-testid 属性定位元素（可以配置其他属性）。
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://47.116.12.183/login.html")

    # 通过文本内容定位
    # text 精准匹配元素
    # page.get_by_text("立即登录 >", exact=True).click()

    # 通过关联标签的文本定位表单控件
    # page.get_by_label("用 户 名:").fill("test")
    # page.get_by_label("密     码").fill("123456")

    # 按占位符定位输入
    page.get_by_placeholder("请输入用户名").fill("test")
    page.get_by_placeholder("请输入密码").fill("123456")

    # 通过标题属性定位元素 必须元素有 title 属性
    # page.get_by_title("Close").click()

    # role 角色定位
    page.get_by_role("button", name="立即登录").click()

    # 通过替代文本定位元素，通常是图像
    # page.get_by_alt_text("Company Logo").click()

    # 根据 data-testid 属性定位元素（可以配置其他属性）
    # page.get_by_test_id("submit-button").click()

    page.pause()
    browser.close()
