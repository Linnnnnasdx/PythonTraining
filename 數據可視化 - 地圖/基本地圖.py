from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map = Map()

data = [
    ("台北市",11),
    ("高雄市",110),
    ("新北市",2),
    ("宜兰县",55)
]

map.add("測試地圖",data, "台湾")

# 設置全局選項
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show = True,
        is_piecewise=True,  # 設定分段
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99", "color": "#FF6666"},
            {"min": 100, "max": 500, "label": "100-500", "color": "#990033"}
        ]
    )
)

map.render()