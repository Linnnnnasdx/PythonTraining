"""數據定義的類"""

class Record:
    def __init__(self,date,order_id,money,province):
        self.date = date            # 訂單日期
        self.order_id = order_id    # 訂單ID
        self.money = money          # 訂單金額
        self.province = province    # 銷售省份

# __str__() 只在你直接打印單個物件時才會被調用。
    def __str__(self) -> str:
        return f"{self.date}, {self.order_id}, {self.money}, {self.province}"
    
# 需要打印一整個列表時可以使用 __repr__() ，通常用來返回開發者使用的物件表現形式