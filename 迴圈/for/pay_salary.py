import random

all_money = 10000

for i in range(1,21):
    num = random.randint(1,10)
    if num < 5 :
        print(f"員工{i}，績效分{num}，不發工資，下一位")
        continue
    if num >= 5:
        all_money = all_money - 1000
        print(f"向員工{i}發放1000元，帳戶餘額還剩餘{all_money}元")
    if all_money == 0:
        print("沒錢了，下個月再來")
        break