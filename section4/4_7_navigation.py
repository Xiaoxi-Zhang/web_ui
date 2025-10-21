from playwright.sync_api import sync_playwright, expect
import re


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://47.116.12.183/login.html")
    username = page.get_by_placeholder("请输入用户名").fill("test")
    password = page.get_by_placeholder("请输入密码").fill("123456")
    # 显式断言
    with page.expect_navigation(url="**/index.html"):
        page.get_by_role("button", name="立即登录").click()

    # 断言新页面
    expect(page).to_have_title("首页")
    expect(page).to_have_url("http://47.116.12.183/index.html")
    # re 表达式
    expect(page).to_have_url(re.compile(".*/index.html"))

    page.pause()

    context.close()
    browser.close()
