from pyecharts.charts import WordCloud
from pyecharts import options as opts

Data = [
    ("Sam S Club", 10000),
    ("Macys", 6181),
    ("Amy Schumer", 4386),
    ("Jurassic World", 4055),
    ("Charter Communications", 2467),
    ("Chick Fil A", 2244),
    ("Planet Fitness", 1868),
    ("Pitch Perfect", 1484),
    ("Express", 1112),
    ("Home", 865),
    ("Johnny Depp", 847),
    ("Lena Dunham", 582),
    ("Lewis Hamilton", 555),
    ("KXAN", 550),
    ("Mary Ellen Mark", 462),
    ("Farrah Abraham", 366),
    ("Rita Ora", 360),
    ("Serena Williams", 282),
    ("NCAA baseball tournament", 273),
    ("Point Break", 265),
    ("城都AG_MVP",3689)
]

wordCloud = WordCloud(
    init_opts=opts.InitOpts(width="100%",height="600px")
)
wordCloud.add("",Data,word_size_range=[12,60],textstyle_opts=opts.TextStyleOpts(font_family="FangSong",font_weight="bold"))
wordCloud.set_global_opts(
    title_opts=opts.TitleOpts(
        title="热点词汇",
        subtitle="(词云图)",
        pos_left="center",
        title_textstyle_opts=opts.TextStyleOpts(
            color="#333",
            font_family="cursive",
            font_style="italic",
            font_weight="bold"
        )
    ),
    legend_opts=opts.LegendOpts(),
    tooltip_opts=opts.TooltipOpts(is_show=True),
    toolbox_opts=opts.ToolboxOpts(
        feature=opts.ToolBoxFeatureOpts(data_view=opts.ToolBoxFeatureDataViewOpts(is_show=False))
    )
)
wordCloud.render("词云图(学习).html")