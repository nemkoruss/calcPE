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
        s_ar = st.text_input('Стоимость Аренды: ', '0.00')
        bb412= s_ar
        if bb412 == (''):
            bb412 = 0
        else:
            bb412 = s_ar
        s_el = st.text_input('Стоимость Электричества: ', '0.00')
        cb412= s_el
        if cb412 == (''):
            cb412 = 0
        else:
            cb412 = s_el
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
    #with col19:
    #    s_sk = st.text_input('Стоимость Скотча: ', '0.00')
    #    fb412 = s_sk
    #    if fb412 == (''):
    #        fb412 = 0
    #    else:
    #        fb412 = s_sk
    #with col20:
    #    s_kr = st.text_input('Стоимость кредита: ', '0.00')
    #    ib412 = s_kr
    #    if ib412 == (''):
    #        ib412 = 0
    #    else:
    #        ib412 = s_kr
    with col20:
        s_pa = st.text_input('Стоимость пакетов: ', '0.00')
        gb412 = s_pa
        if gb412 == (''):
            gb412 = 0
        else:
            gb412 = s_pa
        ob4122012 = (pb412 - oth) + ab412 + float(bb412) + float(cb412) + hb412 + ret12
        ob412812 = ob4122012 + float(eb412) + float(gb412) #+ float(fb412) + float(ib412)
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

    with open('./file/info.docx', 'a+', encoding = 'utf8') as file:
        if st.sidebar.button('Записать результат'):
            file.write(
                'Общий вес замеса: ' + str(ezur12) + ' кг.' '\n' '\n'
                'ПНД: ' + str(ab112) + ' кг.' '\n'
                'Цeна ПНД: ' + str(ab212) + ' руб.' '\n' '\n'
                'ПНД втор.: ' + str(bb112) + ' кг.' '\n'
                'Цeна ПНД втор.: ' + str(bb212) + ' руб.' '\n' '\n'
                'Стрейч: ' + str(vsta112) + ' кг.' '\n'
                'Цeна стрейча: ' + str(vsta212) + ' руб.' '\n' '\n'
                'Мел: ' + str(cb112) + ' кг.' '\n'
                'Цeна мела: ' + str(cb212) + ' руб.' '\n' '\n'
                'Краситель: ' + str(db112) + ' кг.' '\n'
                'Цeна красителя: ' + str(db212) + ' руб.' '\n' '\n'
                'Зарплата сoтрудников: ' + str(eb12) + ' руб.' '\n'
                'Стoимость аренды: ' + str(fb12) + ' руб.' '\n'
                'Стoимость электричества: ' + str(gb12) + ' руб.' '\n'
                'Стoимость ТО: ' + str(ib12) + ' %' '\n'
                'Вoзврат за экструдер: ' + str(kb12) + ' %.' '\n'
                'БРАК: ' + str(lb12) + ' %' '\n' '\n'
                'Цена 1 килограмма плёнки для перчаток: ' + str(yb12) + ' руб.' '\n' '\n'
                'Высота издeлия: ' + str(abusi12) + ' см' '\n'
                'Длина издeлия: ' + str(bbusi12) + ' см' '\n'
                'Тoлщина: ' + str(cb312) + ' мкм' '\n' '\n'
                'Вес одной пары перчаток: ' + str(zb312) + ' гр.' '\n' '\n'
                'Отход : ' + str(otho) + ' %' '\n'
                'Зaрплата сотрудников: ' + str(ab412) + ' руб.' '\n'
                'Стоимость аренды: ' + str(s_ar) + ' руб.' '\n'
                'Стоимость электричества: ' + str(s_el) + ' руб.' '\n'
                'Стоимость доставки: ' + str(hb412) + ' руб.' '\n'
                'Стоимость коробки: ' + str(jb412) + ' руб.' '\n'
                'Количество в коробке пар: ' + str(rit12) + ' пар' '\n'
                'Стоимость TO: ' + str(s_to) + ' руб.' '\n'
                #'Стоимость скотча: ' + str(s_sk) + ' руб.' '\n'
                #'Стоимость кредита: ' + str(s_kr) + ' руб.' '\n'
                'Стоимость пакетов: ' + str(s_pa) + ' руб.' '\n' '\n'
                'Себестоимость перчаток: ' + str(ob412812) + ' руб.' '\n' '\n'
                'Процент удорожания:' + str(nak212) + ' %' '\n'
                'Продажа: ' + str(nakk212) + ' руб.' '\n' '\n'
                'Пpибыль: ' + str(proc123) + ' руб.' '\n'
                'Офис: ' + str(ofi123) + ' руб.' '\n'
                'Налог: ' + str(nal123) + ' руб.' '\n'
                'Аренда: ' + str(ras123) + ' руб.' '\n'
                'Расходы: ' + str(are123) + ' руб.' '\n'
                'Кредит: ' + str(kre123) + ' руб.' '\n' '\n'
                )

    with open('./file/info.docx', 'r', encoding = 'utf8') as my_file:
        st.sidebar.download_button(label = 'Скачать результат',
        data = my_file, file_name = 'rinfo.docx',
        mime = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

if __name__ == "__main__":
    perchatki()


 #   with col19:
 #       const112 = 0
 #       agree = st.checkbox('Стоимость TO 0.005')
 #       if agree:
 #               const112 = float(eb412)
 #       elif agree:
 #           const112 = 0
 #   with col20:
 #      const113 = 0
 #       agreee = st.checkbox('Стоимость Скотча 0.004')
 #       if agreee:
 #               const113 = fb412
 #       elif agreee:
 #           const113 = 0
 #   with col19:
 #       const114 = 0
 #       agreee = st.checkbox('Стоимость кредита 0.005')
 #       if agreee:
 #               const114 = ib412
 #       elif agreee:
 #           const114 = 0
 #   with col20:
 #       const115 = 0
 #       agreee = st.checkbox('Стоимость пакетов 0.008')
 #       if agreee:
 #               const115 = gb412
 #       elif agreee:
 #           const115 = 0
 #       ob412812 = ob4122012 + const112 + const113 + const114 + const115

