from playwright.sync_api import Page, expect


def test_login_title(page: Page):
    page.goto("/login.html")
    expect(page).to_have_title("网站登录")


def test_register_title(page: Page):
    page.goto("/register.html")
    expect(page).to_have_title("注册")
