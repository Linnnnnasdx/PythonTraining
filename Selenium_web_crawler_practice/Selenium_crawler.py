# 載入 Selenium 相關模組
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# 設定 Chrome Driver 的執行檔路徑
options = Options()
options.chrome_executable_path = "D:\python training\Selenium_web crawler_practice\chromedriver.exe"
# 建立 Driver 物件實體，用程式操作瀏覽器運作
driver = webdriver.Chrome(options=options)

# 連線到PTT股票版
driver.get("https://www.ptt.cc/bbs/stock/index.html")
# print(driver.page_source)   # 取得網頁的原始碼

"""取得股票版中的文章標題"""
tags = driver.find_elements(By.CLASS_NAME, "title")    # 搜尋 class 屬性是 title 的所有標籤
for tag in tags:
    print(tag.text)

"""點擊上頁，並取得文章標題"""
link = driver.find_element(By.LINK_TEXT,"‹ 上頁")
link.click()    # 模擬使用者的點擊
tags = driver.find_elements(By.CLASS_NAME, "title")    # 搜尋 class 屬性是 title 的所有標籤
for tag in tags:
    print(tag.text)

driver.close()

"""用for迴圈選擇要點幾次"""
# tags = driver.find_elements(By.CLASS_NAME, "title") 
# for tag in tags:
#     print(tag.text)
# for num in range(5):
#     link = driver.find_element(By.LINK_TEXT,"‹ 上頁")
#     link.click()    # 模擬使用者的點擊
#     tags = driver.find_elements(By.CLASS_NAME, "title")    # 搜尋 class 屬性是 title 的所有標籤
#     for tag in tags:
#         print(tag.text)
# driver.close()