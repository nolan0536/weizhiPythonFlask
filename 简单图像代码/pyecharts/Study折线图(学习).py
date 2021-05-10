from pyecharts.charts import Line
from pyecharts import options as opts


line = Line(
    init_opts=opts.InitOpts(width="680px",height="600px")
)
x=["衬衫","毛衣","T恤","休闲裤"]
y1=[163,128,90,118]
y2=[128,118,68,158]
line.add_xaxis(xaxis_data=x)
line.add_yaxis(series_name="A店铺",y_axis=y1,is_smooth=False,stack="01")
line.add_yaxis(series_name="B店铺",y_axis=y2,is_smooth=False,stack="02")
line.set_global_opts(
    title_opts=opts.TitleOpts(
        title="两家店铺衣服不同价格",
        subtitle="(折线图)",
        pos_left="center",
        title_textstyle_opts=(
            opts.TextStyleOpts(
                color="red",
                font_family="FangSong",
                font_style="italic",
                font_weight="bold"
            )
        ),
        subtitle_textstyle_opts=(opts.TextStyleOpts(color="#333"))
    ),
    legend_opts=opts.LegendOpts(pos_left="right",orient="interval"),
    tooltip_opts=opts.TooltipOpts(trigger="axis",axis_pointer_type="cross"),
    toolbox_opts=opts.ToolboxOpts(
        pos_left="right",
        pos_bottom="center",
        orient="interval",
        feature=opts.ToolBoxFeatureOpts(
            data_view=opts.ToolBoxFeatureDataViewOpts(is_show=True))
    ),
    xaxis_opts=opts.AxisOpts(
        name="类型",
        type_="category",
        is_scale=False,
        # False从y轴开始
        boundary_gap=True,
        axislabel_opts=(opts.LabelOpts(
            color="purple",
            interval=0,
            rotate=270
        )),
        splitline_opts=(opts.SplitLineOpts(
            is_show=False
        ))
    ),
    yaxis_opts=opts.AxisOpts(
        name="价格",
        type_="value",
        splitline_opts=(opts.SplitLineOpts(is_show=False))
    )
)
line.set_series_opts(
    label_opts=opts.LabelOpts(is_show=True,color="#ccc",position="top",font_size=18,formatter="")
)
line.render("折线图(学习).html")