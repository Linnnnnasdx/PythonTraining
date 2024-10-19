# while 迴圈

#無窮迴圈
#n=1
#while True:
#    print(n)
#    n+=1

#n=1
#while n<=3:
#    print(n)
#    n+=1

#1+2+3+...+10
#n=1
#sum=0       # 紀錄累加的結果
#while n<=10:
#    sum=sum+n
#    n+=1
#print(sum)

# for 迴圈

#for x in "Hello":
#    print(x)

#for x in range(5):      #使用range() for x in range(5) 相當於 for x in [0,1,2,3,4]      不包含5
#    print(x)

#for y in range(5,10):       #for x in range(5,10) 相當於 for x in [5,6,7,8,9]    包含開頭不包含結尾
#    print(y)

sum=0
for x in range(1,11):
    sum=sum+x
print(sum)