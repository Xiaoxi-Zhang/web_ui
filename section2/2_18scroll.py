from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
    page.goto("https://www.runoob.com/")
    # click 自动滚动到元素出现的位置
    # page.get_by_text("【学习 Django】").click()

    # 滚动到元素出现的位置
    # page.get_by_text("【学习 Django】").scroll_into_view_if_needed()

    page.get_by_text("【学习 Django】").hover()

    page.pause()
