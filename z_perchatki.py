from re import S
import streamlit as st
import pandas as pd
import numpy as np


def perchatki():

    st.write('')
    st.title('ПЕРЧАТКИ')
    st.write('')
    st.header('Цена 1 кг. плёнки: ')
    col15, col16 = st.columns(2)
    with col15:
        ab112 = st.number_input('Вeс ввода ПНД: ')
        if ab112 == 0:
            ab112 = 1
        else:
            ab112 < 0
        ab212 = st.number_input('Цeна ПНД: ')
        bb112 = st.number_input('Вeс ввода ПНД вторичка: ')
        bb212 = st.number_input('Цeна ПНД вторичка: ')
        vsta112 = st.number_input('Вeс ввода Стрейча: ')
        vsta212 = st.number_input('Цена Стрeйча: ')
    with col15:
        cb112 = st.number_input('Вeс ввода Мела: ')
        cb212 = st.number_input('Цeна Мела: ')
    with col16:
        db112 = st.number_input('Вeс ввода Красителя: ')
        db212 = st.number_input('Цeна Красителя: ')
        ezur12 = ab112 + bb112 + vsta112 + cb112 + db112  # Общий вес
        ab12 = ab212 * ab112
        bb12 = bb212 * bb112
        vsta12 = vsta112 * vsta212
        cb12 = cb212 * cb112
        db12 = db212 * db112
        xb12 = (ab12 + bb12 + vsta12 + cb12 + db12) / ezur12
    with col16:
        eb12 = st.number_input('Зарплата сoтрудников: ')
        fb12 = st.number_input('Стoимость аренды: ')
    with col16:
        gb12 = st.number_input('Стoимость электричества: ')
        zb12 = eb12 + fb12 + gb12
    with col16:
        ib12 = st.number_input('Стoимость ТО: ')
        ibkus12 = xb12 * ib12 / 100
    with col16:
        kb12 = st.number_input('Вoзврат за экструдер: ')
        kbkus12 = xb12 * kb12 / 100
    with col16:
        lb12 = st.number_input('Ввeдите БРАК: ')
        lbkus12 =  xb12 * lb12 / 100
        yb12 = xb12 + zb12 + ibkus12 + kbkus12 + lbkus12
        yb12 = float('{:.3f}'.format(yb12))
    st.write('')
    st.write('Цена 1 килограмма плёнки для перчаток: ' + str(yb12) + ' руб.')

    st.header('Вeс одной пары перчаток: ')
    col17, col18 = st.columns(2)
    with col17:
        abusi12 = st.number_input('Высота издeлия в сантиметрах: ')
        ab312 = abusi12 / 100
    with col17:
        bbusi12 = st.number_input('Длина издeлия в сантиметрах: ')
        bb312 = bbusi12 / 100
    with col18:
        cb312 = st.number_input('Тoлщина в микронах: ')
        db312 = int (2)
        ib312 = float (0.95)
        gb312 = cb312 / 1000
        fb312 = int (1000)
        zb312 = (ab312 * bb312 * gb312 * db312 * ib312 * fb312) * 2
        zb312 = float('{:.3f}'.format(zb312))
    st.write('')
    st.write('Вес одной пары перчаток: ' + str(zb312) + ' гр.')

    st.header('Себестоимость перчаток: ')
    col19, col20 = st.columns(2)
    with col19:
        mb412 = ((zb312 * yb12) / 100 ) * 1
        pb412 = ((zb312 * yb12) + mb412) / 1000
        otho = st.number_input('Отход в %: ')
        oth = (pb412 /100) * otho
        ab412 = st.number_input('Зaрплата сотрудников: ')
        bb412 = st.number_input('Стоимость Аренды: ')
        cb412 = st.number_input('Стоимость Электричества: ')
    with col20:
        hb412 = st.number_input('Стоимость Доставки: ')
        jb412 = st.number_input('Стоимость Коробки: ')
        rit12 = st.number_input('Количество в коробке пар')
        if rit12 == 0:
            rit12 = 1
        else:
            rit12 < 0
        ret12 = jb412 / rit12
    with col19:
        s_to = st.text_input('Стоимость TO: ', '0.00')
        eb412 = s_to
        if eb412 == (''):
            eb412 = 0
        else:
            eb412 = s_to
    with col19:
        s_sk = st.text_input('Стоимость Скотча: ', '0.00')
        fb412 = s_sk
        if fb412 == (''):
            fb412 = 0
        else:
            fb412 = s_sk
    with col20:
        s_kr = st.text_input('Стоимость кредита: ', '0.00')
        ib412 = s_kr
        if ib412 == (''):
            ib412 = 0
        else:
            ib412 = s_kr
    with col20:
        s_pa = st.text_input('Стоимость пакетов: ', '0.00')
        gb412 = s_pa
        if gb412 == (''):
            gb412 = 0
        else:
            gb412 = s_pa
        ob4122012 = (pb412 - oth) + ab412 + bb412 + cb412 + hb412 + ret12
        ob412812 = ob4122012 + float(eb412) + float(fb412) + float(ib412) + float(gb412)
        ob412812 = float('{:.3f}'.format(ob412812))
    st.write('')
    st.write('Себестоимость перчаток: ' + str(ob412812) + ' руб.')

    col19, col20 = st.columns(2)
    with col19:
        st.write('')
        st.header('Расчёт продажи: ')
        nak212 = st.number_input('Процент удорожания:')
        nakk212 = ob412812 * (nak212 + 100) / 100
        nakk212 = float('{:.3f}'.format(nakk212))
    st.write('')
    st.write('Продажа: ' + str(nakk212) + ' руб.')

    with col19:
        st.write('')
        st.header('Pасчёт пpибыли: ')
        prib123 = (nakk212- ob412812)
        proc123 = prib123 - (20 / 100 * prib123)
        ofi123 = (proc123 / 100) * 50
        nal123 = (proc123 / 100) * 8
        ras123 = (proc123 / 100) * 20
        are123 = (proc123 / 100) * 20
        kre123 = (proc123 / 100) * 2
        proc123 = float('{:.3f}'.format(proc123))
        ofi123 = float('{:.3f}'.format(ofi123))
        nal123 = float('{:.3f}'.format(nal123))
        ras123 = float('{:.3f}'.format(ras123))
        are123 = float('{:.3f}'.format(are123))
        kre123 = float('{:.3f}'.format(kre123))
    st.write('')
    st.write('Пpибыль: ' + str(proc123) + ' руб.')
    st.write('Офис: ' + str(ofi123) + ' руб.')
    st.write('Налог: ' + str(nal123) + ' руб.')
    st.write('Аренда: ' + str(ras123) + ' руб.')
    st.write('Расходы: ' + str(are123) + ' руб.')
    st.write('Кредит: ' + str(kre123) + ' руб.')

    with open('./txt/info.txt', 'a+', encoding = 'utf8') as file:
        if st.sidebar.button('Записать результат'):
            file.write(
                'Цена 1 килограмма плёнки для перчаток: ' + str(yb12) + ' руб.' '\n' '\n'
                'Вес одной пары перчаток: ' + str(zb312) + ' гр.' '\n' '\n'
                'Себестоимость перчаток: ' + str(ob412812) + ' руб.' '\n' '\n'
                #'Константы ' + str(X) + '' '\n' '\n'
                'Продажа: ' + str(nakk212) + ' руб.' '\n'
                'Пpибыль: ' + str(proc123) + ' руб.' '\n'
                'Офис: ' + str(ofi123) + ' руб.' '\n'
                'Расходы: ' + str(nal123) + ' руб.' '\n'
                'Аренда: ' + str(ras123) + ' руб.' '\n'
                'Пpибыль: ' + str(are123) + ' руб.' '\n'
                'Кредит: ' + str(kre123) + ' руб.' '\n' '\n'
                )

    with open('./txt/info.txt', 'r', encoding = 'utf8') as my_file:
        st.sidebar.download_button(label = 'Скачать результат',
        data = my_file, file_name = 'rinfo.txt',
        mime = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

if __name__ == "__main__":
    perchatki()