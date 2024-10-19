"""
演示第三个图表：GDP动态柱状图开发
"""
from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts, TitleOpts, TimelineCheckPointerStyle
from pyecharts.globals import ThemeType

# ----------------------------1.获取数据------------------------
# 读取数据
f = open(r"C:\Users\LEGION\Desktop\python學習教材\资料\第1-12章资料\资料\资料\可视化案例数据\动态柱状图数据\1960-2019全球GDP数据.csv", encoding="GB2312")
data_lines = f.readlines()  # 按行读取每一行数据
# 关闭文件
f.close()
# 删除第一行数据
data_lines = data_lines[1:]  # 或    data_lines.pop(0)
# print(data_lines)  # 中途测试代码

# -----------------------------2.处理数据------------------------
# 每行数据都是字符串，很难处理。 故将数据转换成字典存储，格式为：
# { 年份: [ [国家, gdp], [国家,gdp], ......  ], 年份: [ [国家, gdp], [国家,gdp], ......  ], ...... }
# 按照这样的格式便于处理，按照年份作为时间线，国家和gdp为一个条形图中一个柱的两个参数

# 2.1 先定义一个字典对象，获取数据
data_dict = {}
# 2.2 把数据整理好并放入字典中
for line in data_lines:
    line.strip()  # 去掉换行符
    year = int(line.split(",")[0])  # 年份
    country = line.split(",")[1]  # 国家
    gdp = float(line.split(",")[2])  # gdp数据
    #  在给字典添加每一个元素的键值对中的值时，需判断这个值[国家, gdp]是否是这一年中所加的第一个数据。
    #  如果是第一个，那么说明还没有加入对应的键值对的关键字(即年份)
    #  --> 如何判断字典里面有没有指定的key呢？
    try:
        data_dict[year].append([country, gdp])  # 年份不存在，在关键字year下继续添加[country, gdp]
    except KeyError:
        data_dict[year] = []  # 年份不存在，加入新的键值对
        data_dict[year].append([country, gdp])

# print(data_dict)  # 中途测试代码
# -----------------------------3.绘图------------------------
# 3.1 排序年份   (字典是靠键值对的关键字查询数据的，没有顺序)
sorted_year_list = sorted(data_dict.keys())
# print(sorted_year_list)  # 中途测试代码

# 3.2 取出每年gdp前8的国家,然后构建每一年的柱状图，并按时间线设置好对应的柱状图
# 创建时间线对象,并设置主题
timeline = Timeline({"theme": ThemeType.LIGHT})

for year in sorted_year_list:
    # 将每一年的各个国家的gdp按照从大到小顺序进行排序
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    # 取出本年份前8的国家
    year_data = data_dict[year][:8]
    x_data = []  # 用来存放当年x轴数据
    y_data = []  # 用来存放当年y轴数据
    for country_gdp in year_data:
        x_data.append(country_gdp[0])  # 获取当年gdp第country_gdp名的国家
        y_data.append(country_gdp[1] / 1e8)  # 获取当年gdp第country_gdp名的gdp,单位(亿)

    # 构建柱状图
    bar = Bar()
    x_data.reverse()  # 反转数据，将前8按照gdp从小到大的顺序进行排序 --> 柱状图的图形的从上到下，依次是gdp从大到小的国家
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data,
                  label_opts=LabelOpts(position="right")  # 标签靠右
                  )
    # 反转X轴和y轴
    bar.reversal_axis()
    # 设置每一年的图表的标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前8GDP数据")
    )

    # 在时间线内添加柱状图对象
    timeline.add(bar, str(year))

# 3.3 设置时间线自动播放
timeline.add_schema(
    play_interval=300,  # 自动播放的时间阿隔，单位毫砂
    is_timeline_show=True,  # 是否在自动播放的时候，显示时间线
    is_auto_play=True,  # 是否自动播放
    is_loop_play=False,  # 是否循环自动播放
    label_opts=LabelOpts(is_show=True,color="#4169E1")
)

# 3.4 绘图
timeline.render("test.html")