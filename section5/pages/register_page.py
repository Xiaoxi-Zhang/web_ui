from playwright.sync_api import Page


class RegisterPage:

    def __init__(self, page: Page):
        self.page = page
        self.locator_username = page.get_by_label("用 户 名:")
        self.locator_password = page.get_by_label("密     码:")
        self.locator_register_btn = page.locator("text=立即注册")
        self.locator_login_link = page.locator("text=已有账号？点这登录")
        # 用户名输入框提示词
        self.locator_username_tip1 = page.locator(
            '[data-fv-validator="notEmpty"][data-fv-for="username"]'
        )
        self.locator_username_tip2 = page.locator(
            '[data-fv-validator="stringLength"][data-fv-for="username"]'
        )
        self.locator_username_tip3 = page.locator(
            '[data-fv-validator="regexp"][data-fv-for="username"]'
        )

    def navigate(self):
        self.page.goto("http://47.116.12.183/register.html")

    def fill_username(self, username):
        self.locator_username.fill(username)

    def fill_password(self, password):
        self.locator_password.fill(password)

    def click_register_button(self):
        self.locator_register_btn.click()

    def click_login_link(self):
        self.locator_login_link.click()

    def register(self, username, password):
        """流程"""
        self.fill_username(username)
        self.fill_password(password)
        self.click_register_button()
