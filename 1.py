from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置Chrome选项
chrome_options = Options()
chrome_options.add_argument("--headless")  # 无头模式，不打开浏览器窗口

# 初始化WebDriver
service = Service(r'/usr/local/bin/chromedriver')  # 替换为你的chromedriver路径
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # 打开登录页面
    driver.get('https://www.zukongguan.com')

    # 输入用户名和密码
    username = driver.find_element(By.NAME, 'username')  # 替换为实际的用户名输入框的name属性
    password = driver.find_element(By.NAME, 'password')  # 替换为实际的密码输入框的name属性
    username.send_keys('2895530786@qq.com')  # 替换为你的用户名
    password.send_keys('liuzhijiao641')  # 替换为你的密码
    password.send_keys(Keys.RETURN)

    # 等待页面加载并找到签到按钮
    wait = WebDriverWait(driver, 10)
    sign_in_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[onclick*="NimbaAjax"]')))



    # 点击签到按钮
    sign_in_link.click()

    print("签到成功！")

finally:
    # 关闭浏览器
    driver.quit()
