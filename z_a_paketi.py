import streamlit as st
import pandas as pd
import numpy as np

def zapaketi():
    st.write('')
    st.title('ЗАЯВКА ПАКЕТЫ')
    st.write('')
    st.header('Расчёт выполнения заказа: ')
    col25, col26 = st.columns(2)
    with col25:
        aza11 = st.number_input('Введите кол-во задейственного оборудования: ')
        if aza11 == 2:
            aza11 = 2
        elif aza11 == 1:
            aza11 = 1
        elif aza11 == 0:
            aza11 = 1
        else:
            aza11 < 0
    with col25:
        bza11 = st.number_input('[Толстая плёнка = 1, Тонкая плёнка = 2, Флекс-печать = 3]')
        if bza11 == 1:
            bza11 = 2000
        elif bza11 == 2:
            bza11 = 4000
        elif bza11 == 3:
            bza11 = 3000
        elif bza11 == 0:
            bza11 = 1
        else:
            bza11 < 0
        lza11 = aza11 * bza11
    with col26:
        cza11 = st.number_input('График: [где 12 часов = 1, а 24 часа = 2]: ')
        if cza11 == 1:
            cza11 = 1
        elif cza11 == 2:
            cza11 = 2
        elif cza11 == 0:
            cza11 = 1
        else:
            cza11 < 0
        kza11 = lza11 * cza11
    with col26:
        dza11 = st.number_input('Введите кол-во пакетов в штуках: ')
        if dza11 == 0:
            dza11 = 1
        else:
            dza11 < 0
        sza11 = dza11 / kza11
        sza11 = float('{:.3f}'.format(sza11))
        st.write('Для выполнения заказа нужно: ' + str(sza11) + ' день/дня/дней')

if __name__ == "__main__":
    zapaketi()