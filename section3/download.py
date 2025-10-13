from playwright.sync_api import sync_playwright

import os


downloads_dir = os.path.join(os.getcwd(), "法律文书")
os.makedirs(downloads_dir, exist_ok=True)  # 如果文件夹不存在则创建

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
    page.goto(
        "https://zxfw.court.gov.cn/zxfw/#/pagesAjkj/app/wssd/index?qdbh=51b6806faba54b718af8e3c7f40d0a55&sdbh=d8512b82cbe64467b9ef5fd2270c7bdc&sdsin=285f970162fee9933ce570c5471050c3"
    )

    univiews = page.locator('//uni-view[@class="fd-file-container"]')
    # print("uniview如下：", univiews)
    count = univiews.count()
    # print("univiews的数量：", count)

    for i in range(count):
        univiews.nth(i).click()
        page.wait_for_timeout(3000)  # 等待iframe加载
        # 先定位iframe
        iframe = page.frame_locator("iframe")
        # 再在iframe内定位下载按钮
        download_btn = iframe.locator('//button[@id="download"]')
        if download_btn.is_visible():
            with page.expect_download() as download_info:
                download_btn.click()
            download = download_info.value
            # 在文件名前加编号，避免重名覆盖
            filename = f"{i+1}_{download.suggested_filename}"
            save_path = os.path.join(downloads_dir, filename)
            download.save_as(save_path)
            print(f"第{i+1}个文件已下载：", filename)
        else:
            print(f"第{i+1}个文件下载失败：", filename)

        page.wait_for_timeout(3000)  # 等待下载完成或弹窗关闭

    page.pause()

    context.close()
    browser.close()
