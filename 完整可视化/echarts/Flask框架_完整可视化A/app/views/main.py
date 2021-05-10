from app.extensions import db
from app.models import RestaurantNum,CityRestaurantNum,RestaurantScoreNum,CitySaleVol,RestaurantTypeCount,CitySaleApri
from sqlalchemy import *
from flask import Blueprint,render_template
import json


index = Blueprint('index', __name__)  # 实例化路由

@index.route("/")  # 路由名称与函数名称不能一致
def main():
    return "No problem!"


@index.route("/index/")
def Get_data():
    g_crn = Crn_get()
    g_rsn = Rsn_get()
    g_cr = Get_csv_rn()
    g_rtc = Rtc_get()
    g_csa = Csa_get()
    g_cy = Rtc_cy()
    return render_template("/main/echarts.html",g_crn=g_crn,g_rsn=g_rsn,g_cr=g_cr,g_rtc=json.dumps(g_rtc,ensure_ascii=False),g_csa=g_csa,g_cy=g_cy)
    # return render_template("/main/echarts.html", g_rsn=g_rsn)


def Get_csv_rn():
    g_csv = db.session.query(CitySaleVol.city,func.sum(CitySaleVol.sales_vol_month).label("sale_n")).group_by(CitySaleVol.city)
    g_rn = db.session.query(RestaurantNum.city,func.sum(RestaurantNum.number).label("restaurant_n")).group_by(RestaurantNum.city)
    g_csv_rn = [g_csv,g_rn]
    return g_csv_rn

def Rsn_get():
    rsn_get = RestaurantScoreNum.query.all()
    return rsn_get

def Crn_get():
    crn_get = CityRestaurantNum.query.order_by(asc("restaurant_numb")).all()
    return crn_get

def rtc_seal_package(data):
    Dictionary_d = {}
    List_d = []
    for r in data:
        List_d.append(int(r.number))
        Dictionary_d["value"] = List_d
        Dictionary_d["name"] = r.city
    return Dictionary_d

def Rtc_get():
    rtc_wf = db.session.query(RestaurantTypeCount).filter(
        RestaurantTypeCount.city == "潍坊",RestaurantTypeCount.foodtype.in_(["东北菜","云贵菜","京菜鲁菜","川湘菜","江浙菜"])).all()
    rtc_lc = db.session.query(RestaurantTypeCount).filter(
        RestaurantTypeCount.city == "聊城",RestaurantTypeCount.foodtype.in_(["东北菜","云贵菜","京菜鲁菜","川湘菜","江浙菜"])).all()
    rtc_qd = db.session.query(RestaurantTypeCount).filter(
        RestaurantTypeCount.city == "青岛",RestaurantTypeCount.foodtype.in_(["东北菜","云贵菜","京菜鲁菜","川湘菜","江浙菜"])).all()
    rtc_zz = db.session.query(RestaurantTypeCount).filter(
        RestaurantTypeCount.city == "枣庄",RestaurantTypeCount.foodtype.in_(["东北菜","云贵菜","京菜鲁菜","川湘菜","江浙菜"])).all()
    rtc_dy = db.session.query(RestaurantTypeCount).filter(
        RestaurantTypeCount.city == "东营",RestaurantTypeCount.foodtype.in_(["东北菜","云贵菜","京菜鲁菜","川湘菜","江浙菜"])).all()
    rtc_list = [rtc_wf,rtc_lc,rtc_qd,rtc_zz,rtc_dy]
    rtc_data = []       # rtc_data = [{value:[],name:""}]
    for data in rtc_list:
        result = rtc_seal_package(data)
        rtc_data.append(result)
    print(rtc_data)
    return rtc_data

def Csa_get():
    csa_g = db.session.query(CitySaleApri.city,func.sum(CitySaleApri.sales_month).label("Sum_sales")).group_by(CitySaleApri.city)
    return csa_g

def Rtc_cy():
    rtc_cy = db.session.query(RestaurantTypeCount.foodtype,func.sum(RestaurantTypeCount.number).label("Sum_number")).group_by(RestaurantTypeCount.foodtype)
    return rtc_cy