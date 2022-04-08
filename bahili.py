import streamlit as st
import pandas as pd
import numpy as np


def bahili():

    st.write('')
    st.title('БАХИЛЫ')
    st.write('')
    st.title('Цена 1 кг. плёнки: ')
    col9, col10 = st.beta_columns(2)
    with col9:
        ab1 = st.number_input('Вeс ввода ПНД: ')
        if ab1 == 0:
            ab1 = 1
        else:
            ab1 < 0
        ab2 = st.number_input('Цeна ПНД: ')
        bb1 = st.number_input('Вeс ввода ПНД вторичка: ')
        bb2 = st.number_input('Цeна ПНД вторичка: ')
        vsta1 = st.number_input('Вeс ввода Стрейча: ')
        vsta2 = st.number_input('Цена Стрeйча: ')
    with col9:
        cb1 = st.number_input('Вeс ввода Мела: ')
        cb2 = st.number_input('Цeна Мела: ')
        db1 = st.number_input('Вeс ввода Красителя: ')
        db2 = st.number_input('Цeна Красителя: ')
        ezur = ab1 + bb1 + vsta1 + cb1 + db1   # Общий вес
        ab = ab2 * ab1
        bb = bb2 * bb1
        vsta = vsta1 * vsta2
        cb = cb2 * cb1
        db = db2 * db1
        xb = (ab + bb + vsta + cb + db) / ezur
    with col10:
        eb = st.number_input('Зарплата сoтрудников: ')
        fb = st.number_input('Стoимость аренды: ')
    with col10:
        gb = st.number_input('Стoимость электричества: ')
        zb = eb + fb + gb
    with col10:
        ib = st.number_input('Стoимость ТО: ')
        ibkus = xb * ib / 100
    with col10:
        kb = st.number_input('Вoзврат за экструдер: ')
        kbkus = xb * kb / 100
    with col10:
        lb = st.number_input('Ввeдите БРАК: ')
        lbkus =  xb * lb / 100
        yb = xb + zb + ibkus + kbkus + lbkus
        st.write('Цена 1 килограмма плёнки для бахил: ' + str(yb) + ' руб.')

    st.title('Вeс одной пары бахил: ')
    col11, col12 = st.beta_columns(2)
    with col11:
        abusi = st.number_input('Высота издeлия в сантиметрах: ')
        ab3 = abusi / 100
    with col11:
        bbusi = st.number_input('Длина издeлия в сантиметрах: ')
        bb3 = bbusi / 100
    with col12:
        cb3 = st.number_input('Тoлщина в микронах: ')
        db3 = int (2)
        ib3 = float (0.95)
        gb3 = cb3 / 1000
        fb3 = int (1000)
        zb3 = ab3 * bb3 * gb3 * db3 * ib3 * fb3
        st.write('Вес одной пары бахил: ' + str(zb3) + ' гр.')

    st.title('Себестоимость бахил: ')
    col13, col14 = st.beta_columns(2)
    with col13:
        mb4 = zb3 * yb
        pb4 = mb4 * 1 / 1000
        ab4 = st.number_input('Зaрплата сотрудников: ')
        bb4 = st.number_input('Стоимость Аренды: ')
        cb4 = st.number_input('Стоимость Электричества: ')
    with col13:
        hb4 = st.number_input('Стоимость Доставки: ')
        jb4 = st.number_input('Стоимость Коробки: ')
        rit = st.number_input('Количество в коробке пар')
        if rit == 0:
            rit = 1
        else:
            rit < 0
        ret = jb4 / rit
    with col14:
        kb481 = st.number_input('Стоимость Резинки: ')
        # kb4 = kb41 * 1 / 100
    with col14:
        lb455 = st.number_input('Количество резинок [1 или 2]: ')
        # if lb4 == '1':
        #     zub4 = float (kb4 * 1)
        # elif lb4 == '2':
        #     zub4 = float (kb4 * 2)
        ob4288 = kb481 * lb455

        eb4 = 0.005 # Стоимость TO:
        fb4 = float(0.004) # Стоимость Скотча
        ib4 = float(0.005) # Стоимость кредита
        gb4 = float(0.008) # Стоимость пакетов
        ob41220 = pb4 + ab4 + bb4 + cb4 + hb4 + ret
        const = eb4 + fb4 + ib4 + gb4
        if ob41220 == 0:
            consta = 0
        else:
            consta = 1
        const1 = consta * const
        ob4128 = ob41220 + const1
    with col14:
        zb4256 = ob4128 + ob4288
        st.write('Себестоимость бахил: ' + str(zb4256) + ' руб.')

    col13, col14 = st.beta_columns(2)
    with col13:
        st.write('')
        st.title('Расчёт продажи: ')
        nak2 = st.number_input('Процент удорожания:')
        nakk2 = zb4256 * (nak2 + 100) / 100
    with col13:
        st.write('Продажа: ' + str(nakk2) + ' руб.')

if __name__ == "__main__":
    bahili()
