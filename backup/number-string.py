#數字、字串的基本運算
# X的Y次方:X**Y

# 數字運算
# x=3/6 #小數除法
# print(x)
# y=7//6 #整數除法
# print(y)
# z=2**3 #平方
# print(z)
# a=2**0.5 #開根號
# print(a)
# b=7%3 #取餘數
# print(b)

# c=2+3
# print(c)
# c+=1 #c=c+1 #將變數中的數字+1
# print(c)


# 字串運算
s="Hello"
print(s)
t="Hell\"o" # \ ->跳脫 與外符號做區隔
print(t)
m="Hello"+" World" # 用+或者空格(python)代表字串的串接
print(m)
p="Hello\n\n\nWorld" # 用\n或者"""Hello換行World"""(python)都可代表換行
print(p)
k="Hello"*3+"World" #先乘除後加減
print(k)

# 字串會對內部的字元編號(索引)，從0開始算起
u="Hello"
print(u[0])
g="Hello"
print(g[1:4]) #快速取得內部字串   #包含開頭不包含結尾
w="Hello"
print(w[1:]) #除了開頭
q="Hello"
print(q[:4]) #除了結尾
