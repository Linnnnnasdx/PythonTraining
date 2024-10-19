num = 5
if int(input("請猜一個數字: ")) == num:
    print("恭喜，一次答對!")
elif int(input("猜錯了，再猜一次: ")) == num:
    print("恭喜答對!")
elif int(input("猜錯了，再猜一次: ")) == num:
    print("恭喜終於答對!")
else:
    print("你輸了")