import streamlit as st
import pandas as pd
import numpy as np


def zpbahili():

    st.write('')
    st.title('ЗП БАХИЛЫ')
    st.write('')
    st.title('Ставка: ')
    col230, col240 = st.beta_columns(2)
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

    st.title('Сделано (указать кол-во коробок): ')
    col250, col260 = st.beta_columns(2)
    with col250:
        wa = st.number_input('Кол-во "Эконома": ')
        wb = st.number_input('Кол-во "Стандарта": ')
    with col260:
        wc = st.number_input('Кол-во "Прочных": ')
        wd = st.number_input('Кол-во "Детских": ')

    st.title('Отгрузили (указать кол-во коробок): ')
    col270, col280 = st.beta_columns(2)
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
    col290, col300 = st.beta_columns(2)
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
    with col290:
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
    with col300:
        st.title('Удержание с зарплаты: ')
        nakiy = st.number_input('Процент удержания:')
        nakkur = qwer * (nakiy + 100) / 100
        trio = nakkur - qwer
        st.write(str(qwer) + ' руб.')

if __name__ == "__main__":
    zpbahili()

                    #--------------------------

def zpekstruziya():

    st.write('')
    st.title('ЗП ЭКСТРУЗИЯ')
    st.write('')
    st.title('Ставка: ')
    col330, col340 = st.beta_columns(2)
    with col330:
        za1 = st.number_input('Стоимость "12 часов Смена": ')
        if za1 == 0:
            za1 = 1
        else:
            za1 < 0
    with col330:
        zb1 = st.number_input('Стоимость "24 часа смена": ')
        if zb1 == 0:
            zb1 = 1
        else:
            zb1 < 0
        ze1 = za1 * 600
        zf1 = zb1 * 1200

        st.title('Сделано (указать кол-во кг): ')
    col350, col360 = st.beta_columns(2)
    with col350:
        wa1 = st.number_input('Кол-во "за 12 часов": ')
        wb1 = st.number_input('Кол-во "за 24 часа": ')

        st.title('Отгрузили (указать кол-во кг): ')
    col370, col380 = st.beta_columns(2)
    with col370:
        ya1 = st.number_input('Кол-во "за 12 часоа": ')
        yb1 = st.number_input('Кoл-во "за 24 часа": ')

        xa1 = wa1 - ya1
        xb1 = wb1 - yb1

        ua1 = ze1 * wa1
        ub1 = zf1 * wb1
        
        va1 = ze1 * ya1
        vb1 = zf1 * yb1

        ta1 = ze1 * xa1
        tb1 = zf1 * xb1

        st.write('12 часов: ')
        st.write('Сделано: '  + str(wa1) + ' кор., ' + 'Сумма ЗП: ' + str(ua1) + ' руб.')
        st.write('Отгрузили: '  + str(ya1) + ' кор., ' + 'Оплата: ' + str(va1) + ' руб.')
        st.write('Склад: '  + str(xa1) + ' кор., ' + 'Долг: ' + str(ta1) + ' руб.')

        st.write('')
        st.write('')

        st.write('24 часа: ')
        st.write('Сделано: '  + str(wb1) + ' кор., ' + 'Сумма ЗП: ' + str(ub1) + ' руб.')
        st.write('Отгрузили: '  + str(yb1) + ' кор., ' + 'Оплата: ' + str(vb1) + ' руб.')
        st.write('Склад: '  + str(xb1) + ' кор., ' + 'Долг: ' + str(tb1) + ' руб.')

if __name__ == "__main__":
    zpekstruziya()

                    #--------------------------

def zpperchatki():

    st.write('')
    st.title('ЗП ПЕРЧАТКИ')
    st.write('')
    st.title('Ставка: ')
    col430, col440 = st.beta_columns(2)
    with col430:
        za11 = st.number_input('Стоимость "Обычные": ')
        if za11 == 0:
            za11 = 1
        else:
            za11 < 0
    with col430:
        zb11 = st.number_input('Стоимость "С манжетой": ')
        if zb11 == 0:
            zb11 = 1
        else:
            zb11 < 0

        ze11 = za11 * 5400
        zf11 = zb11 * 4500

        st.title('Сделано (указать кол-во коробок): ')
    col450, col460 = st.beta_columns(2)
    with col450:
        wa11 = st.number_input('Кол-во "Обычных": ')
        wb11 = st.number_input('Кол-во "С манжетой": ')

        st.title('Отгрузили (указать кол-во коробок): ')
    col470, col480 = st.beta_columns(2)
    with col470:
        ya11 = st.number_input('Кол-во "Обчныx": ')
        yb11 = st.number_input('Кoл-во "C манжетой": ')

        xa11 = wa11 - ya11
        xb11 = wb11 - yb11
        
        ua11 = ze11 * wa11
        ub11 = zf11 * wb11

        va11 = ze11 * ya11
        vb11 = zf11 * yb11

        ta11 = ze11 * xa11
        tb11 = zf11 * xb11

        st.write('Oбычныe: ')
        st.write('Сделано: '  + str(wa11) + ' кор., ' + 'Сумма ЗП: ' + str(ua11) + ' руб.')
        st.write('Отгрузили: '  + str(ya11) + ' кор., ' + 'Оплата: ' + str(va11) + ' руб.')
        st.write('Склад: '  + str(xa11) + ' кор., ' + 'Долг: ' + str(ta11) + ' руб.')

        st.write('')
        st.write('')

        st.write('С мaнжeтой: ')
        st.write('Сделано: '  + str(wb11) + ' кор., ' + 'Сумма ЗП: ' + str(ub11) + ' руб.')
        st.write('Отгрузили: '  + str(yb11) + ' кор., ' + 'Оплата: ' + str(vb11) + ' руб.')
        st.write('Склад: '  + str(xb11) + ' кор., ' + 'Долг: ' + str(tb11) + ' руб.')

if __name__ == "__main__":
    zpperchatki()

                    #--------------------------

def zppaketi():
    st.write('')
    st.title('ЗП ПАКЕТЫ')
    st.write('')
    st.title('Ставка: ')
    col530, col540 = st.beta_columns(2)
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

    st.title('Сделано (указать кол-во коробок): ')
    col550, col560 = st.beta_columns(2)
    with col550:
        wa111 = st.number_input('Кол-во "4 ручья": ')
        wb111 = st.number_input('Кол-во "2 ручья": ')
    with col560:
        wc111 = st.number_input('Кол-во "1 ручей": ')

    st.title('Отгрузили (указать кол-во коробок): ')
    col570, col580 = st.beta_columns(2)
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

        st.write('4 ручья: ')
        st.write('Сделано: '  + str(wa111) + ' кор., ' + 'Сумма ЗП: ' + str(ua111) + ' руб.')
        st.write('Отгрузили: '  + str(ya111) + ' кор., ' + 'Оплата: ' + str(va111) + ' руб.')
        st.write('Склад: '  + str(xa111) + ' кор., ' + 'Долг: ' + str(ta111) + ' руб.')

        st.write('')
        st.write('')

        st.write('2 ручья: ')
        st.write('Сделано: '  + str(wb111) + ' кор., ' + 'Сумма ЗП: ' + str(ub111) + ' руб.')
        st.write('Отгрузили: '  + str(yb111) + ' кор., ' + 'Оплата: ' + str(vb111) + ' руб.')
        st.write('Склад: '  + str(xb111) + ' кор., ' + 'Долг: ' + str(tb111) + ' руб.')

        st.write('')
        st.write('')

        st.write('1 ручей: ')
        st.write('Сделано: '  + str(wc111) + ' кор., ' + 'Сумма ЗП: ' + str(uc111) + ' руб.')
        st.write('Отгрузили: '  + str(yc111) + ' кор., ' + 'Оплата: ' + str(vc111) + ' руб.')
        st.write('Склад: '  + str(xc111) + ' кор., ' + 'Долг: ' + str(tc111) + ' руб.')
                        
if __name__ == "__main__":
    zppaketi()
