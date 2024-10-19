# 繼承分為'單繼承'和'多繼承'

# 單繼承
class Phone:        # 父類成員1
    IMEI = None     # 序列號
    producer = "ITCAST" # 廠商

    def call_by_4g(self):
        print("4g通話")


class Phone2022(Phone):     # 繼承寫法
    face_id = "10001"       # 面部識別ID

    def call_by_5g(self):
        print("2022年新功能：5g通話")


phone = Phone2022()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()


# 多繼承
class NFCReader:        # 父類成員2
    nfc_type = "第五代"
    producer = "HM"

    def read_card(self):
        print("NFC讀卡")

    def write_card(self):
        print("NFC寫卡")


class RemoteControl:        # 父類成員3
    rc_type = "紅外遙控"

    def control(self):
        print("紅外遙控開啟了")


class MyPhone(Phone, NFCReader, RemoteControl):
    pass        # 可以讓語法不出現錯誤，同時能成功執行


phone = MyPhone()
phone.call_by_4g()
phone.read_card()
phone.write_card()
phone.control()

# 若父類有同名方法or屬性，先繼承的優先於後面
print(phone.producer)
