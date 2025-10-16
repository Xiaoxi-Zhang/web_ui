from playwright.sync_api import sync_playwright, expect


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.baidu.com/")

    # 元素存在
    loc1 = page.locator("id=kw")
    print(loc1)
    print(loc1.count())  # 统计元素个数

    # 元素不存在
    loc2 = page.locator("id=yoyo")
    print(loc2)
    print(loc2.count())

    # query
    # 元素存在
    loc3 = page.query_selector("#kw")
    print(loc3)

    # 元素不存在
    loc4 = page.query_selector("#yoyo")
    print(loc4)

    page.pause()

    context.close()
    browser.close()
