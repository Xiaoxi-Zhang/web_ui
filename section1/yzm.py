"""
验证码识别
ddddocr -- 第三方库
"""

import ddddocr

ocr = ddddocr.DdddOcr(show_ad=False)
with open("yzm.png", "rb") as f:
    yzm_img = f.read()
yzm = ocr.classification(yzm_img)
print(yzm)
