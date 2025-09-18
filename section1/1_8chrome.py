from playwright.sync_api import sync_playwright
import getpass

print(getpass.getuser())

USER_DIR_PATH = (
    f"C:\\Users\\{getpass.getuser()}\\AppData\\Local\\Google\\Chrome\\User Data"
)

with sync_playwright() as p:
    context = p.chromium.launch_persistent_context(
        headless=False, user_data_dir=USER_DIR_PATH, channel="chrome"， bypass_csp=True
    )
    page = context.new_page()
    print("准备去139邮箱")
    page.goto("https://html5.mail.10086.cn/")
    print("跳转完成")
    print(page.title())
    page.pause()

    context.close()
