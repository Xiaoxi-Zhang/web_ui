from playwright.sync_api import sync_playwright, expect


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.baidu.com/")

    # 判断是不是正常打开
    print(page.title())
    print(page.url)
    # assert page.title() == "百度一下，你就知道"
    # assert page.url == "https://www.baidu.com/"

    expect(page).to_have_title("百度一下，你就知道")
    expect(page).to_have_url("https://www.baidu.com/")

    page.pause()

    context.close()
    browser.close()
