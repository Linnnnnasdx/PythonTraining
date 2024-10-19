"""
面向對象，數據分析案例，主業務邏輯代碼
實現步驟：
1. 設計一個類，可以完成數據的封裝
2. 設計一個抽象類，定義文件讀取的相關功能，並使用子類實現具體功能
3. 讀取文件，生產數據對象
4. 進行數據需求的邏輯計算（計算每一天的銷售額）
5. 通過PyEcharts進行圖形繪制
"""

from file_define import FileReader,TextFileReader,JsonFileReader
from data_define import Record
from pyecharts.charts import Bar    # 柱狀圖
from pyecharts.options import *     # 可選選項
from pyecharts.globals import ThemeType     # 主題

text_file_reader = TextFileReader("C:/Users/LEGION/Desktop/python學習教材/资料/第13章/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("C:/Users/LEGION/Desktop/python學習教材/资料/第13章/2011年2月销售数据JSON.txt")

jan_data:list[Record] = text_file_reader.read_data()
feb_data:list[Record] = json_file_reader.read_data()

# 將2個月份的數據，合併為一個list
all_data:list[Record] = jan_data+feb_data

# 開始數據計算
# 運用字典，將date當成key，用累加的方式獲取整天的總營業額，然後for獲得每一天的數據
data_dict = {} 
for record in all_data:
    if record.date in data_dict.keys():
        # 當前日期已經有紀錄了，所以和同日期的銷售額做累加
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money       # 新增字典元素，key是date : value是money


# 資料視覺化開發
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))     # 這種寫法就是構建一個類別對象

bar.add_xaxis(list(data_dict.keys()))       # dict轉成list
bar.add_yaxis("銷售額",list(data_dict.values()), label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="2011年1-2月 每日銷售額")
)

bar.render("2011年1-2月 每日銷售額柱狀圖.html")