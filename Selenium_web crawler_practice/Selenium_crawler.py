# 載入 Selenium 相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# 設定 Chrome Driver 的執行檔路徑
options = Options()
options.chrome_executable_path = "D:\python training\Selenium_web crawler_practice\chromedriver.exe"
# 建立 Driver 物件實體，用程式操作瀏覽器運作
driver = webdriver.Chrome(options=options)
# 連線到PTT股票版


driver.close()