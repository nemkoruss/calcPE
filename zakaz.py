import streamlit as st
import pandas as pd
import numpy as np


def za_bahili():

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

if __name__ == "__main__":
    za_bahili()


                    #---------------------------

def za_plenka():

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

if __name__ == "__main__":
    za_plenka()

                    #---------------------------

def za_paketi():
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

if __name__ == "__main__":
    za_paketi()

                    #--------------------------

def za_perchatki():

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

if __name__ == "__main__":
    za_perchatki()







