# 私有成員變量和私有成員方法的使用，定義錢加上 __ (兩個下劃線)

# 私有:代表只能由'內部'進行使用，類對象無法訪問

class Phone:
    __current_voltage = 0.5        # 當前手機運行電壓

    def __keep_single_core(self):
        print("讓CPU以單核模式運行")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5G通話已開啟")
        else:
            self.__keep_single_core()
            print("電量不足，無法使用5G通話，已設定為單核運行進行省電")

phone = Phone()
phone.call_by_5g()