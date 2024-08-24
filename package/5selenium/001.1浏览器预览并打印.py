from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time, json


settings = {
    "recentDestinations": [{"id": "Save as PDF", "origin": "local", "account": ""}],
    "selectedDestinationId": "Save as PDF",
    "version": 2,
    "isHeaderFooterEnabled": True,
    # "customMargins": {},
    # "marginsType": 2,
    "scaling": 100, # 缩放
    # "scalingType": 3,
    # "scalingTypePdf": 3,
    "isLandscapeEnabled": False,  # landscape横向，portrait 纵向，若不设置该参数，默认纵向
    "isCssBackgroundEnabled": True,
    "mediaSize": {
        "height_microns": 297000,
        "name": "ISO_A4",
        "width_microns": 210000,
        "custom_display_name": "A4 210 x 297 mm",
    },
}


options = Options()
# options.add_argument('--headless') # 不显示图形界面
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# 打印相关配置
options.add_argument("--enable-print-browser")
options.add_argument("--kiosk-printing")  # 静默打印，无需用户点击打印页面的确定按钮(执行打印操作)
# options.add_argument("--print-to-pdf") # 

# 下面配置可打印输出出pdf(入宫没有则默认打印，而不是导出pdf)
pdf_path = "D:\WeChat"
prefs = {
    "printing.print_preview_sticky_settings.appState": json.dumps(settings),
    "savefile.default_directory": pdf_path,  # 此处填写文件保存的路径
}
options.add_experimental_option('prefs', prefs)

# 告诉浏览器：“嗨，我知道你在检测自动化行为，但请相信我，这是人工操作，而不是机器人操作。” 
options.add_experimental_option('excludeSwitches', ['enable-automation'])

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options, service)

driver.get("https://baidu.com")
time.sleep(1)  # 加载等待
print(driver.title)

# 点击打印按钮
# print_button = driver.find_element_by_css_selector(".print-button")
# print_button.click()
# 模拟打印按钮测试
driver.execute_script('document.title="{}";window.print();'.format("测试")) #利用js修改网页的title，该title最终就是PDF文件名，利用js的window.print可以快速调出浏览器打印窗口，避免使用热键ctrl+P

# 切换到打印预览模式
# 切换到新打开的窗口
# print(1111111111)
# driver.switch_to.window(driver.window_handles[-1])
# print(222222222222)

# 关闭浏览器
driver.close()