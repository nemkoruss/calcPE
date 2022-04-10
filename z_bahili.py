import streamlit as st
import pandas as pd
import numpy as np


def bahili():

    st.write('')
    st.title('БАХИЛЫ')
    st.write('')
    st.header('Цена 1 кг. плёнки: ')
    col9, col10 = st.columns(2)
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
    with col10:
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
        yb = float('{:.3f}'.format(yb))

    with col9:
        st.write('')
        st.write('Цена 1 килограмма плёнки для бахил: ' + str(yb) + ' руб.')

    st.header('Вeс одной пары бахил: ')
    col11, col12 = st.columns(2)
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
        zb3 = float('{:.3f}'.format(zb3))

    with col11:
        st.write('')
        st.write('Вес одной пары бахил: ' + str(zb3) + ' гр.')

    st.header('Себестоимость бахил: ')
    col13, col14 = st.columns(2)
    with col13:
        mb4 = zb3 * yb
        pb4 = mb4 * 1 / 1000
        ab4 = st.number_input('Зaрплата сотрудников: ')
        bb4 = st.number_input('Стоимость Аренды: ')
        cb4 = st.number_input('Стоимость Электричества: ')
    with col13:
        hb4 = st.number_input('Стоимость Доставки: ')
    with col14:
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
        zb4256 = float('{:.3f}'.format(zb4256))
    with col13:
        st.write('')
        st.write('Себестоимость бахил: ' + str(zb4256) + ' руб.')

    col13, col14 = st.columns(2)
    with col13:
        st.write('')
        st.header('Расчёт продажи: ')
        nak2 = st.number_input('Процент удорожания:')
        nakk2 = zb4256 * (nak2 + 100) / 100
        nakk2 = float('{:.3f}'.format(nakk2))

    with col13:
        st.write('')
        st.write('Продажа: ' + str(nakk2) + ' руб.')

    with col13:
        st.write('')
        st.header('Pасчёт пpибыли: ')
        prib1 = (nakk2 - zb4256)
        proc1 = prib1 - (20 / 100 * prib1)
        ofi1 = (proc1 / 100) * 50
        nal1 = (proc1 / 100) * 8
        ras1 = (proc1 / 100) * 20
        are1 = (proc1 / 100) * 20
        kre1 = (proc1 / 100) * 2
        proc1 = float('{:.3f}'.format(proc1))
        ofi1 = float('{:.3f}'.format(ofi1))
        nal1 = float('{:.3f}'.format(nal1))
        ras1 = float('{:.3f}'.format(ras1))
        are1 = float('{:.3f}'.format(are1))
        kre1 = float('{:.3f}'.format(kre1))

    with col13:
        st.write('')
        st.write('Пpибыль: ' + str(proc1) + ' руб.')
        st.write('Офис: ' + str(ofi1) + ' руб.')
        st.write('Налог: ' + str(nal1) + ' руб.')
        st.write('Аренда: ' + str(ras1) + ' руб.')
        st.write('Расходы: ' + str(are1) + ' руб.')
        st.write('Кредит: ' + str(kre1) + ' руб.')

    with open('./txt/info.txt', 'a+', encoding = 'utf8') as file:
        if st.sidebar.button('Записать результат'):
            file.write('Цена 1 килограмма плёнки для бахил: ' + str(yb) + ' руб.' '\n' '\n'
                'Вес одной пары бахил: ' + str(zb3) + ' гр.' '\n' '\n'
                'Себестоимость бахил: ' + str(zb4256) + ' руб.' '\n' '\n'
                'Продажа: ' + str(nakk2) + ' руб.' '\n'
                'Пpибыль: ' + str(proc1) + ' руб.' '\n'
                'Офис: ' + str(ofi1) + ' руб.' '\n'
                'Расходы: ' + str(nal1) + ' руб.' '\n'
                'Аренда: ' + str(ras1) + ' руб.' '\n'
                'Пpибыль: ' + str(are1) + ' руб.' '\n'
                'Кредит: ' + str(kre1) + ' руб.' '\n' '\n')

    with open('./txt/info.txt', 'r', encoding = 'utf8') as my_file:
        st.sidebar.download_button(label = 'Скачать результат',
        data = my_file, file_name = 'rinfo.txt',
        mime = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

if __name__ == "__main__":
    bahili()
