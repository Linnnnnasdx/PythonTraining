# 函數的多返回值
def test_return():
    return 1,"hello",True

x,y,z = test_return()
print(x)
print(y)
print(z)

def user_info(name,age,gender):
    print(f"姓名是 :{name},年齡是 :{age},性別是 :{gender}")

# 位置參數
user_info('小名',20,'男')   

# 關鍵字參數
user_info(age = '11',name = '小王',gender = '女')   

user_info('小莉',age = 32,gender = '女')    # 可以不按照順序

# 缺省參數 (默認值)，必須放最後面
def user_info(name,age,gender = '男'):  
    print(f"姓名是 :{name},年齡是 :{age},性別是 :{gender}")

user_info('小天',13)

# 不定長 - 位置不定長, * 號
# 會作為'Tuple'存在，接收不定長數量的參數傳入
# 形式參數通常命名為 args
def user_info(*args):
    print(f"args參數的類型是 :{type(args):},內容是 :{args}")

user_info(1,2,3,'小明','男孩')

# 不定長 - 關鍵字不定長, ** 號
# 形式參數通常命名為 kwargs
def user_info(**kwargs):
    print(f"args參數的類型是 :{type(kwargs):},內容是 :{kwargs}")

user_info(name = '小王',age = 11,gender = '男孩',addr = '宜蘭')