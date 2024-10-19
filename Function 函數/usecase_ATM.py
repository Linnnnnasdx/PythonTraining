money = 5000000
name = input("請輸入您的名字: ")
select = None

def menu():
    print("\n---------------主菜單---------------\n")
    print(f"{name} 您好，歡迎來到拉麵銀行。請選擇操作:\n")
    print("查詢餘額  [輸入1]")
    print("存款      [輸入2]")
    print("取款      [輸入3]")
    print("退出      [輸入4]")
    global select
    select = int(input("\n請輸入您的選擇: "))

def check_balance(show_header):         #   透過參數控制
        if show_header:     #   如果show_header為True，則印出
            print("---------------查詢餘額---------------")
        print(f"\n{name}您好，您的餘額剩餘: {money}元")
        if money <= 100:
            print(f"\n哈哈，{name}，你是窮鬼")

def deposit(num):
        global money
        money += num
        print("---------------存款---------------")
        print(f"\n{name}您好，存款{num}元成功")
        check_balance(False)        #   False，不會印出show_header

def withdraw(num):
        global money
        money -= num
        print("---------------提款---------------")
        print(f"\n{name}您好，提款{num}元成功")
        check_balance(False)        #   False，不會印出show_header

while True:
    menu()
    if select == 1:
        check_balance(True)
        continue
    elif select == 2:
        num = int(input("請輸入存款金額: "))
        deposit(num)
        continue
    elif select == 3:
        num = int(input("請輸入提款金額: "))
        withdraw(num)
        continue
    elif select == 4:
        print("\n---祝您有美好的一天 !---\n")
        break
    else:
        print("\n---輸入錯誤---\n")
        break