# 對形參進行類型註解
def add(x:int,y:int):
    return x+y

print(add(2,3))

# 對'返回值'進行註解
def func(data: list) -> list:
    return data