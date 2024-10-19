# 模組:獨立的程式檔案，將程式寫在一個檔案中，此檔案可重複載入使用
# 載入->使用 : 先載入模組，在使用模組中的函式或變數
# 基本語法 1. import 模組名稱
#         2. import 模組名稱 as 模組別名 
# 內建模組 : 例如 sys

# 載入內建的 sys 模組並取得資料
# import sys as s
# print(s.platform)
# print(s.maxsize)

#建立 grometry 模組，載入使用
# import geometry as g
# result=g.distance(1,1,5,5)
# print(result)
# result=g.slope(1,2,5,6)
# print(result)

# 調整搜尋模組的路徑
import sys
sys.path.append("modules")      # 在模組的搜尋路徑列表中【新增路徑】
print(sys.path)     # 印出模組的搜尋路徑列表
print("---------------------------")
import geometry
print(geometry.distance(1,1,5,5))