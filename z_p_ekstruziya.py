import streamlit as st
import pandas as pd
import numpy as np

def zpekstruziya():

    st.write('')
    st.title('ЗП ЭКСТРУЗИЯ')
    st.write('')
    st.header('Ставка: ')
    col330, col340 = st.columns(2)
    with col330:
        za1 = st.number_input('Стоимость "12 часов Смена": ')
        if za1 == 0:
            za1 = 1
        else:
            za1 < 0
    with col340:
        zb1 = st.number_input('Стоимость "24 часа смена": ')
        if zb1 == 0:
            zb1 = 1
        else:
            zb1 < 0
        ze1 = za1 * 600
        zf1 = zb1 * 1200

    st.header('Сделано (указать кол-во кг): ')
    col350, col360 = st.columns(2)
    with col350:
        wa1 = st.number_input('Кол-во "за 12 часов": ')
    with col360:
        wb1 = st.number_input('Кол-во "за 24 часа": ')

    st.header('Отгрузили (указать кол-во кг): ')
    col370, col380 = st.columns(2)
    with col370:
        ya1 = st.number_input('Кол-во "за 12 часоа": ')
    with col380:
        yb1 = st.number_input('Кoл-во "за 24 часа": ')

        xa1 = wa1 - ya1
        xb1 = wb1 - yb1

        ua1 = ze1 * wa1
        ub1 = zf1 * wb1

        va1 = ze1 * ya1
        vb1 = zf1 * yb1

        ta1 = ze1 * xa1
        tb1 = zf1 * xb1
    with col370:
        st.write('')
        st.write('')
        st.subheader('12 часов: ')
        st.write('Сделано: '  + str(wa1) + ' кор., ' + 'Сумма ЗП: ' + str(ua1) + ' руб.')
        st.write('Отгрузили: '  + str(ya1) + ' кор., ' + 'Оплата: ' + str(va1) + ' руб.')
        st.write('Склад: '  + str(xa1) + ' кор., ' + 'Долг: ' + str(ta1) + ' руб.')

        st.write('')
        st.write('')

        st.subheader('24 часа: ')
        st.write('Сделано: '  + str(wb1) + ' кор., ' + 'Сумма ЗП: ' + str(ub1) + ' руб.')
        st.write('Отгрузили: '  + str(yb1) + ' кор., ' + 'Оплата: ' + str(vb1) + ' руб.')
        st.write('Склад: '  + str(xb1) + ' кор., ' + 'Долг: ' + str(tb1) + ' руб.')

if __name__ == "__main__":
    zpekstruziya()