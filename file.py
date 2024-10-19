# Python 文字檔案的讀取和儲存

# 檔案操作流程 : 開啟檔案 -> 讀取或寫入 -> 關閉檔案
# 開啟檔案 : 檔案物件=open(檔案路徑,mode=開啟模式)
# 開啟模式 : 讀取模式 - r ； 寫入模式 - w ； 讀寫模式 - r+
# 讀取檔案 : 檔案物件.read()        # 讀取全部文字
# 一次讀取一行 : for 變數 in 檔案物件:

# 讀取 JSON 格式 :
# import json
# 讀取到的資料=json.load(檔案物件)

# 寫入檔案 : 檔案物件.write(字串)

# 寫入 JSON 格式 :
# import json
# json.dump(要寫入的資料，檔案物件)

# 關閉檔案 : 檔案物件.close()
# with open(檔案路徑,mode=開啟模式) as 檔案物件:
#   讀取或寫入的程式
# 以上區塊會自動、安全的關閉檔案
# JSON 格式 : JavaScript Object Notation (JavaScript 物件表示法)


# 儲存檔案
# file=open("data.txt",mode="w",encoding="utf8")      # 開啟
# file.write("測試中文\nSecond Line")        # 操作
# file.close()        # 關閉
with open("data.txt",mode="w",encoding="utf-8") as file:
    file.write("5\n3")


# 讀取檔案
# with open("data.txt",mode="r",encoding="utf-8") as file:
#     data=file.read()        # 讀取全部檔案
# print(data)

# 把檔案中的數字資料，一行一行的讀取出來，並計算總合。
# sum=0
# with open("data.txt",mode="r",encoding="utf-8") as file:
#     for line in file:       # 設定 line 為變數，將file中的資料，一行一行的讀取
#         sum+=int(line)      # int 將字串轉換成整數
# print(sum)


# 使用 JSON 格式讀取、複寫檔案
import json
# 從檔案中讀取 JSON 資料，放入變數 data 裡面
with open("config.json",mode="r") as file:
    data=json.load(file)        # 讀取 JSON 格式        
print(data)     # data 是一個字典資料
data["name"]="New Name"     # 修改變數中的資料
# 把最新的資料複寫回檔案中
with open("config.json",mode="w") as file:
    json.dump(data,file)        # 寫入 JSON 格式