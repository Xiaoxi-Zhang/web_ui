from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
    page.goto("file:///D:/Project/web_ui/section2/demo.html")

    # a1 = page.locator("#a1")
    # print(a1)
    # a1.click()

    # all = page.locator('[type="checkbox"]')
    # print(all)
    # all.click()
    # page.pause()

    # first last
    all = page.locator('[type="checkbox"]')
    # all.first.click()
    # all.last.click()

    # page.pause()

    # nth(index)
    # all.nth(0).click()
    # all.nth(2).click()

    # count 统计个数
    # count = all.count()
    # print(count)
    # for index in range(count):
    #     all.nth(index).click()

    # all() 得到所有元素
    # elements = all.all()
    # print(elements)

    for ele in all.all():
        ele.click()

    page.pause()
