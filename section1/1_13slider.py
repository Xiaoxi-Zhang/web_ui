from playwright.sync_api import sync_playwright
import ddddocr

"""
简单图像验证
"""

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()

    page.goto(
        "https://www.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"
    )
    img_loc = page.locator("#imgCode")
    # 截图
    img_loc.screenshot(path="yzm.png")

    # 识别验证码
    ocr = ddddocr.DdddOcr(show_ad=False)
    with open("yzm.png", "rb") as f:
        yzm_img = f.read()
    yzm = ocr.classification(yzm_img)
    print(yzm)

    # 写入验证码
    page.locator("#code").fill(yzm)
    page.pause()
