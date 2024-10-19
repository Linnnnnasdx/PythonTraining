import json
from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

with open(r"C:\Users\LEGION\Desktop\python學習教材\资料\第1-12章资料\资料\资料\可视化案例数据\动态柱状图数据\1960-2019全球GDP数据.csv",encoding="GB2312") as f:
    data_lines = f.readlines()

# 刪除第一條
data_lines.pop(0)
# 將數據轉換為字典存儲，格式為：
# { 年份: [ [國家, gdp], [國家,gdp], ......  ], 年份: [ [國家, gdp], [國家,gdp], ......  ], ...... }
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])
    country = (line.split(",")[1])
    gdp = float(line.split(",")[2])     # 科學符號可以藉由轉成'浮點數'就可以取到具體的數字
    # 判斷字典裡面有沒有指定的key
    try:
        data_dict[year].append([country,gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country,gdp])

# 創建時間軸對象
timeline = Timeline({"theme": ThemeType.LIGHT})

# 排序年份
# 先排key，讓年份按照1960~2019排序
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
    data_dict[year].sort(key = lambda element: element[1],reverse=True)     # 依照下標1的數值進行排序
    # 取出本年份前8名國家
    year_data = data_dict[year][0:8]
    x_data=[]
    y_data=[]
    for country_gdp in year_data:
        x_data.append(country_gdp[0])       # x軸添加國家
        y_data.append(country_gdp[1] / 100000000)       # y軸添加GDP
    # 構建柱狀圖
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data,)
    bar.add_yaxis("GDP(億)", y_data, label_opts=LabelOpts(position="right"))
    # 反轉X,Y軸
    bar.reversal_axis()
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前八GDP數據")
    )
    timeline.add(bar,str(year))


timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)

timeline.render("1960-2019年全球GDP前八國家.html")