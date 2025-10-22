from playwright.sync_api import sync_playwright, Page, expect


def test_login_1(page: Page):
    page.goto("http://47.116.12.183/login.html")
    page.get_by_label("用 户 名:").fill("test")
    page.get_by_label("密     码:").fill("123456")
    page.get_by_text("立即登录 > ").click()
    # 断言
    expect(page).to_have_title("首页")


def test_login_2(page: Page):
    page.goto("http://47.116.12.183/login.html")
    page.get_by_label("用 户 名:").fill("yoyo")
    print(page.title())
