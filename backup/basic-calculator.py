# 建立基本計算機

n1 = input("請輸入第一個數字:")
n1 = int(n1)
n2 = input("請輸入第二個數字:")
n2 = int(n2)
op = input("請輸入運算元:")
if op == "+":
    print(n1+n2)
elif op == "-":
    print(n1-n2)
elif op == "*":
    print(n1*n2)
elif op == "/":
    print(n1/n2)
else:
    print("無解")