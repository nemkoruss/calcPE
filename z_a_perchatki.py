import streamlit as st
import pandas as pd
import numpy as np

def zaperchatki():

    st.write('')
    st.title('ЗАЯВКА ПЕРЧАТКИ')
    st.write('')
    st.header('Расчёт выполнения заказа: ')
    col27, col28 = st.columns(2)
    with col27:
        aza111 = st.number_input('Введите кол-во задейственного оборудования: ')
        if aza111 == 2:
            aza111 = 2
        elif aza111 == 1:
            aza111 = 1
        elif aza111 == 0:
            aza111 = 1
        else:
            aza111 < 0
    with col27:
        bza111 = st.number_input('[С манжетой = 1, Обычные = 2]')
        if bza111 == 1:
            bza111 = 50000
        elif bza111 == 0:
            bza111 = 1
        else:
            bza111 < 0
        lza111 = aza111 * bza111
    with col28:
        cza111 = st.number_input('График: [где 12 часов = 1, а 24 часа = 2]: ')
        if cza111 == 1:
            cza111 = 1
        elif cza111 == 2:
            cza111 = 2
        elif cza111 == 0:
            cza111 = 1
        else:
            cza111 < 0
        kza111 = lza111 * cza111
    with col28:
        dza111 = st.number_input('Введите кол-во перчаток в парах: ')
        if dza111 == 0:
            dza111 = 1
        else:
            dza111 < 0
        sza111 = dza111 / kza111
        st.write('Для выполнения заказа нужно: ' + str(sza111) + ' день/дня/дней')

if __name__ == "__main__":
    zaperchatki()