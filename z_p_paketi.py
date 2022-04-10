import streamlit as st
import pandas as pd
import numpy as np

def zppaketi():
    st.write('')
    st.title('ЗП ПАКЕТЫ')
    st.write('')
    st.header('Ставка: ')
    col530, col540 = st.columns(2)
    with col530:
        za111 = st.number_input('Стоимость "4 ручья" за штуку: ')
        if za111 == 0:
            za111 = 1
        else:
            za111 < 0
    with col530:
        zb111 = st.number_input('Стоимость "2 ручья" за штуку: ')
        if zb111 == 0:
            zb111 = 1
        else:
            zb111 < 0
    with col540:
        zc111 = st.number_input('Стоимость "1 ручей" за штуку: ')
        if zc111 == 0:
            zc111 = 1
        else:
            zc111 < 0

        ze111 = za111 * 4000
        zf111 = zb111 * 3500
        zg111 = zc111 * 2000

    st.header('Сделано (указать кол-во коробок): ')
    col550, col560 = st.columns(2)
    with col550:
        wa111 = st.number_input('Кол-во "4 ручья": ')
        wb111 = st.number_input('Кол-во "2 ручья": ')
    with col560:
        wc111 = st.number_input('Кол-во "1 ручей": ')

    st.header('Отгрузили (указать кол-во коробок): ')
    col570, col580 = st.columns(2)
    with col570:
        ya111 = st.number_input('Кол-во "4 pучья": ')
        yb111 = st.number_input('Кoл-во "2 pучья": ')
    with col580:
        yc111 = st.number_input('Кол-вo "1 pучей": ')

        xa111 = wa111 - ya111
        xb111 = wb111 - yb111
        xc111 = wc111 - yc111

        ua111 = ze111 * wa111
        ub111 = zf111 * wb111
        uc111 = zg111 * wc111

        va111 = ze111 * ya111
        vb111 = zf111 * yb111
        vc111 = zg111 * yc111

        ta111 = ze111 * xa111
        tb111 = zf111 * xb111
        tc111 = zg111 * xc111

    with col570:

        st.write('')
        st.write('')

        st.subheader('4 ручья: ')
        wa111 = float('{:.3f}'.format(wa111))
        ua111 = float('{:.3f}'.format(ua111))
        ya111 = float('{:.3f}'.format(ya111))
        va111 = float('{:.3f}'.format(va111))
        xa111 = float('{:.3f}'.format(xa111))
        ta111 = float('{:.3f}'.format(ta111))
        st.write('Сделано: '  + str(wa111) + ' кор., ' + 'Сумма ЗП: ' + str(ua111) + ' руб.')
        st.write('Отгрузили: '  + str(ya111) + ' кор., ' + 'Оплата: ' + str(va111) + ' руб.')
        st.write('Склад: '  + str(xa111) + ' кор., ' + 'Долг: ' + str(ta111) + ' руб.')

        st.write('')
        st.write('')

        st.subheader('2 ручья: ')
        wb111 = float('{:.3f}'.format(wb111))
        ub111 = float('{:.3f}'.format(ub111))
        yb111 = float('{:.3f}'.format(yb111))
        vb111 = float('{:.3f}'.format(vb111))
        xb111 = float('{:.3f}'.format(xb111))
        tb111 = float('{:.3f}'.format(tb111))
        st.write('Сделано: '  + str(wb111) + ' кор., ' + 'Сумма ЗП: ' + str(ub111) + ' руб.')
        st.write('Отгрузили: '  + str(yb111) + ' кор., ' + 'Оплата: ' + str(vb111) + ' руб.')
        st.write('Склад: '  + str(xb111) + ' кор., ' + 'Долг: ' + str(tb111) + ' руб.')

        st.write('')
        st.write('')

        st.subheader('1 ручей: ')
        wc111 = float('{:.3f}'.format(wc111))
        uc111 = float('{:.3f}'.format(uc111))
        yc111 = float('{:.3f}'.format(yc111))
        vc111 = float('{:.3f}'.format(vc111))
        xc111 = float('{:.3f}'.format(xc111))
        tc111 = float('{:.3f}'.format(tc111))
        st.write('Сделано: '  + str(wc111) + ' кор., ' + 'Сумма ЗП: ' + str(uc111) + ' руб.')
        st.write('Отгрузили: '  + str(yc111) + ' кор., ' + 'Оплата: ' + str(vc111) + ' руб.')
        st.write('Склад: '  + str(xc111) + ' кор., ' + 'Долг: ' + str(tc111) + ' руб.')

if __name__ == "__main__":
    zppaketi()
