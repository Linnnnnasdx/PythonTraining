# 函式:程式碼包裝在一個區塊中，方便隨時呼叫使用
# 要先定義(建立)函式，然後才能呼叫(使用)函式      #定義->呼叫

# def 函式名稱(參數名稱):       #定義函式基本語法
#     函式內部的程式碼
#     return        #結束函式 回傳None
#     return 資料       #結束函式 回傳「資料」

# 函式名稱(參數資料)      #呼叫函式基本語法

# def say(msg):       #函式回傳None
#     print(msg)
#     return
# value=say("Hellooo")      #呼叫函式，取得回傳值
# print(value)        #印出 None

# def add(n1,n2):       #函式回傳字串 Hello
#     result=n1+n2
#     return "Hello"
# value=add(3,4)        #呼叫函式，取得回傳值
# print(value)      #印出 Hello

# def add(n1,n2):       #函式回傳n1+n2的結果
#     result=n1+n2
#     return result
# value=add(3,4)        #呼叫函式，取得回傳值
# print(value)      #印出 7

# 定義函式
# 函式內部的程式碼，若是沒有做函式呼叫，就不會執行
# def multiply(n1,n2):
#     print(n1*n2)
#     return n1*n2
# 呼叫函式
# value=multiply(3,4)
# print(value)

# def multiply(n1,n2):
#     return n1*n2
# value=multiply(3,4)+multiply(10,5)      #回傳值能在函式外部繼續操作資料
# print(value)

# 函式最大的用途就是做程式的包裝，同樣的邏輯可以重複利用
def calculate(min,max):
    sum=0
    for i in range(min,max+1):
        sum+=i
    print("前數+後數=",sum)

a=int(input("請輸入前數: "))
b=int(input("請輸入後數: "))

calculate(a,b)

