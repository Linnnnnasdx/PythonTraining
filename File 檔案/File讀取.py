# 檔案的讀取、寫入

# open(”XXX.xxx”,mode=”開啟模式”)
# 絕對路徑 - ex: C/Users/desktop/python/123.txt
# 相對路徑 - 以程式的位置做延伸 ex: 123.txt

# mode=”r”    -讀取
# mode=”w”   -覆寫
# mode=”a”   -在原先的資料後寫東西

file = open("new/123.txt",mode = "r",encoding = "utf-8")
print(file.read(1))     # 不填數字默認全部
file.close()        # 文件若不關閉將會一直占用，也會影響到下一次讀取

# readline() 一次讀取一行，封裝到'列表'中
file = open("new/123.txt",mode = "r",encoding = "utf-8")
line1 = file.readline()
line2 = file.readline()
line3 = file.readline()
print(f"第一行的數據是: {line1}")
print(f"第二行的數據是: {line2}")
print(f"第三行的數據是: {line3}")
file.close()

# readlines() 讀取文件的全部行，封裝到'列表'中
file = open("new/123.txt",mode = "r",encoding = "utf-8")
lines = file.readlines()
print(f"lines對象的類型是: {type(lines)}")
print(f"lines對象的內容是: {lines}")
file.close()

file = open("new/123.txt",mode = "r",encoding = "utf-8")
for line in file:
    print(f"每一行的數據是: {line}")
file.close()

# 用with寫，程式會再結束後自動關閉檔案
with open("new/123.txt",mode = "a",encoding = "utf-8") as file:
    file.write("\n你好啊")