class student:
    name = None     # 成員變量

    def say_hi(self):       # 成員方法
        print(f"大家好，我是{self.name}")

    def say_hi2(self,msg):
        print(f"大家好，我是{self.name},{msg}")

stu = student()     # 基於類別創建對象，讓對象做具體的工作
stu.name = "林鈺翔"
stu.say_hi()

stu2 = student()
stu.name = "薛亦晴"
stu.say_hi2("水水水")