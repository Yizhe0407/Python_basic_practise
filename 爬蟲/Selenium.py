# 載入Selenium相關模組
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

# 設定 Edge Driver 的執行檔路徑
options = Options()
options.edge_executable_path = r"C:\Users\yizhe\Dropbox\vscode\Python\爬蟲\msedgedriver.exe"
driver = webdriver.Edge(options=options)

# Navigate to the Google homepage
driver.maximize_window()  # 視窗最大化
driver.get("https://webapp.yuntech.edu.tw/YunTechSSO/Account/Login")
usernameInput = driver.find_element(By.ID, 'pLoginName')
passwordInput = driver.find_element(By.ID, 'pLoginPassword')
usernameInput.send_keys("B11217003")
passwordInput.send_keys("Rafe47max")
signinBtn = driver.find_element(By.ID, 'LoginSubmitBtn')
signinBtn.send_keys(Keys.ENTER)
time.sleep(0.1)
driver.get("https://eclass.yuntech.edu.tw/yuntech/sso-login")
time.sleep(0.1)
driver.get("https://eclass.yuntech.edu.tw/user/courses")

# driver.quit()
