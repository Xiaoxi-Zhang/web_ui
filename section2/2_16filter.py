from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
    page.goto("file:///D:/Project/web_ui/section2/demo.html")

    items = page.locator(".item")
    for item in items.all():
        print("item------", item.inner_html())

    # filter 筛选
    x = items.filter(has_text="playwright")
    print("filter------", x.inner_html())

    # locator 继续定位
    y = items.locator("text=playwright")
    print("locator------", y.inner_html())

    # locator 加上has_text
    a = page.locator(".item", has_text="playwright")
    print("has_text------", a.inner_html())
    # 等价于
    aa = page.locator(".item").filter(has_text="playwright")
    print("has_text------", aa.inner_html())

    # filter 可以传 has_text 和 has
    c = page.locator(".item").filter(has=page.get_by_text("playwright"))
    print("has------", c.inner_html())

    page.pause()
