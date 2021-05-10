from pyecharts import options as opts
from pyecharts.charts import Pie
import pandas as pd

Data = pd.read_csv("E:/input/清晰图表数据(matplotlib)/雷达图+饼状图.csv",encoding="gbk")

x_data = Data["部门"]
y_data= Data["预计开销"]
print(type(y_data.tolist()))

pie = Pie(
    init_opts=opts.InitOpts(width="100%",height="680px")
)
pie.add("",[list(z) for z in zip(x_data.tolist(),y_data.tolist())],
        center=["50%","50%"],radius="50%")
pie.set_global_opts(
    title_opts=opts.TitleOpts(
        title="2020年各部门预计支出",
        subtitle="(饼状图)",
        pos_left="center",
        title_textstyle_opts=(opts.TextStyleOpts(
            color="#333",
            font_style="italic",
            font_weight="bold"
        )),
        subtitle_textstyle_opts=(opts.TextStyleOpts(
            color="#ccc"
        ))
    ),
    legend_opts=opts.LegendOpts(pos_left="left",pos_bottom="center",orient="interval"),
    tooltip_opts=opts.TooltipOpts(
        trigger="item",
        formatter="{b} : {c}({d}%)"
    ),
    toolbox_opts=opts.ToolboxOpts(
        feature=(
            opts.ToolBoxFeatureOpts(data_view=opts.ToolBoxFeatureDataViewOpts(is_show=True))
        )
    )
)
pie.set_series_opts(
    label_opts=opts.LabelOpts(
        font_size=16,
        formatter="{b}: {c}({d}%)"
    )
)
pie.render("饼状图(学习).html")