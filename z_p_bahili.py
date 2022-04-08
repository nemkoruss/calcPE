import streamlit as st
import pandas as pd
import numpy as np

def zpbahili():

    st.write('')
    st.title('ЗП БАХИЛЫ')
    st.write('')
    st.header('Ставка: ')
    col230, col240 = st.columns(2)
    with col230:
        za = st.number_input('Стоимость "Эконома" за пару: ')
        if za == 0:
            za = 1
        else:
            za < 0
    with col230:
        zb = st.number_input('Стоимость "Стандарта" за пару: ')
        if zb == 0:
            zb = 1
        else:
            zb < 0
    with col240:
        zc = st.number_input('Стоимость "Прочных" за пару: ')
        if zc == 0:
            zc = 1
        else:
            zc < 0
    with col240:
        zd = st.number_input('Стоимость "Детских" за пару: ')
        if zd == 0:
            zd = 1
        else:
            zd < 0
        ze = za * 4000
        zf = zb * 3500
        zg = zc * 2000
        zh = zd * 5400

    st.header('Сделано (указать кол-во коробок): ')
    col250, col260 = st.columns(2)
    with col250:
        wa = st.number_input('Кол-во "Эконома": ')
        wb = st.number_input('Кол-во "Стандарта": ')
    with col260:
        wc = st.number_input('Кол-во "Прочных": ')
        wd = st.number_input('Кол-во "Детских": ')

    st.header('Отгрузили (указать кол-во коробок): ')
    col270, col280 = st.columns(2)
    with col270:
        ya = st.number_input('Кол-во "Экoнома": ')
        yb = st.number_input('Кoл-во "Стандарта": ')
    with col280:
        yc = st.number_input('Кол-вo "Прочных": ')
        yd = st.number_input('Кoл-во "Детских": ')

        xa = wa - ya
        xb = wb - yb
        xc = wc - yc
        xd = wd - yd

        ua = ze * wa
        ub = zf * wb
        uc = zg * wc
        ud = zh * wd

        va = ze * ya
        vb = zf * yb
        vc = zg * yc
        vd = zh * yd

        ta = ze * xa
        tb = zf * xb
        tc = zg * xc
        td = zh * xd
    col290, col300 = st.columns(2)
    with col290:
        st.subheader('Эконом: ')
        st.write('Сделано: '  + str(wa) + ' кор., ' + 'Сумма ЗП: ' + str(ua) + ' руб.')
        st.write('Отгрузили: '  + str(ya) + ' кор., ' + 'Оплата: ' + str(va) + ' руб.')
        st.write('Склад: '  + str(xa) + ' кор., ' + 'Долг: ' + str(ta) + ' руб.')

        st.write('')
        st.write('')
    with col290:
        st.subheader('Стандарт: ')
        st.write('Сделано: '  + str(wb) + ' кор., ' + 'Сумма ЗП: ' + str(ub) + ' руб.')
        st.write('Отгрузили: '  + str(yb) + ' кор., ' + 'Оплата: ' + str(vb) + ' руб.')
        st.write('Склад: '  + str(xb) + ' кор., ' + 'Долг: ' + str(tb) + ' руб.')

        st.write('')
        st.write('')
    with col290:
        st.subheader('Прочные: ')
        st.write('Сделано: '  + str(wc) + ' кор., ' + 'Сумма ЗП: ' + str(uc) + ' руб.')
        st.write('Отгрузили: '  + str(yc) + ' кор., ' + 'Оплата: ' + str(vc) + ' руб.')
        st.write('Склад: '  + str(xc) + ' кор., ' + 'Долг: ' + str(tc) + ' руб.')

        st.write('')
        st.write('')
    with col300:
        st.subheader('Детские: ')
        st.write('Сделано: '  + str(wd) + ' кор., ' + 'Сумма ЗП: ' + str(ud) + ' руб.')
        st.write('Отгрузили: '  + str(yd) + ' кор., ' + 'Оплата: ' + str(vd) + ' руб.')
        st.write('Склад: '  + str(xd) + ' кор., ' + 'Долг: ' + str(td) + ' руб.')

        st.write('')
        st.write('')
    with col300:
        st.write('Итого к оплате: ')
        qwer = ua + ub + uc + ud
        st.subheader(str(qwer) + ' руб.')

        st.write('')
    with col290:
        st.header('Удержание с зарплаты: ')
        nakiy = st.number_input('Процент удержания:')
        nakkur = qwer * (nakiy + 100) / 100
        trio = nakkur - qwer
        st.write(str(trio) + ' руб.')

if __name__ == "__main__":
    zpbahili()