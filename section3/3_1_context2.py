from playwright.sync_api import sync_playwright

"""
多账号登录场景，对于流程性审批用例非常适用
账号1 page1操作
账号2 page2操作
"""

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context1 = browser.new_context(accept_downloads=True)
    page1 = context1.new_page()
    page1.goto("http://47.116.12.183/login.html")
    page1.get_by_placeholder("请输入用户名").fill("test")
    page1.get_by_placeholder("请输入密码").fill("123456")
    page1.get_by_role("button", name="立即登录").click()

    context2 = browser.new_context(accept_downloads=True)
    page2 = context2.new_page()
    page2.goto("http://47.116.12.183/login.html")
    page2.get_by_placeholder("请输入用户名").fill("yoyo1")
    page2.get_by_placeholder("请输入密码").fill("aa123456")
    page2.get_by_role("button", name="立即登录").click()

    page1.pause()
