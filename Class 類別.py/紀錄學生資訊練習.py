class student:
    def __init__(self,name,age,addr):
        self.name = name
        self.age = age
        self.addr = addr
        
for num in range(1,11) :
    print(f"當前錄入第{num}位學生訊息，總共需錄入10位學生訊息")
    name = input("請輸入學生姓名:")
    age = input("請輸入學生年齡:")
    addr = input("請輸入學生地址:")
    
    stu = student(name,age,addr)
    print(f"學生{num}錄入完成，訊息為: 【學生姓名: {name},年齡: {age},地址: {addr}】")