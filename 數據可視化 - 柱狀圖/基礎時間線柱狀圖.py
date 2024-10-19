from pyecharts.charts import Bar,Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType

# 在X軸上設置時間點
bar1 = Bar()
bar1.add_xaxis(["台灣","美國","英國"])
bar1.add_yaxis("GDP",[20,50,80],label_opts=LabelOpts(position="right"))  # 設置數值標籤在右側
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["台灣","美國","英國"])
bar2.add_yaxis("GDP",[10,70,40],label_opts=LabelOpts(position="right"))  # 設置數值標籤在右側
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["台灣","美國","英國"])
bar3.add_yaxis("GDP",[30,90,50],label_opts=LabelOpts(position="right"))  # 設置數值標籤在右側
bar3.reversal_axis()

# 構建時間線
timeline =Timeline({"theme": ThemeType.DARK})      # 主題設置
timeline.add(bar1,"點1")
timeline.add(bar2,"點2")
timeline.add(bar3,"點3")

# 自動播放
timeline.add_schema(
    play_interval=1000,      # 自動播放的時間間隔，單位毫秒
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)

# 繪圖是用時間線對象繪圖，而不是bar對象
timeline.render("基礎時間線繪製.html")