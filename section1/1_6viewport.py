from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://47.116.12.183/login.html")
    page.get_by_role("textbox", name="用 户 名:").click()
    page.get_by_role("textbox", name="密     码:").click()
    page.get_by_role("textbox", name="用 户 名:").click()
    page.get_by_role("textbox", name="用 户 名:").fill("test")
    page.locator("#home-login").click()
    page.get_by_role("textbox", name="密     码:").click()
    page.get_by_role("textbox", name="密     码:").fill("123456")

    # 断点
    page.pause()

    page.get_by_role("button", name="立即登录 >").click()

    # 打断点
    page.pause()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
