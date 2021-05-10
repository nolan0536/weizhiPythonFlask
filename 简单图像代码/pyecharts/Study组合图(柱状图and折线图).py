from pyecharts.charts import Bar,Line,Grid
from pyecharts import options as opts

X_data = ["{}月".format(i) for i in range(1,13)]
Y_data1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
Y_data2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
Y_data3 = [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]

bar = Bar(
    init_opts=opts.InitOpts(width="100%",height="610px")
)
bar.add_xaxis(xaxis_data=X_data)
bar.add_yaxis(series_name="蒸发量",y_axis=Y_data1,stack="01",color="#d14a61",yaxis_index=0)
bar.add_yaxis(series_name="降水量",y_axis=Y_data2,stack="02",color="#5793f3",gap="",yaxis_index=1)
bar.extend_axis(
    yaxis=opts.AxisOpts(
        name="蒸发量",
        type_="value",
        min_=0,
        max_=250,
        interval=50,
        # 设置坐标轴在图像右侧
        position="right",
        axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(color="#d14a61")
        ),
        axislabel_opts=opts.LabelOpts(formatter="{value} ml")
    )
)
bar.extend_axis(
    yaxis=opts.AxisOpts(
        name="温度",
        type_="value",
        min_=0,
        max_=25,
        interval=5,
        position="left",
        axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(color="#675bba")
        ),
        axislabel_opts=opts.LabelOpts(formatter="{value} ℃"),
        splitline_opts=opts.SplitLineOpts(
            is_show=True,linestyle_opts=opts.LineStyleOpts(opacity=1)
        )
    )
)
bar.set_global_opts(
    title_opts=opts.TitleOpts(
        title="2020年降雨量,蒸发量,平均温度",
        subtitle="(折线 + 柱状图)",
        pos_left="center",
        title_textstyle_opts=opts.TextStyleOpts(
            color="#333",
            font_family="YouYuan"
        ),
        subtitle_textstyle_opts=opts.TextStyleOpts(color="purple")
    ),
    legend_opts=opts.LegendOpts(is_show=True,pos_bottom="bottom"),
    tooltip_opts=opts.TooltipOpts(
        trigger="axis",
        axis_pointer_type="cross"
    ),
    yaxis_opts=opts.AxisOpts(
        name="降水量",
        min_=0,
        max_=250,
        interval=50,
        position="right",
        # 纵轴距图像右轴距离
        offset=80,
        axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(color="#5793f3")
        ),
        axislabel_opts=opts.LabelOpts(formatter="{value} ml")
    )
)

line = Line()
line.add_xaxis(xaxis_data=X_data)
line.add_yaxis(series_name="平均温度",y_axis=Y_data3,color="#675bba",yaxis_index=2)

# 图像重叠
bar.overlap(line)
grid = Grid()
# is_control_axis_index 是否存在控制轴线索引
grid.add(bar,opts.GridOpts(pos_left="10%",pos_right="20%"),is_control_axis_index=True)
grid.render("组合图(学习).html")