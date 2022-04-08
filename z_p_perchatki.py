import streamlit as st
import pandas as pd
import numpy as np

def zpperchatki():

    st.write('')
    st.title('ЗП ПЕРЧАТКИ')
    st.write('')
    st.header('Ставка: ')
    col430, col440 = st.columns(2)
    with col430:
        za11 = st.number_input('Стоимость "Обычные": ')
        if za11 == 0:
            za11 = 1
        else:
            za11 < 0
    with col440:
        zb11 = st.number_input('Стоимость "С манжетой": ')
        if zb11 == 0:
            zb11 = 1
        else:
            zb11 < 0

        ze11 = za11 * 5400
        zf11 = zb11 * 4500

    st.header('Сделано (указать кол-во коробок): ')
    col450, col460 = st.columns(2)
    with col450:
        wa11 = st.number_input('Кол-во "Обычных": ')
    with col460:
        wb11 = st.number_input('Кол-во "С манжетой": ')

    st.header('Отгрузили (указать кол-во коробок): ')
    col470, col480 = st.columns(2)
    with col470:
        ya11 = st.number_input('Кол-во "Обчныx": ')
    with col480:
        yb11 = st.number_input('Кoл-во "C манжетой": ')

        xa11 = wa11 - ya11
        xb11 = wb11 - yb11

        ua11 = ze11 * wa11
        ub11 = zf11 * wb11

        va11 = ze11 * ya11
        vb11 = zf11 * yb11

        ta11 = ze11 * xa11
        tb11 = zf11 * xb11
    with col470:
        st.write('')
        st.write('')
        st.subheader('Oбычныe: ')
        st.write('Сделано: '  + str(wa11) + ' кор., ' + 'Сумма ЗП: ' + str(ua11) + ' руб.')
        st.write('Отгрузили: '  + str(ya11) + ' кор., ' + 'Оплата: ' + str(va11) + ' руб.')
        st.write('Склад: '  + str(xa11) + ' кор., ' + 'Долг: ' + str(ta11) + ' руб.')

        st.write('')
        st.write('')

        st.subheader('С мaнжeтой: ')
        st.write('Сделано: '  + str(wb11) + ' кор., ' + 'Сумма ЗП: ' + str(ub11) + ' руб.')
        st.write('Отгрузили: '  + str(yb11) + ' кор., ' + 'Оплата: ' + str(vb11) + ' руб.')
        st.write('Склад: '  + str(xb11) + ' кор., ' + 'Долг: ' + str(tb11) + ' руб.')

if __name__ == "__main__":
    zpperchatki()