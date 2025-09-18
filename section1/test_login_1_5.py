from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("http://47.116.12.183/login.html")
    page.get_by_role("textbox", name="用 户 名:").click()
    page.get_by_role("textbox", name="用 户 名:").fill("test")
    page.get_by_role("textbox", name="密     码:").click()
    page.get_by_role("textbox", name="密     码:").fill("123456")
    page.get_by_role("button", name="立即登录 >").click()
