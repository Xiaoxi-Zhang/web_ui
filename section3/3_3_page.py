"""
监听事件
1. context.on("page") 监听新标签页打开事件
2. page.on("popup") 监听新标签页打开事件
"""

from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
    page.goto("https://www.baidu.com/")

    # def handle_page(page):
    #     page.wait_for_load_state()  # 等待页面加载到load状态
    #     print("新标签页的title:", page.title())

    # context.on("page", handle_page)  # 监听新标签页打开事件

    def handle_popup(popup):
        popup.wait_for_load_state()  # 等待页面加载到load状态
        print("新标签页的title:", popup.title())

    page.on("popup", handle_popup)  # 监听新标签页打开事件

    page.get_by_role("link", name="新闻").click()  # 触发事件
    print("当前标签页的title:", page.title())

    page.pause()
