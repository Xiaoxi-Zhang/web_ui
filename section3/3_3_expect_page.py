"""
有 target="_blank" 的链接时，会打开一个新的标签页，有2种方式捕获到新页面的page对象
- 1. context.expect_page() 获取新标签页对象
- 2. page.expect_popup() 获取新标签页对象
"""

from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
    page.goto("https://www.baidu.com/")

    # 点新闻
    with context.expect_page() as new_page_info:
        page.get_by_role("link", name="新闻").click()
    new_page = new_page_info.value

    print(page.title())  # 操作百度
    print(new_page.title())  # 操作新页面
    new_page.get_by_text("地图").click()

    page.pause()
