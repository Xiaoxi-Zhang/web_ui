from section5.pages.register_page import RegisterPage
from playwright.sync_api import expect
import pytest


class TestRegister:

    @pytest.fixture(autouse=True)
    def start_for_each(self, context_chrome):
        print("for each--start: 打开新页面访问注册页")
        self.page = context_chrome.new_page()
        self.register = RegisterPage(self.page)
        self.register.navigate()
        yield
        print("for each--close: 关闭注册页")
        self.page.close()

    def test_register_1(self):
        """用户名为空，点注册"""
        self.register.fill_username("")
        self.register.fill_password("123456")
        self.register.click_register_button()
        # 断言
        expect(self.register.locator_username_tip1).to_be_visible()
        expect(self.register.locator_username_tip1).to_contain_text("不能为空")

    def test_register_2(self):
        """用户名大于30字符"""
        self.register.fill_username("hello world hello world hello world")
        # 断言
        expect(self.register.locator_username_tip2).to_be_visible()
        expect(self.register.locator_username_tip2).to_contain_text(
            "用户名称1-30位字符"
        )
        # 断言 注册按钮不可点击
        expect(self.register.locator_register_btn).not_to_be_enabled()
