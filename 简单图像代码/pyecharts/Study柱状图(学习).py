from pyecharts.charts import Bar
from pyecharts import options as opts

bar = Bar(
    init_opts=opts.InitOpts(width="680px",height="600px")
)
x_data = ["雪碧","可乐","橙汁","牛奶","咖啡","奶茶"]
y_data1 = [3,2.5,6,4,18,8]
y_data2 = [3.5,3,4.5,3,10,7]

bar.add_xaxis(xaxis_data=x_data,)
bar.add_yaxis(y_axis=y_data1,stack="01",category_gap="",series_name="A超市")
# category_gap 同一系列的柱间距离 gap 不用系列的柱间距离
bar.add_yaxis(series_name="B超市",y_axis=y_data2,stack="02",gap="")
bar.set_global_opts(
    title_opts=opts.TitleOpts(
        title="A,B两超市饮品价格",
        subtitle="(柱状图)",
        pos_left="center",
        title_textstyle_opts=(
            opts.TextStyleOpts(
                color="#333",
                font_family="YouYuan",
                font_style="italic",
                font_weight="bold"
            )
        ),
        subtitle_textstyle_opts=(opts.TextStyleOpts(color="purple"))
    ),
    legend_opts=opts.LegendOpts(pos_bottom="bottom"), # orient="interval"
    tooltip_opts=opts.TooltipOpts(
        trigger="axis",
        axis_pointer_type="shadow"
    ),
    toolbox_opts=opts.ToolboxOpts(
        feature=(
            opts.ToolBoxFeatureOpts(data_view=opts.ToolBoxFeatureDataViewOpts(is_show=True))
        )
    ),
    # # 图像缩进
    # datazoom_opts=opts.DataZoomOpts(is_show=True),
    xaxis_opts=opts.AxisOpts(
        name="种类",
        type_="category",
        axislabel_opts=opts.LabelOpts(
            color="#333",
            interval=0,
            rotate=0
        ),
        splitline_opts=opts.SplitLineOpts(is_show=False)
    ),
    yaxis_opts=opts.AxisOpts(
        name="价格(元)",
        type_="value"
    )
)
bar.set_series_opts(
    label_opts=opts.LabelOpts(is_show=True,position="inside",formatter="")
)
bar.render("柱状图(学习).html")