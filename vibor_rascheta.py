import streamlit as st
import pandas as pd
import numpy as np
import z_plenka as pl # Модуль расчета замеса пленки
from z_plenka import plenka
import z_bahili as pr # Модуль расчета бахил
from z_bahili import bahili
import z_individ # Модуль расчёта индивидуальной упаковки
from z_individ import individualka
import z_paket as pr # Модуль расчета пакетов
from z_paket import paketi
import z_perchatki as pr # Модуль расчета перчаток
from z_perchatki import perchatki
import z_dav_sirie as ds # Модуль расчета давальческое сырьё
from z_dav_sirie import daval_sir
import z_a_bahili # Модуль расчета выполнения заказа бахил
from z_a_bahili import zabahili
import z_a_plenka # Модуль расчета выполнения заказа пленки
from z_a_plenka import zaplenka
import z_a_paketi # Модуль расчета выполнения заказа пакеты
from z_a_paketi import zapaketi
import z_a_perchatki # Модуль расчета выполнения заказа перчатки
from z_a_perchatki import zaperchatki
import z_p_bahili # Модуль расчета зарплат бахил
from z_p_bahili import zpbahili
import z_p_ekstruziya # Модуль расчета зарплат пленки
from z_p_ekstruziya import zpekstruziya
import z_p_perchatki # Модуль расчета зарплат перчатки
from z_p_perchatki import zpperchatki
import z_p_paketi # Модуль расчета зарплат пакеты
from z_p_paketi import zppaketi



def products():

    b = st.sidebar.selectbox('ПРОДУКЦИЯ:', ['Выбрать/Очистить','Плёнка', 'Бахилы', 'Индивидуальная уп.', 'Пакеты', 'Перчатки', 'Дав. сырьё'])

    if b == 'Плёнка':
        b = plenka()

#------------------------

    elif b == 'Пакеты':
        b = paketi()
#------------------------

    elif b == 'Индивидуальная уп.':
        b = individualka()

#------------------------

    elif b == 'Бахилы':
        b = bahili()

#-------------------------

    elif b == 'Перчатки':
        b = perchatki()

#-------------------------

    elif b == 'Дав. сырьё':
        b = daval_sir()

#-------------------------

if __name__ == "__main__":
    products()

#-------------------------

def orders():

    y = st.sidebar.selectbox('РАСЧЁТ ЗАКАЗА:', ['Выбрать/Очистить','Заказ на бахилы','Заказ на пленку', 'Заказ на пакеты','Заказ на перчатки'])

    if y == 'Заказ на бахилы':
        y = zabahili()

#---------------------------

    elif y == 'Заказ на пленку':
        y = zaplenka()

    #---------------------------

    elif y == 'Заказ на пакеты':
        y = zapaketi()

#--------------------------

    elif y == 'Заказ на перчатки':
        y = zaperchatki()

if __name__ == "__main__":
    orders()

#--------------------------

def salarys():

    z = st.sidebar.selectbox('РАСЧЁТ ВЫПЛАТ:', ['Выбрать/Очистить','Цех бахил','Цех экструзии', 'Цех перчатки','Цех пакеты',])

    if z == 'Цех бахил':
        z = zpbahili()

#--------------------------

    if z == 'Цех экструзии':
        z = zpekstruziya()

#--------------------------

    elif z == 'Цех перчатки':
        z = zpperchatki()

#--------------------------

    elif z == 'Цех пакеты':
        z = zppaketi()

    #-------------------------
if __name__ == "__main__":
    salarys()
