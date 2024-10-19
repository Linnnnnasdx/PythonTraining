
def test(compute):
    result = compute(1,2)   # 確定compute是函數
    print(f"計算結果 :{result}")

def compute(x,y):
    return x + y

test(compute)   # 調用並傳用函數

# 匿名函數 - lambda 傳入參數: 函數體(一行代碼)
# 臨時使用，只能用一次，只能寫一行代碼
test(lambda x,y:x+y)