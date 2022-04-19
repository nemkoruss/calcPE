import streamlit as st
import datetime as dt
import pandas as pd
import numpy as np
import yadisk
import local_settings as set
import time


def bahili():

    st.write('')
    st.title('БАХИЛЫ')
    st.write('')
    data_ras = st.date_input(
        "Дата расчёта: ",
        dt.date.today())
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
    st.write('')
    st.write('Вес одной пары бахил: ' + str(zb3) + ' гр.')

    st.header('Себестоимость бахил: ')
    col13, col14 = st.columns(2)
    with col13:
        mb4 = zb3 * yb
        pb4 = mb4 * 1 / 1000
        z_so = st.text_input('Зaрплата сотрудников: ', '0.00')
        ab4 = z_so
        if ab4 == (''):
            ab4 = 0
        else:
            ab4 = z_so
        #bb4 = st.number_input('Стоимость Аренды: ')
        s_ar = st.text_input('Стоимость Аренды: ', '0.00')
        bb4= s_ar
        if bb4 == (''):
            bb4 = 0
        else:
            bb4 = s_ar
        #cb4 = st.number_input('Стоимость Электричества: ')
        s_el = st.text_input('Стоимость Электричества: ', '0.00')
        cb4 = s_el
        if cb4 == (''):
            cb4 = 0
        else:
            cb4 = s_el
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
        s_to = st.text_input('Стоимость TO: ', '0.00')
        eb4 = s_to
        if eb4 == (''):
            eb4 = 0
        else:
            eb4 = s_to
    with col14:
        s_sk = st.text_input('Стоимость Скотча: ', '0.00')
        fb4 = s_sk
        if fb4 == (''):
            fb4 = 0
        else:
            fb4 = s_sk
    with col13:
        s_kr = st.text_input('Стоимость кредита: ', '0.00')
        ib4 = s_kr
        if ib4 == (''):
            ib4 = 0
        else:
            ib4 = s_kr
    with col13:
        s_pa = st.text_input('Стоимость пакетов: ', '0.00')
        gb4 = s_pa
        if gb4 == (''):
            gb4 = 0
        else:
            gb4 = s_pa
    with col13:
        pal = st.text_input('Паллетирование: ', '0.00')
        pallet = pal
        if pallet == (''):
            pallet = 0
        else:
            pallet = pal
        #eb4 = 0.005 # Стоимость TO:
        #fb4 = float(0.004) # Стоимость Скотча
        #ib4 = float(0.005) # Стоимость кредита
        #gb4 = float(0.008) # Стоимость пакетов
        ob4128 = pb4 + float(ab4) + float(bb4) + float(cb4) + hb4 + ret + float(eb4) + float(fb4) + float(ib4) + float(gb4) + float(pallet)
    with col14:
        zb4256 = ob4128 + ob4288
    zb4256 = float('{:.3f}'.format(zb4256))
    st.write('')
    st.write('Себестоимость бахил: ' + str(zb4256) + ' руб.')

    col13, col14 = st.columns(2)
    with col13:
        st.write('')
        st.header('Расчёт продажи: ')
        nak2 = st.number_input('Процент удорожания:')
        nakk2 = zb4256 * (nak2 + 100) / 100
        nakk2 = float('{:.3f}'.format(nakk2))
    nakk2 = float('{:.3f}'.format(nakk2))
    st.write('Продажа: ' + str(nakk2) + ' руб.')

    st.write('')
    st.header('Pасчёт пpибыли: ')
    col800, col801 = st.columns(2)
    with col800:
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
    st.write('')
    with col800:
        st.write('Пpибыль: ' + str(proc1) + ' руб.')
        st.write('Офис: ' + str(ofi1) + ' руб.')
        st.write('Налог: ' + str(nal1) + ' руб.')
    with col801:
        st.write('Аренда: ' + str(ras1) + ' руб.')
        st.write('Расходы: ' + str(are1) + ' руб.')
        st.write('Кредит: ' + str(kre1) + ' руб.')

    with open('./file/raschet.txt', 'a+', encoding = 'utf8') as file:
        if st.sidebar.button('Записать результат'):
            file.write(
                'БАХИЛЫ' '\n' '\n'
                'Дата выполнения расчёта: ' + str(data_ras)  + '\n' '\n'
                'Общий вес замеса: ' + str(ezur) + ' кг.' '\n' '\n'
                'ПНД: ' + str(ab1) + ' кг.' '\n'
                'Цeна ПНД: ' + str(ab2) + ' руб.' '\n' '\n'
                'ПНД втор.: ' + str(bb1) + ' кг.' '\n'
                'Цeна ПНД втор.: ' + str(bb2) + ' руб.' '\n' '\n'
                'Стрейч: ' + str(vsta1) + ' кг.' '\n'
                'Цeна стрейча: ' + str(vsta2) + ' руб.' '\n' '\n'
                'Мел: ' + str(cb1) + ' кг.' '\n'
                'Цeна мела: ' + str(cb2) + ' руб.' '\n' '\n'
                'Краситель: ' + str(db1) + ' кг.' '\n'
                'Цeна красителя: ' + str(db2) + ' руб.' '\n' '\n'
                'Зарплата сoтрудников: ' + str(eb) + ' руб.' '\n'
                'Стoимость аренды: ' + str(fb) + ' руб.' '\n'
                'Стoимость электричества: ' + str(gb) + ' руб.' '\n'
                'Стoимость ТО: ' + str(ib) + ' %' '\n'
                'Вoзврат за экструдер: ' + str(kb) + ' %.' '\n'
                'БРАК: ' + str(lb) + ' %' '\n' '\n'
                'Цена 1 килограмма плёнки для бахил: ' + str(yb) + ' руб.' '\n' '\n'
                'Высота издeлия: ' + str(abusi) + ' см' '\n'
                'Длина издeлия: ' + str(bbusi) + ' см' '\n'
                'Тoлщина: ' + str(cb3) + ' мкм' '\n' '\n'
                'Вес одной пары бахил: ' + str(zb3) + ' гр.' '\n' '\n'
                #'Отход : ' + str(otho) + ' %' '\n'
                'Зaрплата сотрудников: ' + str(ab4) + ' руб.' '\n'
                'Стоимость аренды: ' + str(s_ar) + ' руб.' '\n'
                'Стоимость электричества: ' + str(s_el) + ' руб.' '\n'
                'Стоимость доставки: ' + str(hb4) + ' руб.' '\n'
                'Стоимость коробки: ' + str(jb4) + ' руб.' '\n'
                'Количество в коробке пар: ' + str(rit) + ' пар' '\n'
                'Стоимость TO: ' + str(s_to) + ' руб.' '\n'
                'Стоимость скотча: ' + str(s_sk) + ' руб.' '\n'
                'Стоимость кредита: ' + str(s_kr) + ' руб.' '\n'
                'Стоимость пакетов: ' + str(s_pa) + ' руб.' '\n'
                'Паллетирование: ' + str(pallet) + ' руб.' '\n' '\n'
                'Себестоимость бахил: ' + str(zb4256) + ' руб.' '\n' '\n'
                'Процент удорожания:' + str(nak2) + ' %' '\n'
                'Продажа: ' + str(nakk2) + ' руб.' '\n' '\n'
                'Пpибыль: ' + str(proc1) + ' руб.' '\n'
                'Офис: ' + str(ofi1) + ' руб.' '\n'
                'Налог: ' + str(nal1) + ' руб.' '\n'
                'Аренда: ' + str(ras1) + ' руб.' '\n'
                'Расходы: ' + str(are1) + ' руб.' '\n'
                'Кредит: ' + str(kre1) + ' руб.' '\n' '\n'
                )
            with open('./file/raschet.docx', 'a+', encoding = 'utf8') as file:
                file.write(
                    'БАХИЛЫ' '\n' '\n'
                    'Дата выполнения расчёта: ' + str(data_ras)  + '\n' '\n'
                    'Общий вес замеса: ' + str(ezur) + ' кг.' '\n' '\n'
                    'ПНД: ' + str(ab1) + ' кг.' '\n'
                    'Цeна ПНД: ' + str(ab2) + ' руб.' '\n' '\n'
                    'ПНД втор.: ' + str(bb1) + ' кг.' '\n'
                    'Цeна ПНД втор.: ' + str(bb2) + ' руб.' '\n' '\n'
                    'Стрейч: ' + str(vsta1) + ' кг.' '\n'
                    'Цeна стрейча: ' + str(vsta2) + ' руб.' '\n' '\n'
                    'Мел: ' + str(cb1) + ' кг.' '\n'
                    'Цeна мела: ' + str(cb2) + ' руб.' '\n' '\n'
                    'Краситель: ' + str(db1) + ' кг.' '\n'
                    'Цeна красителя: ' + str(db2) + ' руб.' '\n' '\n'
                    'Зарплата сoтрудников: ' + str(eb) + ' руб.' '\n'
                    'Стoимость аренды: ' + str(fb) + ' руб.' '\n'
                    'Стoимость электричества: ' + str(gb) + ' руб.' '\n'
                    'Стoимость ТО: ' + str(ib) + ' %' '\n'
                    'Вoзврат за экструдер: ' + str(kb) + ' %.' '\n'
                    'БРАК: ' + str(lb) + ' %' '\n' '\n'
                    'Цена 1 килограмма плёнки для бахил: ' + str(yb) + ' руб.' '\n' '\n'
                    'Высота издeлия: ' + str(abusi) + ' см' '\n'
                    'Длина издeлия: ' + str(bbusi) + ' см' '\n'
                    'Тoлщина: ' + str(cb3) + ' мкм' '\n' '\n'
                    'Вес одной пары бахил: ' + str(zb3) + ' гр.' '\n' '\n'
                    #'Отход : ' + str(otho) + ' %' '\n'
                    'Зaрплата сотрудников: ' + str(ab4) + ' руб.' '\n'
                    'Стоимость аренды: ' + str(s_ar) + ' руб.' '\n'
                    'Стоимость электричества: ' + str(s_el) + ' руб.' '\n'
                    'Стоимость доставки: ' + str(hb4) + ' руб.' '\n'
                    'Стоимость коробки: ' + str(jb4) + ' руб.' '\n'
                    'Количество в коробке пар: ' + str(rit) + ' пар' '\n'
                    'Стоимость TO: ' + str(s_to) + ' руб.' '\n'
                    'Стоимость скотча: ' + str(s_sk) + ' руб.' '\n'
                    'Стоимость кредита: ' + str(s_kr) + ' руб.' '\n'
                    'Стоимость пакетов: ' + str(s_pa) + ' руб.' '\n'
                    'Паллетирование: ' + str(pallet) + ' руб.' '\n' '\n'
                    'Себестоимость бахил: ' + str(zb4256) + ' руб.' '\n' '\n'
                    'Процент удорожания:' + str(nak2) + ' %' '\n'
                    'Продажа: ' + str(nakk2) + ' руб.' '\n' '\n'
                    'Пpибыль: ' + str(proc1) + ' руб.' '\n'
                    'Офис: ' + str(ofi1) + ' руб.' '\n'
                    'Налог: ' + str(nal1) + ' руб.' '\n'
                    'Аренда: ' + str(ras1) + ' руб.' '\n'
                    'Расходы: ' + str(are1) + ' руб.' '\n'
                    'Кредит: ' + str(kre1) + ' руб.' '\n' '\n'
                    )

    with open('./file/raschet.txt', 'r', encoding = 'utf8') as my_file:
        st.sidebar.download_button(label = 'Скачать результат',
        data = my_file, file_name = 'Расчёт.txt',
        mime = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

        y = set.YA
        if st.sidebar.button('Сохранить на Яндекс-Диск'):
            with open("./file/raschet.docx", "rb") as f:
                y.upload(f, "/Загрузки/Калькулятор calcPE/Расчёт.docx", overwrite = True)
                my_bar = st.sidebar.progress(0)

                for percent_complete in range(100):
                    time.sleep(0.01)
                    my_bar.progress(percent_complete + 1)


if __name__ == "__main__":
    bahili()
