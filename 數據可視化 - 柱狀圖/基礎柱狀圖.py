# 導入Bar基礎柱狀圖
from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

bar = Bar()
bar.add_xaxis(["台灣","美國","英國"])
bar.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(position="right"))  # 設置數值標籤在右側

# 反轉x軸跟y軸
bar.reversal_axis()

bar.render("基礎柱狀圖.html")