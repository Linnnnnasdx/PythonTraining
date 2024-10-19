# '子類' 複寫(修改) '父類'成員
class Phone:        # 父類
    IMEI = None     # 序列號
    producer = "ITCAST" # 廠商

    def call_by_4g(self):
        print("使用4g通話")

class Myphone(Phone):       # 子類
    producer = "ITHEIMA"
    def call_by_4g(self):
        print("開啟單核模式")

        # 複寫後，調用父類成員
        # 方式1
        print(f"父類的廠商是: {Phone.producer}")
        Phone.call_by_4g(self)

        # 方法2
        print(f"父類的廠商是: {super().producer}")
        super().call_by_4g()

p = Myphone()
p.call_by_4g()
print(p.producer)