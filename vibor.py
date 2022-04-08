import streamlit as st
import pandas as pd
import numpy as np
import plenka as pl # Модуль расчета замеса пленки
from plenka import plastik
import bahili as pr # Модуль расчета бахил
from bahili import bahili
import paket as pr # Модуль расчета пакетов
from paket import paketi
import perchatki as pr # Модуль расчета перчаток
from perchatki import perchatki
import zakaz # Модуль расчета выполнения заказа
from zakaz import zabahili, zaplenka, zapaketi, zaperchatki
import viplati # Модуль расчета зарплат
from viplati import zpbahili, zpekstruziya, zpperchatki, zppaketi

def products():

    b = st.sidebar.selectbox('ПРОДУКЦИЯ:', ['Выбрать/Очистить','Плёнка', 'Бахилы', 'Пакеты', 'Перчатки'])

    if b == 'Плёнка':
        b = plastik()

#------------------------

    elif b == 'Пакеты':
        b = paketi()

#------------------------

    elif b == 'Бахилы':
        b = bahili()

#-------------------------

    elif b == 'Перчатки':
        b = perchatki()

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
