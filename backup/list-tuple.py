# 有序"可"變動的列表 List #[]

#grades=[12,60,15,70,90]
#print(grades)
#grades[0]=55    # 把 55 放到列表中第一個位置
#print(grades[0])    # 索引編號取資料

#grades[1:4]=[]      # 連續刪除列表中從編號 1 到編號 4 (不包括) 的資料
#print(grades[1:4])    # 包含開頭不包含結尾

#grades=grades+[12,33]       # 加在後方   #看到等號先看等號右邊
#print(grades)

#length=len(grades)      # 取得列表的長度(資料數量)     
#print(length)      #len(列表資料)

#data=[[3,4,5],[6,7,8]]      # 巢狀列表:列表中的資料也是列表
#print(data)
#print(data[0][1])       # print(變數名稱[第一層第0個][第二層第1個])
#data[0][0:2]=[5,5,5]       #將 3,4 換成 5,5,5
#print(data)


# 有序"不可"變動列表 Tuple # ()

data=(3,4,5)        #Tuple用()，List用[]
data[0]=5       # 錯誤: Tuple的資料不可以變動
print(data)