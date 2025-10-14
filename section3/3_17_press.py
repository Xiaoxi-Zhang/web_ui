"""
press 模拟键盘操作
"""

from playwright.sync_api import sync_playwright
import pyperclip


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    # page.goto("http://47.116.12.183/login.html")

    # # 定位输入框，按enter
    # page.locator("#username").press("Enter")

    # page.pause()

    page.goto("file:///D:/Project/web_ui/section3/press.html")
    page.locator("#btn").click()

    # 粘贴到其他输入框
    page.locator("#copy").press("Control+V")

    # 拿到复制板里面的内容
    y = pyperclip.paste()
    print(f"粘贴板的内容：", y)

    page.pause()

    context.close()
    browser.close()
