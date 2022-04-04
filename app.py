import streamlit as st
import pandas as pd
import numpy as np
import local_settings as settings # Самописный модуль с информацией
#from PIL import Image # Для отображения изображений
import plenka as pl
from plenka import plastik
import products as pr
from products import product
from product import paketi, bahili, perchatki



def main():
    menu = ["Инструкция", "Калькулятор", "Контакты"]
    choice = st.sidebar.selectbox("Меню" ,menu)

    if choice == "Инструкция":
            st.subheader ("Инструкция")
            st.subheader('Для работы калькулятора выберите в боковом меню нужный расчёт !')
            st.markdown('*Для входа в боковое меню на устройстве с маленьким экраном нажмите, в левом вверхнем углу, значок в виде стрелки  ">"*')
            st.markdown('*Для более комфортной работы, не забывайте "Очищать экран"  *')

    elif choice == "Калькулятор":
           # st.subheader("Пароль верный")
            #username = st.sidebar.text_input("Имя")
            password = st.sidebar.text_input("Пароль", type='password')
            if st.sidebar.checkbox("Войти"):

               # if password == 'tatoshka12':
                if password == settings.MYSQL_PASSWORD:

                    st.success("Верный пароль! ") # {}".format(username) )
                                        
                    b = st.sidebar.selectbox('РАСЧЁТ ПЛЕНКИ:', ['Выбрать/Очистить','Замес гранулы'])
                    
                    if b == 'Замес гранулы':
                        b = plastik() 
           
                    #-----------------------------------------------------------------
                    
                    x = st.sidebar.selectbox('РАСЧЁТ ПРОДУКЦИИ:', ['Выбрать/Очистить','Пакеты','Бахилы','Перчатки'])
                    
                    if x == "Пакеты":
                        x = paketi()
                        
                    #------------------------
                    
                    elif x == "Бахилы":
                        x = bahili()                   
                       
                    #-------------------------
                    
                    elif x == "Перчатки":
                        x = perchatki() 
                        
                    #----------------------------------------------------------------
                    
                    y = st.sidebar.selectbox('РАСЧЁТ ЗАКАЗА:', ['Выбрать/Очистить','Заказ на бахилы','Заказ на пленку', 'Заказ на пакеты','Заказ на перчатки'])
                    
                    if y == "Заказ на бахилы":
                        st.write('')
                        st.title('ЗАЯВКА БАХИЛЫ')
                        st.write('')
                        st.title('Расчёт выполнения заказа: ')
                        col21, col22 = st.beta_columns(2)
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
                        st.write('Для выполнения заказа нужно: ' + str(sza) + ' день/дня/дней')
                    
                    #---------------------------
                    
                    if y == "Заказ на пленку":
                        st.write('')
                        st.title('ЗАЯВКА ПЛЕНКА')
                        st.write('')
                        st.title('Расчёт выполнения заказа: ')
                        col23, col24 = st.beta_columns(2)
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
                        st.write('Для выполнения заказа нужно: ' + str(sza1) + ' день/дня/дней')
                    
                    #---------------------------
                    
                    if y == "Заказ на пакеты":
                        st.write('')
                        st.title('ЗАЯВКА ПАКЕТЫ')
                        st.write('')
                        st.title('Расчёт выполнения заказа: ')
                        col25, col26 = st.beta_columns(2)
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
                    
                        st.write('Для выполнения заказа нужно: ' + str(sza11) + ' день/дня/дней')
                    
                    #--------------------------
                    
                    if y == "Заказ на перчатки":
                        st.write('')
                        st.title('ЗАЯВКА ПЕРЧАТКИ')
                        st.write('')
                        st.title('Расчёт выполнения заказа: ')
                        col27, col28 = st.beta_columns(2)
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
                    
                    #-----------------------------------------------------------------
                    
                    z = st.sidebar.selectbox('РАСЧЁТ ВЫПЛАТ:', ['Выбрать/Очистить','Цех бахил','Цех экструзии', 'Цех перчатки','Цех пакеты',])
                    
                    if z == "Цех бахил":
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
                    
                    
                    
                    #--------------------------
                    
                    if z == "Цех экструзии":
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
                    
                    #--------------------------
                    
                    if z == "Цех перчатки":
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
                    
                    #--------------------------
                    
                    if z == "Цех пакеты":
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
                    
                    #-------------------------

                else:
                    st.warning("Неверный пароль! ") # {}".format(username) )

    elif choice == "Контакты":
                st.subheader("Контакты")
                st.markdown('**Корпоративный сайт: ** [tpkpromed.ru](https://tpkpromed.ru)')
                st.markdown('**Производство бахил: ** [bioinvn.ru](https://bioinvn.ru)')
                st.markdown('**Интернет магазин: ** [pmpsale.ru](https://pmpsale.ru)')
                # st.markdown('**Скачать приложение: ** [Скачать](https://goo.su/RH7qQ)')
                # image = Image.open('./qrcode/qrcode.jpg')
                # st.image(image, width = 100, caption='QR код для скачивания',use_column_width=100)

if __name__ == '__main__':
        main()
