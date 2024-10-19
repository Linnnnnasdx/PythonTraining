#   列表.index(元素) - 查詢某元素在列表中的下標索引
mylist = ["a","b","c"]

index = mylist.index("b")
print(f"b 的下標索引是 : {index}")

#   修改特定下標索引的值
mylist[0] = "123"
print(f"修改後結果是 : {mylist}")

#   列表.insert(元素) - 在指定位置插入元素
mylist.insert(1,"best")
print(f"插入後結果是 : {mylist}")

#   列表.append(元素) - 在列表尾部追加元素
mylist.append("讚喔")
print(f"在列表後追加元素，結果是 : {mylist}")

#   列表.extend(元素) - 在列表尾部追加'新的列表'，也就是延伸列表
mylist2 = ["x","y","Z"]
mylist.extend(mylist2)
print(f"在列表後追加另一個列表，結果是 : {mylist}")

#   刪除'指定下標'列表的元素(2種方式)

#   方式1:  del 列表[下標]
mylist = ["a","b","c"]
del mylist[0]
print(f"刪除一個元素後，結果是 : {mylist}")

#   方式2:  列表.pop(下標)
mylist = ["a","b","c"]
element = mylist.pop(1)
print(f"使用pop取出一個元素後，結果是 : {mylist} , 取出的元素是 {element}")

#   列表.remove(元素) - 刪除指定'元素'
mylist = ["a","b","c"]
mylist.remove("c")
print(f"使用remove刪除指定元素，結果是 : {mylist}")

#   列表.clear() - 清空列表
mylist.clear()
print("列表被清空了!")

#   列表.count(元素) - 統計某元素在列表中的數量
mylist = ["a","b","c","a","b"]
count = mylist.count("c")
print(f"列表中c的數量是 : {count}")

#   len(列表) - 統計列表中全部的元素數量
mylist = ["a","b","c","a","b"]
lentgh = len(mylist)
print(f"列表的全部數量總共有: {lentgh} 個")
