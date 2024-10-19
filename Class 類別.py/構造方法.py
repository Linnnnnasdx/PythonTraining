# 溝造方法的名稱 : __init__ (兩條下劃線)
# 構造方法的作用 :
# 1.構建類對象時，會自動執行
# 2.構建類對象的傳參會傳遞給構造方法，藉此特性可以給成員變量賦值

class student:

    def __init__(self,name,age,tel):
        # 在方法內使用成員變量一樣要使用self
        self.name = name
        self.age = age
        self.tel = tel
        print("student類創造了一個類對象")

stu = student("林鈺翔",22,"0985440714")
print(stu.name)
print(stu.age)
print(stu.tel)