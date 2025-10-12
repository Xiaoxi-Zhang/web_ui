from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.cnblogs.com/yoyoketang/?_wv=1031")

    # html内容
    # res = page.content()
    # print(res)

    # 获取元素的html
    res1 = page.locator("#blogTitle")
    # print(res1.inner_html())

    print(res1.inner_text())
    print("------------------")
    print(res1.text_content())

    page.pause()

    context.close()
    browser.close()
