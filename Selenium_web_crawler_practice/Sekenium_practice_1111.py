"""Fail"""

# 載入 Selenium 相關模組
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time

# 設定 Chrome Driver 的執行檔路徑
options = Options()
options.chrome_executable_path = "D:\python training\Selenium_web crawler_practice\chromedriver.exe"
# 建立 Driver 物件實體，用程式操作瀏覽器運作
driver = webdriver.Chrome(options=options)
# 連到linkedin
driver.get("https://www.104.com.tw/jobs/search/?jobcat=2004001005,2004001007,2004001004&jobsource=joblist_search&keyword=%E8%BB%9F%E9%AB%94%E5%B7%A5%E7%A8%8B%E5%B8%AB&order=15&page=2")

n = 0
while n < 3:
    # 捲動視窗並等待瀏覽器載入更多內容
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")    # 捲動視窗到底部

    # 直接暫停時間，但不是最優解
    time.sleep(2)
    # 使用 JavaScript 檢查 document.readyState 是否為 complete，表示頁面已完全載入。
    # WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
    n+=1

# 取得網頁中職缺的標題
titleTags = driver.find_elements(By.XPATH, "//a[contains(@class, 'info-ellipsis')]")
for titleTag in titleTags:
    print(titleTag.text)

driver.close()