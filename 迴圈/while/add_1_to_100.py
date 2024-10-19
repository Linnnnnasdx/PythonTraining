num = 1
sum = 0
while num <= 100:
    sum = sum + num
    num += 1
print(f"加總是{sum}")
print("加總是%d" % sum)
print("加總是" + str(sum))  #將數字轉成字串後輸出