from app.settings import session
from flask import Blueprint
from app.models import Possword_B,Iphone_De,Radar_Data,Table3_1,Table3_2
from jinja2 import Markup
from app.utils.Obtain_datas import Get_dataA,Get_dataB,Get_dataC,Get_dataD,Get_dataE,Get_dataF


index = Blueprint("index",__name__)

@index.route("/AAA")
def get_dataA():
    A_get = get_possword_b()
    c1 = Get_dataA(A_get)
    return Markup(c1.render_embed())

@index.route("/BBB")
def get_dataB():
    B_get = get_iphone()
    c2 = Get_dataB(B_get)
    return Markup(c2.render_embed())

@index.route("/CCC")
def get_dataC():
    C_get = get_radar_data()
    c3 = Get_dataC(C_get)
    return Markup(c3.render_embed())

@index.route("/DDD")
def get_dataD():
    D_get = get_table3_2()
    c4 = Get_dataD(D_get)
    return Markup(c4.render_embed())

@index.route("/EEE")
def get_dataE():
    E_get = get_table3_1()
    c5 = Get_dataE(E_get)
    return Markup(c5.render_embed())

@index.route("/FFF")
def get_dataF():
    F_get = get_iphone()
    c6 = Get_dataF(F_get)
    return Markup(c6.render_embed())

def get_iphone():
    tmp1 = session.query(Iphone_De).filter(Iphone_De.id%2 == 0).all()
    return tmp1

def get_radar_data():
    tmp2 = session.query(Radar_Data).all()
    return tmp2

def get_table3_1():
    tmp3 = session.query(Table3_1).all()
    return tmp3

def get_possword_b():
    tmp4 = session.query(Possword_B).all()
    return tmp4

def get_table3_2():
    tmp5 = session.query(Table3_2.province,Table3_2.norate).all()
    return tmp5