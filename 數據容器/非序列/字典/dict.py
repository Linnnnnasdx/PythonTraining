# 字典的運算: key-value 配對
# Key 不可重複，Key 也不可為字典

my_dic1 = {}
my_dic2 = dict()    # 兩個都代表空集合

stu_scores_dict = {     # 字典的嵌套使用
    "Lin":{
        "語文":77,
        "數學":88,
        "英文":99
    },"Jay":{
        "語文":22,
        "數學":33,
        "英文":44
    },"Ray":{
        "語文":55,
        "數學":66,
        "英文":77
    }
}
print(stu_scores_dict)

stu_scores_dict.pop("Ray")  # 刪除此Key的鍵值對
print(stu_scores_dict)

stu_scores_dict["gaga"] = {"語文":69,"數學":79,"英文":89}   # 新增元素
print(stu_scores_dict)

score = stu_scores_dict["Jay"]["語文"]  # 查詢
print(f"Jay的語文成績是:{score}")

keys = stu_scores_dict.keys()       # 字典.keys() 可獲取字典中全部的key
print(f"字典的全部Keys是:{keys}")

for key in keys:        # 用key遍歷取得value，也可以將keys換成字典直接循環
    print(f"字典{key}的value是{stu_scores_dict[key]}")

num = len(stu_scores_dict)
print(f"字典中的元素數量有:{num}個")

stu_scores_dict.clear()
print("字典被清空拉 !")