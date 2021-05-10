from pyecharts.charts import Radar
from pyecharts import options as opts
import pandas as pd

Data = pd.read_csv("E:/input/清晰图表数据(matplotlib)/雷达.csv",encoding="gbk")
value1 = Data["下限流量"]
value2 = Data["上限流量"]
data1 = [{"value":value1.tolist()}]
data2 = [{"value":value2.tolist()}]
print(data1)
# 雷达图数据格式 --> [ {value:[A,b,C...],name:"XXXX"} ]

print(type(data1))
c_schema = [
    {"name":"1月","max":10000},
    {"name":"2月","max":6000},
    {"name":"3月","max":3200},
    {"name":"4月","max":6800},
    {"name":"5月","max":999},
    {"name":"6月","max":9000}
]

radar = Radar(
    init_opts=opts.InitOpts(width="680px",height="600px")
)
radar.add_schema(
    # schema=c_schema,        #  ---》方式1
    schema=[
        opts.RadarIndicatorItem(name="1月(A)",max_=10000),       # ---》方式二
        opts.RadarIndicatorItem(name="2月(B)",max_=6000),
        opts.RadarIndicatorItem(name="3月(C)",max_=3200),
        opts.RadarIndicatorItem(name="4月(D)",max_=6800),
        opts.RadarIndicatorItem(name="5月(E)",max_=999),
        opts.RadarIndicatorItem(name="6月(F)",max_=9000)
    ],
    shape="",
    radius="80%",
    # 设置标签颜色
    textstyle_opts=opts.TextStyleOpts(color="#333"),
    # splitarea_opts分段设置区域颜色
    splitarea_opt=opts.SplitAreaOpts(
        is_show=True,areastyle_opts=opts.AreaStyleOpts(opacity=1)
    )
)
# linestyle_opts 设置线的颜色 | 弊端只设置图像上线的颜色而图例颜色不能一致
radar.add(series_name="上限流量",data=data1,linestyle_opts=opts.LineStyleOpts(color="blue"))
radar.add(series_name="下限流量",data=data2,color="yellow")
radar.set_global_opts(
    title_opts=opts.TitleOpts(
        title="1-6月份上限流量与下限流量",
        subtitle="(雷达图)",
        pos_left="left",
        title_textstyle_opts=opts.TextStyleOpts(
            color="#333",
            font_family="FangSong",
            font_style="italic",
            font_weight="bold"
        )
    ),
    legend_opts=opts.LegendOpts(pos_left="center"),
    tooltip_opts=opts.TooltipOpts()
)
radar.set_series_opts(
    # 是否显示线上的点
    label_opts=opts.LabelOpts(is_show=False)
)
radar.render("雷达图(学习).html")