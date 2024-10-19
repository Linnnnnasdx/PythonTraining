# 參數的預設資料
# def power(base,exp=0):        # power開方；exp=0 為預設資料
#     print(base**exp)        # *是乘法，**是開方
# power(3,2)
# power(4)

# 使用參數名稱對應
# def divide(n1,n2):
#     print(n1/n2)
# divide(2,4)
# divide(n2=2,n1=4)

# 無限/不定 參數資料
def avg(*ns):
    sum=0
    for n in ns:
        sum+=n
    print(sum/len(ns))      # len 代表列表長度(數量)
avg(3,4)
avg(3,5,10)
avg(1,4,-1,-8)