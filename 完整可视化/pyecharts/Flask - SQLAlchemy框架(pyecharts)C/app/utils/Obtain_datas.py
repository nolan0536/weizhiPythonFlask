from .Obtain_image import create_pie,create_bar,create_radar,create_scatter,create_line,create_wordCloud

def Get_dataA(datas1):

    data1 = []
    data2 = []
    for r1 in datas1:
        data1.append(r1.password)
        data2.append(r1.kid)

    return create_pie(data1,data2)

def Get_dataB(datas2):
    x_data = []
    y_data1 = []
    y_data2 = []
    for r2 in datas2:
        x_data.append(r2.编号)
        y_data1.append(r2.上限流量)
        y_data2.append(r2.下限流量)

    print(x_data)
    return create_bar(x_data,y_data1,y_data2)

def Get_dataC(data3):
    dataA = []
    dataB = []
    dataC = []
    for r3 in data3:
        dataA.append(r3.section)
        dataB.append(r3.est_cost)
        dataC.append(r3.actu_expent)

    return create_radar(dataA,dataB,dataC)

def Get_dataD(data4):
    data_a = []
    data_b = []
    for r4 in data4:
        data_a.append(r4.province)
        data_b.append(r4.norate)
    return create_scatter(data_a,data_b)

def Get_dataE(data5):
    x_data1 = []
    x_data2 = []
    y_data1 = []
    y_data2 = []
    for r5 in data5:
        x_data1.append(r5.city)
        x_data2.append(r5.province)
        y_data1.append(r5.hotel_num)
        y_data2.append(r5.room_num)
    return create_line(x_data1=x_data1,x_data2=x_data2,y_data1=y_data1,y_data2=y_data2)

def Get_dataF(data6):
    dataAA = []
    dataBB = []
    for r6 in data6:
        dataAA.append(r6.编号)
        dataBB.append(r6.上限流量)
    # tuple() 函数可将列表转换为元组
    Data = [tuple(z) for z in zip(dataBB,dataAA)]
    print(Data)
    return create_wordCloud(dataAA,dataBB)