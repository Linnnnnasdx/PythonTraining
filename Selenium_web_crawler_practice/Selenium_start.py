# 載入 Selenium 相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# 設定 Chrome Driver 的執行檔路徑
options = Options()
options.chrome_executable_path = "D:\python training\Selenium_web crawler_practice\chromedriver.exe"
# 建立 Driver 物件實體，用程式操作瀏覽器運作
driver = webdriver.Chrome(options=options)
driver.maximize_window()    # 視窗最大化
driver.get("https://www.google.com/")
driver.save_screenshot("screenshot-google.png")    # 截圖
driver.get("https://www.usc.edu.tw/")
driver.save_screenshot("screenshot-USC.png") 
driver.close()