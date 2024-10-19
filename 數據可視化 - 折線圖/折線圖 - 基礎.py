from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts

Line = Line()
Line.add_xaxis(["台灣","美國","英國"])
Line.add_yaxis("GDP",[30,20,10])

Line.set_global_opts(
    title_opts=TitleOpts(title = "GDP展示",pos_left="center",pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)

Line.render()