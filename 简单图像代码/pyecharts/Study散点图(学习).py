from pyecharts.charts import Scatter,EffectScatter,Grid
from pyecharts import options as opts

# x有多少数据对应的y就用多少数据(y数据再多也只能显示与x相同的数据)
x_data = ["小米","华为","三星","苹果","诺基亚"]
y_data1 = [166.8, 56.6,172.7, 105.2,163.5, 51.8,169.4, 63.4,167.8, 59.0,159.5, 47.6,167.6, 63.0,161.2, 55.2,
              160.0, 45.0,163.2, 54.0,162.2, 50.2,161.3, 60.2,149.5, 44.8,157.5, 58.8,163.2, 56.4]
y_data2 = [110.9,127.8,21.3,131.5,27.1]
scatter = Scatter(
    # init_opts= opts.InitOpts(width="680px",height="600px")
)
scatter.add_xaxis(xaxis_data=x_data)
scatter.add_yaxis(y_axis=y_data1,symbol_size=16,series_name="正常")
scatter.add_yaxis(y_axis=y_data2,symbol_size=20,series_name="异常")
scatter.set_global_opts(
    title_opts=opts.TitleOpts(
        title="数据分布",
        subtitle="(散点图)",
        pos_left="left",
        title_textstyle_opts=opts.TextStyleOpts(
            color="blue",
            font_weight="bold"
        ),
        subtitle_textstyle_opts=opts.TextStyleOpts(color="#333",font_family="FangSong")
    ),
    legend_opts=opts.LegendOpts(orient="italic"),
    tooltip_opts=opts.TooltipOpts(
        trigger="item",
        formatter="{b}: ({c})"
    ),
    # toolbox_opts=opts.ToolboxOpts(
    #     feature=opts.ToolBoxFeatureOpts(data_view=opts.ToolBoxFeatureDataViewOpts(is_show=True))
    # ),
    xaxis_opts=opts.AxisOpts(
        name="xxx",
        type_="category",
        axislabel_opts=opts.LabelOpts(
            color="red",
            interval=0,
            rotate=10
        ),
        splitline_opts=opts.SplitLineOpts(is_show=True),
        is_scale=True
    ),
    yaxis_opts=opts.AxisOpts(
        name="yyy",
        type_="value",
        splitline_opts=opts.SplitLineOpts(is_show=True),
        is_scale=True
    )
)
scatter.set_series_opts(
    label_opts=opts.LabelOpts(
        color="blue",
        position="left",
        font_size=16
    )
)

effectScatter = EffectScatter()
effectScatter.add_xaxis(xaxis_data=x_data)
effectScatter.add_yaxis(y_axis=y_data1,symbol_size=20,series_name="效果散点")
effectScatter.set_global_opts(
    title_opts=opts.TitleOpts(
        title="效果散点",
        subtitle="(效果散点图)",
        pos_left="70%"
    ),
    legend_opts=opts.LegendOpts(pos_left="80%"),
    tooltip_opts=opts.TooltipOpts(
        trigger="item",
        formatter="{c}",
    ),
    toolbox_opts=opts.ToolboxOpts(
        feature=opts.ToolBoxFeatureOpts(data_view=opts.ToolBoxFeatureDataViewOpts(is_show=False))
    ),
    xaxis_opts=opts.AxisOpts(
        name="XXX",
        type_="category",
        # axispointer_opts=opts.AxisPointerOpts(type_="cross"),
        splitline_opts=opts.SplitLineOpts(is_show=True)
    ),
    yaxis_opts=opts.AxisOpts(
        name="YYY",
        type_="value",
        splitline_opts=opts.SplitLineOpts(is_show=True)
    ),
)
effectScatter.set_series_opts(
    label_opts=opts.LabelOpts(
        is_show=True,
        color="#333",
        position="right",
        font_size=16
    ),
    effect_opts=opts.EffectOpts(
        is_show=True
    )
)

# 两图放同一页面
grid = Grid()
grid.add(scatter,grid_opts=opts.GridOpts(pos_right="60%"))
grid.add(effectScatter,grid_opts=opts.GridOpts(pos_left="60%"))

grid.render("散点图(学习).html")