from playwright.sync_api import sync_playwright, expect

import cv2
import numpy as np


def img_mat_rgb_2_gray(img_mat):
    """
    Turn img_mat into gray_scale, so that template match can figure the img data.
    "print(type(im_search[0][0])")  can check the pixel type.
    """
    assert isinstance(img_mat[0][0], np.ndarray), "input must be instance of np.ndarray"
    return cv2.cvtColor(img_mat, cv2.COLOR_BGR2GRAY)


def cal_ccoeff_confidence(im_source, im_search):
    """求取两张图片的可信度，使用TM_CCOEFF_NORMED方法."""
    # 扩展置信度计算区域
    im_source = cv2.copyMakeBorder(im_source, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
    # 加入取值范围干扰，防止算法过于放大微小差异
    im_source[0, 0] = 0
    im_source[0, 1] = 255

    im_source, im_search = img_mat_rgb_2_gray(im_source), img_mat_rgb_2_gray(im_search)
    res = cv2.matchTemplate(im_source, im_search, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    return max_val


def cal_rgb_confidence(img_src_rgb, img_sch_rgb):
    """同大小彩图计算相似度."""
    # 减少极限值对hsv角度计算的影响
    img_src_rgb = np.clip(img_src_rgb, 10, 245)
    img_sch_rgb = np.clip(img_sch_rgb, 10, 245)
    # 转HSV强化颜色的影响
    img_src_rgb = cv2.cvtColor(img_src_rgb, cv2.COLOR_BGR2HSV)
    img_sch_rgb = cv2.cvtColor(img_sch_rgb, cv2.COLOR_BGR2HSV)

    # 扩展置信度计算区域
    img_src_rgb = cv2.copyMakeBorder(img_src_rgb, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
    # 加入取值范围干扰，防止算法过于放大微小差异
    img_src_rgb[0, 0] = 0
    img_src_rgb[0, 1] = 255

    # 计算BGR三通道的confidence，存入bgr_confidence
    src_bgr, sch_bgr = cv2.split(img_src_rgb), cv2.split(img_sch_rgb)
    bgr_confidence = [0, 0, 0]
    for i in range(3):
        res_temp = cv2.matchTemplate(src_bgr[i], sch_bgr[i], cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res_temp)
        bgr_confidence[i] = max_val

    return min(bgr_confidence)


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://html5.mail.10086.cn/")  # load

    page.get_by_text("账号登录").click()
    page.get_by_placeholder("移动认证账号/手机号/别名").fill("13149230717")
    page.get_by_placeholder("密码").fill("ZXXld@146192")
    page.locator('//*[@id="chkSimlogin"]').click()
    page.get_by_role("button", name="登录").click()
    # 切换到我的页面
    page.get_by_role("link", name="我的").click()

    # 等待，等图片加载完成
    page.wait_for_load_state("networkidle")
    # 定位图片
    img_tou = page.locator("#imgUserAvatar")

    # 判断src 不等于 src='/static/users/error-img.png'
    src = img_tou.get_attribute("src")
    print("头像图片的src属性值为：", src)
    assert src != "/static/users/error-img.png"

    # 保存图片
    img_tou.screenshot(path="D:\Project\web_ui\section4\images/result01.png")

    # 对比图片
    img1 = cv2.resize(
        cv2.imread("D:\Project\web_ui\section4\images/result01.png"), (100, 100)
    )
    img2 = cv2.resize(
        cv2.imread("D:\Project\web_ui\section4\images/expect01.png"), (100, 100)
    )
    res1 = cal_ccoeff_confidence(img1, img2)
    print("img1 vs img2 相似度对比结果: ", res1)
    # 断言相似度大于0.5
    assert res1 >= 0.5
