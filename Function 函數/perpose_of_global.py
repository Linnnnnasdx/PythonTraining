#   global 的用途
num = 100

def testA():
    print(num)

def testB():
    global num      #將函數內的'局部變量'定義成'全局變量'
    num = 200
    print(num)

testA()
testB()
print(f'全局變量的 num = {num}')