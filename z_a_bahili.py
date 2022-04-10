import streamlit as st
import pandas as pd
import numpy as np


def zabahili():

    st.write('')
    st.title('ЗАЯВКА БАХИЛЫ')
    st.write('')
    st.header('Расчёт выполнения заказа: ')
    col21, col22 = st.columns(2)
    with col21:
        aza = st.number_input('Введите кол-во задейственного оборудования: ')
        if aza == 5:
            aza = 5
        elif aza == 4:
            aza = 4
        elif aza == 3:
            aza = 3
        elif aza == 2:
            aza = 2
        elif aza == 1:
            aza = 1
        elif aza == 0:
            aza = 1
        else:
            aza < 0
    with col21:
        bza = st.number_input('[Эконом = 1, Стандарт = 2, Прочные = 3, Детские = 4]')
        if bza == 1:
            bza = 40000
        elif bza == 2:
            bza = 35000
        elif bza == 3:
            bza = 30000
        elif bza == 4:
            bza = 10000
        elif bza == 0:
            bza = 1
        else:
            bza < 0
        lza = aza * bza
    with col22:
        cza = st.number_input('График: [где 12 часов = 1, а 24 часа = 2]: ')
        if cza == 1:
            cza = 1
        elif cza == 2:
            cza = 2
        elif cza == 0:
            cza = 1
        else:
            cza < 0
        kza = lza * cza
    with col22:
        dza = st.number_input('Введите кол-во бахил в парах: ')
        if dza == 0:
            dza = 1
        else:
            dza < 0
        sza = dza / kza
        sza = float('{:.3f}'.format(sza))
        st.write('Для выполнения заказа нужно: ' + str(sza) + ' день/дня/дней')

if __name__ == "__main__":
    zabahili()