list = [1,2,3,4,5,6,7,8,9,10]

def list_while_func():
    i = 0       #   用變量表示下標
    newlist = []
    while i < len(list):    # 長度是10,下標是0~9,故設定為'<'
        element = list[i]
        if element % 2 == 0:
            newlist.append(element)
        i += 1
    print(f"通過while迴圈，從列表 : {list}中取出偶數，組成新列表 : {newlist}")

def list_for_func():
    newlist = []
    for element in list:
        if element % 2 == 0:
            newlist.append(element)
    print(f"通過for迴圈，從列表 : {list}中取出偶數，組成新列表 : {newlist}")


list_while_func()
list_for_func()