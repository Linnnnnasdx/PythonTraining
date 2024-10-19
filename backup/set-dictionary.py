# 集合的運算

# s1={3,4,5}
# print(10 not in s1)     #用 in 或者 not in 表示資料是否在集合中     #True or False

# s1={3,4,5}
# s2={4,5,6,7}
# s3=s1&s2    # 交集: 取兩個集合中，相同的部分
# s3=s1|s2    # 聯集: 取兩個集合中的所有資料，但"不重複"取
# s3=s1-s2    # 差集: 對集合做減法，從 s1 中，減去 s2 "重疊"的部分
# s3=s1^s2    # 反交集: 取兩個集合中，不重疊的部分
# print(s3)

# s=set("Hello")      # 將字串中的字母拆解成集合: set(字串)
# print("H" in s)


# 字典的運算: key-value 配對
#dic={"apple":"蘋果","bug":"蟲蟲"}
#dic["apple"]="小蘋果"
#print(dic["apple"])

# dic={"apple":"蘋果","bug":"蟲蟲"}
# print("apple" in dic)       # 判斷 key 是否存在

#dic={"apple":"蘋果","bug":"蟲蟲"}
#print(dic)
#del dic["apple"]        # 刪除字典中的鍵值對 (key-value pair): del
#print(dic)

dic={x:x*2 for x in [3,4,5]}        # 從列表的資料產生字典
print(dic)