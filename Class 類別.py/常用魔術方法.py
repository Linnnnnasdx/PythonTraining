
class Student:
    def __init__(self, name, age):
        self.name = name        # 學生姓名
        self.age = age          # 學生年齡

    # __str__() 字符串
    def __str__(self):
        return f"Student類對象，name:{self.name}, age:{self.age}"

    # __lt__() 小於符號比較
    def __lt__(self, other):
        return self.age < other.age

    # __le__() 小於等於比較
    def __le__(self, other):
        return self.age <= other.age

    # __eq__() 比較運算福
    def __eq__(self, other):
        return self.age == other.age


stu1 = Student("周傑輪", 31)
stu2 = Student("林俊節", 36)
print(stu1 == stu2)
