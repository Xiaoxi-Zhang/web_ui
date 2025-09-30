from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=2000)
    page = browser.new_page()
    page.goto("https://mail.163.com/")

    print(page.frames)
    for f in page.frames:
        print(f)

    # frame = page.frame_locator("[id^=x-URS-iframe]")
    # frame.get_by_placeholder("邮箱账号或手机号码").fill("13149230717")
    # frame.locator("[name='password']").fill("Zxcvbnm123")
    # frame.locator("#dologin").click()
    # 外面元素的操作
    # page.locator()

    page.pause()
    browser.close()
