import streamlit as st
import pandas as pd
import numpy as np


def zaplenka():

    st.write('')
    st.title('ЗАЯВКА ПЛЕНКА')
    st.write('')
    st.header('Расчёт выполнения заказа: ')
    col23, col24 = st.columns(2)
    with col23:
        aza1 = st.number_input('Введите кол-во задейственного оборудования: ')
        if aza1 == 2:
            aza1 = 2
        elif aza1 == 1:
            aza1 = 1
        elif aza1 == 0:
            aza1 = 1
        else:
            aza1 < 0
    with col23:
        zza1 = st.number_input('[Рукав = 1, Полотно = 2]')
        if zza1 == 2:
            zza1 = 4
        elif zza1 == 1:
            zza1 =  1
        elif zza1 == 0:
            zza1 = 1
        else:
            zza1 <0
        wza1 = aza1 * zza1
    with col23:
        bza1 = st.number_input('[7 - 10 мкм = 1, 10 - 15 мкм = 2, 16 - 21 мкм = 3]')
        if bza1 == 1:
            bza1 = 300
        elif bza1 == 2:
            bza1 = 200
        elif bza1 == 3:
            bza1 = 100
        elif bza1 == 0:
            bza1 = 1
        else:
            bza1 < 0
        lza1 = wza1 * bza1
    with col24:
        cza1 = st.number_input('График: [где 12 часов = 1, а 24 часа = 2]: ')
        if cza1 == 1:
            cza1 = 1
        elif cza1 == 2:
            cza1 = 2
        elif cza1 == 0:
            cza1 = 1
        else:
            cza1 < 0
        kza1 = lza1 * cza1
    with col24:
        dza1 = st.number_input('Введите кол-во плёнки в кг: ')
        if dza1 == 0:
            dza1 = 1
        else:
            dza1 < 0
        sza1 = dza1 / kza1
        sza1 = float('{:.3f}'.format(sza1))
    st.write('')
    st.write('Для выполнения заказа нужно: ' + str(sza1) + ' день/дня/дней')

if __name__ == "__main__":
    zaplenka()