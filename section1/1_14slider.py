from playwright.sync_api import sync_playwright
import base64
import ddddocr
import random

"""
简单图像验证
"""

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demos.geetest.com/slide-float.html")

    # 点击按钮，出现滑动验证码
    page.locator(".geetest_wait").click()

    # 获取 canvas 元素背景图
    bg_base64 = page.evaluate(
        "document.getElementsByClassName('geetest_canvas_bg geetest_absolute')[0].toDataURL('image/ png')"
    )
    fullbg_base64 = page.evaluate(
        "document.getElementsByClassName('geetest_canvas_fullbg geetest_fade geetest_absolute')[0].toDataURL('image/ png')"
    )
    # print(bg_base64)
    # base64 图片编码
    with open("bg_img.png", "wb") as f:
        bg_b = str(bg_base64).split(",")[-1]
        f.write(base64.b64decode(bg_b))

    with open("fullbg_img.png", "wb") as f:
        fullbg_b = str(fullbg_base64).split(",")[-1]
        f.write(base64.b64decode(fullbg_b))

    # 识别缺口位置
    slide = ddddocr.DdddOcr(show_ad=False, ocr=False, det=False)
    with open("bg_img.png", "rb") as f:
        target_bytes = f.read()

    with open("fullbg_img.png", "rb") as f:
        background_bytes = f.read()

    res = slide.slide_comparison(target_bytes, background_bytes)
    print(res)
    gap = res.get("target")[0]
    print(f"缺口位置：{gap}")

    slider_button = page.locator(".geetest_slider_button")
    button = slider_button.bounding_box()
    print(button)

    # 开始拖动滑块
    page.mouse.move(x=button["x"], y=button["y"] + button["height"] / 2)
    page.mouse.down()
    page.wait_for_timeout(300)

    page.mouse.move(
        x=button["x"] + gap + random.randint(2, 8), y=button["y"] + button["height"] / 2
    )
    page.wait_for_timeout(500)
    page.mouse.move(x=button["x"] + gap - 2, y=button["y"] + button["height"] / 2)
    page.mouse.move(x=button["x"] + gap - 6, y=button["y"] + button["height"] / 2)
    page.wait_for_timeout(300)
    page.mouse.move(x=button["x"] + gap - 8, y=button["y"] + button["height"] / 2)
    page.mouse.up()

    page.close()
