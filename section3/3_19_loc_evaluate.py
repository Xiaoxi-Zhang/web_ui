from playwright.sync_api import sync_playwright, expect


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    # page.goto("http://47.116.12.183/login.html")

    # user = page.locator("#username")
    # # 输入
    # user.evaluate('node=> node.value="yoyo"')
    # # 获取输入框
    # res = user.evaluate('node=> node.value="yoyo"')
    # print(res)

    page.goto("https://www.baidu.com/index.htm")

    links = page.locator("#s-top-left > a")
    res = links.evaluate_all("nodes => nodes.length")
    print(res)

    page.pause()

    context.close()
    browser.close()
