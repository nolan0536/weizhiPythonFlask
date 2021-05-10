from pyecharts.charts import Pie,Line,Bar,Radar,Scatter,WordCloud,Grid
from pyecharts import options as opts

def create_pie(dataA,dataB):
    pie = Pie(
        init_opts=opts.InitOpts(width="100%",height="600px")
    )
    pie.add("",[list(z) for z in zip(dataA,dataB)],radius="66%",is_clockwise=True)
    pie.set_global_opts(
        title_opts=opts.TitleOpts(
            title="各password的kid所占比例",
            subtitle="(饼状图)",
            pos_left="center",
            title_textstyle_opts=opts.TextStyleOpts(
                color="#333",
                font_family="cursive",
                font_style="normal",
                font_weight="bold"
            )
        ),
        legend_opts=opts.LegendOpts(pos_left="right",pos_top="bottom",orient="vertical"),
        tooltip_opts=opts.TooltipOpts(
            trigger="item",
            formatter="{b} : {c}({d}%)"
        ),
        toolbox_opts=opts.ToolboxOpts(
            feature=opts.ToolBoxFeatureOpts(data_view=opts.ToolBoxFeatureDataViewOpts(is_show=True))
        )
    )
    pie.set_series_opts(
        label_opts=opts.LabelOpts(
            is_show=True,
            formatter="{b}({d}%)"
        )
    )
    return pie

def create_bar(x_data,y_data1,y_data2):
    bar = Bar(
        init_opts=opts.InitOpts(width="100%",height="600px")
    )
    bar.add_xaxis(xaxis_data=x_data)
    bar.add_yaxis(series_name="上限流量",y_axis=y_data1,stack="01",category_gap="")
    bar.add_yaxis(series_name="下限流量",y_axis=y_data2,stack="02",gap="")
    bar.set_global_opts(
        title_opts=opts.TitleOpts(
            title="每个编号的上限,下限流量",
            subtitle="(柱状图)",
            pos_left="center",
            title_textstyle_opts=opts.TextStyleOpts(
                color="purple",
                font_family="FangSong",
                font_style="italic",
                font_weight="normal"
            ),
            subtitle_textstyle_opts=opts.TextStyleOpts(
                color="#333"
            )
        ),
        legend_opts=opts.LegendOpts(pos_left="right",orient="vertical"),
        tooltip_opts=opts.TooltipOpts(
            trigger="axis",
            axis_pointer_type="shadow"
        ),
        xaxis_opts=opts.AxisOpts(
            name="编号",
            type_="category",
            axislabel_opts=opts.LabelOpts(
                color="red"
            )
        ),
        yaxis_opts=opts.AxisOpts(
            name="(MB)",
            type_="value",
            splitline_opts=opts.SplitLineOpts(
                is_show=True,linestyle_opts=opts.LineStyleOpts(opacity=1)
            )
        )
    )
    bar.set_series_opts(
        label_opts=opts.LabelOpts(
            is_show=True,
            color="white",
            font_weight="bolder",
            position="inside"
        )
    )
    return bar

def create_radar(dataA,dataB,dataC):
    radar = Radar(
        init_opts=opts.InitOpts(width="100%",height="600px")
    )
    DataB = [{"name":"est_cost","value":dataB}]
    DataC = [{"name":"actu_expent","value":dataC}]
    radar.add_schema(
        shape="",
        radius="67%",
        schema=[
            opts.RadarIndicatorItem(name=dataA[0],max_=3500),
            opts.RadarIndicatorItem(name=dataA[1],max_=7200),
            opts.RadarIndicatorItem(name=dataA[2],max_=5300),
            opts.RadarIndicatorItem(name=dataA[3],max_=2500),
            opts.RadarIndicatorItem(name=dataA[4],max_=16000),
            opts.RadarIndicatorItem(name=dataA[5],max_=12000),
            opts.RadarIndicatorItem(name=dataA[6],max_=3500)
        ],
        textstyle_opts=opts.TextStyleOpts(color="#333"),
        splitarea_opt=opts.SplitAreaOpts(
            is_show=True,areastyle_opts=opts.AreaStyleOpts(opacity=1)
        )
    )
    radar.add(series_name="est_cost",data=DataB,color="green")
    radar.add(series_name="actu_expent",data=DataC,color="purple")
    radar.set_global_opts(
        title_opts=opts.TitleOpts(
            title="各部门ect_cost VS actu_expent",
            subtitle="(雷达图)",
            pos_left="center"
        ),
        legend_opts=opts.LegendOpts(pos_bottom="bottom"),
        tooltip_opts=opts.TooltipOpts()
    )
    radar.set_series_opts(
        label_opts=opts.LabelOpts(
            is_show=False
        )
    )
    return radar

def create_scatter(x_data,y_data1):
    scatter = Scatter(
        init_opts=opts.InitOpts(width="100%",height="600px")
    )
    scatter.add_xaxis(xaxis_data=x_data)
    scatter.add_yaxis(series_name="norate",y_axis=y_data1,symbol_size=16)
    scatter.set_global_opts(
        title_opts=opts.TitleOpts(
            title="10省拒单率分布",
            subtitle="(散点图)",
            pos_left="center",
            title_textstyle_opts=opts.TextStyleOpts(
                color="#333",
                font_family="YouYuan",
                font_style="italic",
                font_weight="normal"
            ),
            subtitle_textstyle_opts=opts.TextStyleOpts(color="orange")
        ),
        legend_opts=opts.LegendOpts(pos_left="right"),
        tooltip_opts=opts.TooltipOpts(
            trigger="item",
            formatter="{c}"
        ),
        toolbox_opts=opts.ToolboxOpts(
            pos_left="center",
            pos_top="bottom",
            feature=opts.ToolBoxFeatureOpts(
                data_view=opts.ToolBoxFeatureDataViewOpts(is_show=True)
            )
        )
    )
    scatter.set_series_opts(
        label_opts=opts.LabelOpts(
            is_show=True,
            color="blue",
            position="left"
        )
    )
    return scatter

def create_line(x_data1,x_data2,y_data1,y_data2):
        line1 = Line()
        line1.add_xaxis(xaxis_data=x_data1)
        line1.add_yaxis(series_name="hotel",y_axis=y_data1,stack="01",is_smooth=False)
        line1.set_global_opts(
            title_opts=opts.TitleOpts(
                title="17地市的hotel数量",
                subtitle="(双折线)",
                pos_left="center",
                title_textstyle_opts=opts.TextStyleOpts(
                    color="purple",
                    font_weight="bolder",
                    font_style="normal"
                )
            ),
            legend_opts=opts.LegendOpts(pos_left="right"),
            tooltip_opts=opts.TooltipOpts(
                trigger="axis",
                axis_pointer_type="cross"
            ),
            xaxis_opts=opts.AxisOpts(
                name="城市",
                # type_="category",
                axislabel_opts=opts.LabelOpts(
                    color="red",
                    interval=0,
                    rotate=5
                )
            ),
            yaxis_opts=opts.AxisOpts(
                # type_="value",
                name="酒店数量",
                splitline_opts=opts.SplitLineOpts(
                    is_show=True,linestyle_opts=opts.LineStyleOpts(opacity=1)
                )
            )
        )

        line2 = Line()
        line2.add_xaxis(xaxis_data=x_data2)
        line2.add_yaxis(series_name="room",y_axis=y_data2)
        line2.set_global_opts(
            title_opts=opts.TitleOpts(
                title="16省份的room数量",
                pos_top="48%",
                pos_left="center"
            ),
            legend_opts=opts.LegendOpts(is_show=True,pos_right="right",pos_top="50%"),
            xaxis_opts=opts.AxisOpts(
                # type_="category",
                name="城市",
                axisline_opts=opts.AxisLineOpts(
                    is_show=True,linestyle_opts=opts.LineStyleOpts(color="blue")
                )
            ),
            yaxis_opts=opts.AxisOpts(
                # type_="value",
                name="房间数量",
                splitline_opts=opts.SplitLineOpts(is_show=False),
                axisline_opts=opts.AxisLineOpts(
                    is_show=True,linestyle_opts=opts.LineStyleOpts(color="blue")
                )
            )
        )

        grid = Grid(
            init_opts=opts.InitOpts(width="100%",height="620px")
        )
        grid.add(line1,grid_opts=opts.GridOpts(pos_bottom="55%"))
        grid.add(line2,grid_opts=opts.GridOpts(pos_top="55%"))
        return grid

def create_wordCloud(dataAA,dataBB):
    Data = [tuple(z) for z in zip(dataAA,dataBB)]
    wordCloud = WordCloud(
        init_opts=opts.InitOpts(width="100%",height="600px")
    )
    wordCloud.add("",Data,word_size_range=[12,60],rotate_step=45,shape="cricle",word_gap=1,emphasis_shadow_blur=10,emphasis_shadow_color="rgba(0,0,0,0.8)")
    wordCloud.set_global_opts(
        title_opts=opts.TitleOpts(
            title="词云图",
            pos_left="center",
            title_textstyle_opts=opts.TextStyleOpts(
                font_family="cursive"
            )
        ),
        legend_opts=opts.LegendOpts(is_show=True),
        tooltip_opts=opts.TooltipOpts(is_show=True)
    )
    return wordCloud