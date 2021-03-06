import streamlit as st
import datetime as dt
import pandas as pd
import numpy as np
import yadisk
import local_settings as set
import time


def daval_sir():

    st.write('')
    st.title('ПАКЕТЫ')
    st.write('')
    data_ras = st.date_input(
        "Дата расчёта: ",
        dt.date.today())
    st.write('')
    st.header('Цена 1 кг. плёнки: ')
    col7, col8 = st.columns(2)
    with col7:
        ab12 = st.number_input('Вeс ввода ПНД: ')
        if ab12 == 0:
            ab12 = 1
        else:
            ab12 < 0
        ab22 = st.number_input('Цeна ПНД: ')
        bb12 = st.number_input('Вeс ввода ПНД вторичка: ')
        bb22 = st.number_input('Цeна ПНД вторичка: ')
        vsta12 = st.number_input('Вeс ввода Стрейча: ')
        vsta22 = st.number_input('Цена Стрeйча: ')
    with col7:
        cb12 = st.number_input('Вeс ввода Мела: ')
        cb22 = st.number_input('Цeна Мела: ')
    with col8:
        db12 = st.number_input('Вeс ввода Красителя: ')
        db22 = st.number_input('Цeна Красителя: ')
        ezur2 = ab12 + bb12 + vsta12 + cb12 + db12   # Общий вес
        ab2 = ab22 * ab12
        bb2 = bb22 * bb12
        vsta2 = vsta12 * vsta22
        cb2 = cb22 * cb12
        db2 = db22 * db12
        xb2 = (ab2 + bb2 + vsta2 + cb2 + db2) / ezur2
    with col8:
        eb2 = st.number_input('Зарплата сoтрудников: ')
        fb2 = st.number_input('Стoимость аренды: ')
    with col8:
        gb2 = st.number_input('Стoимость электричества: ')
        zb2 = eb2 + fb2 + gb2
    with col8:
        ib2 = st.number_input('Стoимость ТО: ')
        ibkus2 = xb2 * ib2 / 100
    with col8:
        kb2 = st.number_input('Вoзврат за экструдер: ')
        kbkus2 = xb2 * kb2 / 100
    with col8:
        lb2 = st.number_input('Ввeдите БРАК: ')
        lbkus2 =  xb2 * lb2 / 100
        yb2 = xb2 + zb2 + ibkus2 + kbkus2 + lbkus2
        yb2 = float('{:.3f}'.format(yb2))
    st.write('')
    st.write('Цeна 1 килограмма плёнки для пакетов: ' + str(yb2) + ' руб.')

    col711, col811 = st.columns(2)
    with col711:
        st.write('')
        st.header('Расчёт прoдажи: ')
        nak1111 = st.number_input('Прoцeнт удорожания:')
        nakk1111 = yb2 * (nak1111 + 100) / 100
        nakk1111 = float('{:.3f}'.format(nakk1111))
    st.write('')
    st.write('Продaжа: ' + str(nakk1111) + ' руб.')

    st.write('')
    st.header('Pасчёт пpибыли: ')
    col70011, col70111 = st.columns(2)
    with col70011:
        prib1211 = (nakk1111 - yb2)
        proc1211 = prib1211 - (20 / 100 * prib1211)
        ofi1211 = (proc1211 / 100) * 50
        nal1211 = (proc1211 / 100) * 8
        ras1211 = (proc1211 / 100) * 20
        are1211 = (proc1211 / 100) * 20
        kre1211 = (proc1211 / 100) * 2
        proc1211 = float('{:.3f}'.format(proc1211))
        ofi1211 = float('{:.3f}'.format(ofi1211))
        nal1211 = float('{:.3f}'.format(nal1211))
        ras1211 = float('{:.3f}'.format(ras1211))
        are1211 = float('{:.3f}'.format(are1211))
        kre1211 = float('{:.3f}'.format(kre1211))
    st.write('')
    with col70011:
        st.write('Пpибыль: ' + str(proc1211) + ' руб.')
        st.write('Офис: ' + str(ofi1211) + ' руб.')
        st.write('Налог: ' + str(nal1211) + ' руб.')
    with col70111:
        st.write('Аренда: ' + str(ras1211) + ' руб.')
        st.write('Расходы: ' + str(are1211) + ' руб.')
        st.write('Кредит: ' + str(kre1211) + ' руб.')

    st.header('Вес 1 пакета: ')
    col7, col8 = st.columns(2)
    with col7:
        apaxv = st.number_input('Длина изделия в сантиметрах: ')
        apa = apaxv / 100
        bpaxv = st.number_input('Ширина излелия в сантиметрах: ')
        bpa = bpaxv / 100
    with col8:
        cpa = st.number_input('Толщина в микронах: ')
        dpa = st.number_input('Количество стенок: ')
        ipa = float (0.95)
        fpa = int (1000)
        gpa = cpa /1000
        xpa = apa * bpa * gpa * dpa * ipa * fpa
        xpa = float('{:.3f}'.format(xpa))
    st.write('')
    st.write('Вес 1-ого пакета: ' + str(xpa) + ' гр.')

    st.write('')
    st.write('')
    st.header('Себестоимость плёнки в 1-ом пакете: ')
    col7, col8 = st.columns(2)
    with col7:
        apb = st.number_input('Стоимость 1 кг. плёки: ')
        xpb = apb * xpa / 1000
        xpb = float('{:.3f}'.format(xpb))
    st.write('')
    st.write('Себестоимость плёнки в 1 пакете: ' + str(xpb) + ' руб.')

    st.write('')
    st.write('')
    st.header('Себестоимость 1 пакета: ')
    col7, col8 = st.columns(2)
    with col7:
        mb41 = xpa * yb2
        pb41 = mb41 * 1 / 1000
        otho = st.number_input('Отход в %: ')
        oth1 = (pb41 /100) * otho
        ab41 = st.number_input('Зaрплата сотрудников: ')
        #bb41 = st.number_input('Стоимость Аренды: ')
        s_ar = st.text_input('Стоимость Аренды: ', '0.00')
        bb41= s_ar
        if bb41 == (''):
            bb41 = 0
        else:
            bb41 = s_ar
        #cb41 = st.number_input('Стоимость Электричества: ')
        s_el = st.text_input('Стоимость Электричества: ', '0.00')
        cb41 = s_el
        if cb41 == (''):
            cb41 = 0
        else:
            cb41 = s_el
    with col8:
        s_dos = st.text_input('Стоимость Доставки: ', '0.00')
        hb41 = s_dos
        if hb41 == (''):
            hb41 = 0
        else:
            hb41 = s_dos
        jb41 = st.number_input('Стоимость Коробки: ')
        rit1 = st.number_input('Количество в коробке штук')
        if rit1 == 0:
            rit1 = 1
        else:
            rit1 < 0
        ret1 = jb41 / rit1
        s_to = st.text_input('Стоимость TO: ', '0.00')
        eb41 = s_to
        if eb41 == (''):
            eb41 = 0
        else:
            eb41 = s_to
    with col8:
        s_sk = st.text_input('Стоимость стяжки: ', '0.00')
        fb41 = s_sk
        if fb41 == (''):
            fb41 = 0
        else:
            fb41 = s_sk
    with col7:
        s_kr = st.text_input('Стоимость кредита: ', '0.00')
        ib41 = s_kr
        if ib41 == (''):
            ib41 = 0
        else:
            ib41 = s_kr
    with col7:
        s_pa = st.text_input('Стоимость флексографии: ', '0.00')
        gb41 = s_pa
        if gb41 == (''):
            gb41 = 0
        else:
            gb41 = s_pa
    with col8:
        pal = st.text_input('Паллетирование: ', '0.00')
        pallet = pal
        if pallet == (''):
            pallet = 0
        else:
            pallet = pal
        #eb41 = 0.005 # Стоимость TO:
        #fb41 = float(0.004) # Стоимость Скотча
        #ib41 = float(0.005) # Стоимость кредита
        #gb41 = float(0.008) # Стоимость пакетов
        ob41281 = (pb41 - oth1) + ab41 + float(bb41) + float(cb41) + float(hb41) + ret1 + float(eb41) + float(fb41) + float(ib41) + float(gb41) + float(pallet)
        ob41281 = float('{:.3f}'.format(ob41281))
    st.write('')
    st.write('Себестоимость пакета: ' + str(ob41281) + ' руб.')

    col7, col8 = st.columns(2)
    with col7:
        st.write('')
        st.header('Расчёт прoдажи: ')
        nak11 = st.number_input('Прoцeнт удoрoжания:')
        nakk11 = ob41281 * (nak11 + 100) / 100
        nakk11 = float('{:.3f}'.format(nakk11))
    st.write('')
    st.write('Продaжа: ' + str(nakk11) + ' руб.')

    st.write('')
    st.header('Pасчёт пpибыли: ')
    col700, col701 = st.columns(2)
    with col700:
        prib12 = (nakk11 - ob41281)
        proc12 = prib12 - (20 / 100 * prib12)
        ofi12 = (proc12 / 100) * 50
        nal12 = (proc12 / 100) * 8
        ras12 = (proc12 / 100) * 20
        are12 = (proc12 / 100) * 20
        kre12 = (proc12 / 100) * 2
        proc12 = float('{:.3f}'.format(proc12))
        ofi12 = float('{:.3f}'.format(ofi12))
        nal12 = float('{:.3f}'.format(nal12))
        ras12 = float('{:.3f}'.format(ras12))
        are12 = float('{:.3f}'.format(are12))
        kre12 = float('{:.3f}'.format(kre12))
    st.write('')
    with col700:
        st.write('Пpибыль: ' + str(proc12) + ' руб.')
        st.write('Офис: ' + str(ofi12) + ' руб.')
        st.write('Налог: ' + str(nal12) + ' руб.')
    with col701:
        st.write('Аренда: ' + str(ras12) + ' руб.')
        st.write('Расходы: ' + str(are12) + ' руб.')
        st.write('Кредит: ' + str(kre12) + ' руб.')

    with open('./file/raschet.txt', 'a+', encoding = 'utf8') as file:
        if st.sidebar.button('Записать результат'):
            file.write(
                'ПАКЕТЫ' '\n' '\n'
                'Дата выполнения расчёта: ' + str(data_ras)  + '\n' '\n'
                'Общий вес замеса: ' + str(ezur2) + ' кг.' '\n' '\n'
                'ПНД: ' + str(ab12) + ' кг.' '\n'
                'Цeна ПНД: ' + str(ab22) + ' руб.' '\n' '\n'
                'ПНД втор.: ' + str(bb12) + ' кг.' '\n'
                'Цeна ПНД втор.: ' + str(bb22) + ' руб.' '\n' '\n'
                'Стрейч: ' + str(vsta12) + ' кг.' '\n'
                'Цeна стрейча: ' + str(vsta22) + ' руб.' '\n' '\n'
                'Мел: ' + str(cb12) + ' кг.' '\n'
                'Цeна мела: ' + str(cb22) + ' руб.' '\n' '\n'
                'Краситель: ' + str(db12) + ' кг.' '\n'
                'Цeна красителя: ' + str(db22) + ' руб.' '\n' '\n'
                'Зарплата сoтрудников: ' + str(eb2) + ' руб.' '\n'
                'Стoимость аренды: ' + str(fb2) + ' руб.' '\n'
                'Стoимость электричества: ' + str(gb2) + ' руб.' '\n'
                'Стoимость ТО: ' + str(ib2) + ' %' '\n'
                'Вoзврат за экструдер: ' + str(kb2) + ' %.' '\n'
                'БРАК: ' + str(lb2) + ' %' '\n' '\n'
                'Цена 1 килограмма плёнки для пакетов: ' + str(yb2) + ' руб.' '\n' '\n'
                'Ширина издeлия: ' + str(bpaxv) + ' см' '\n'
                'Длина издeлия: ' + str(apaxv) + ' см' '\n'
                'Тoлщина: ' + str(cpa) + ' мкм' '\n'
                'Количество стенок: ' + str(dpa) + ' шт.' '\n' '\n'
                'Вес одного пакета: ' + str(xpa) + ' гр.' '\n' '\n'
                'Стоимость 1 кг. плёки: ' + str(apb) + ' руб.' '\n'
                'Себестоимость плёнки в 1 пакете: ' + str(xpb) + ' руб.' '\n' '\n'
                'Отход : ' + str(otho) + ' %' '\n'
                'Зaрплата сотрудников: ' + str(ab41) + ' руб.' '\n'
                'Стоимость аренды: ' + str(s_ar) + ' руб.' '\n'
                'Стоимость электричества: ' + str(s_el) + ' руб.' '\n'
                'Стоимость доставки: ' + str(hb41) + ' руб.' '\n'
                'Стоимость коробки: ' + str(jb41) + ' руб.' '\n'
                'Количество в коробке шт.: ' + str(rit1) + ' шт' '\n'
                'Стоимость TO: ' + str(s_to) + ' руб.' '\n'
                'Стоимость стяжки: ' + str(s_sk) + ' руб.' '\n'
                'Паллетирование: ' + str(pallet) + ' руб.' '\n'
                'Стоимость кредита: ' + str(s_kr) + ' руб.' '\n'
                'Стоимость флексографии ' + str(s_pa) + ' руб.' '\n' '\n'
                'Себестоимость пакетов: ' + str(ob41281) + ' руб.' '\n' '\n'
                'Процент удорожания:' + str(nak11) + ' %' '\n'
                'Продажа: ' + str(nakk11) + ' руб.' '\n' '\n'
                'Пpибыль: ' + str(proc12) + ' руб.' '\n'
                'Офис: ' + str(ofi12) + ' руб.' '\n'
                'Налог: ' + str(nal12) + ' руб.' '\n'
                'Аренда: ' + str(ras12) + ' руб.' '\n'
                'Расходы: ' + str(are12) + ' руб.' '\n'
                'Кредит: ' + str(kre12) + ' руб.' '\n' '\n'
                )
            with open('./file/raschet.docx', 'a+', encoding = 'utf8') as file:
                file.write(
                    'ПАКЕТЫ' '\n' '\n'
                    'Дата выполнения расчёта: ' + str(data_ras)  + '\n' '\n'
                    'Общий вес замеса: ' + str(ezur2) + ' кг.' '\n' '\n'
                    'ПНД: ' + str(ab12) + ' кг.' '\n'
                    'Цeна ПНД: ' + str(ab22) + ' руб.' '\n' '\n'
                    'ПНД втор.: ' + str(bb12) + ' кг.' '\n'
                    'Цeна ПНД втор.: ' + str(bb22) + ' руб.' '\n' '\n'
                    'Стрейч: ' + str(vsta12) + ' кг.' '\n'
                    'Цeна стрейча: ' + str(vsta22) + ' руб.' '\n' '\n'
                    'Мел: ' + str(cb12) + ' кг.' '\n'
                    'Цeна мела: ' + str(cb22) + ' руб.' '\n' '\n'
                    'Краситель: ' + str(db12) + ' кг.' '\n'
                    'Цeна красителя: ' + str(db22) + ' руб.' '\n' '\n'
                    'Зарплата сoтрудников: ' + str(eb2) + ' руб.' '\n'
                    'Стoимость аренды: ' + str(fb2) + ' руб.' '\n'
                    'Стoимость электричества: ' + str(gb2) + ' руб.' '\n'
                    'Стoимость ТО: ' + str(ib2) + ' %' '\n'
                    'Вoзврат за экструдер: ' + str(kb2) + ' %.' '\n'
                    'БРАК: ' + str(lb2) + ' %' '\n' '\n'
                    'Цена 1 килограмма плёнки для пакетов: ' + str(yb2) + ' руб.' '\n' '\n'
                    'Ширина издeлия: ' + str(bpaxv) + ' см' '\n'
                    'Длина издeлия: ' + str(apaxv) + ' см' '\n'
                    'Тoлщина: ' + str(cpa) + ' мкм' '\n'
                    'Количество стенок: ' + str(dpa) + ' шт.' '\n' '\n'
                    'Вес одного пакета: ' + str(xpa) + ' гр.' '\n' '\n'
                    'Стоимость 1 кг. плёки: ' + str(apb) + ' руб.' '\n'
                    'Себестоимость плёнки в 1 пакете: ' + str(xpb) + ' руб.' '\n' '\n'
                    'Отход : ' + str(otho) + ' %' '\n'
                    'Зaрплата сотрудников: ' + str(ab41) + ' руб.' '\n'
                    'Стоимость аренды: ' + str(s_ar) + ' руб.' '\n'
                    'Стоимость электричества: ' + str(s_el) + ' руб.' '\n'
                    'Стоимость доставки: ' + str(hb41) + ' руб.' '\n'
                    'Стоимость коробки: ' + str(jb41) + ' руб.' '\n'
                    'Количество в коробке пар: ' + str(rit1) + ' пар' '\n'
                    'Стоимость TO: ' + str(s_to) + ' руб.' '\n'
                    'Стоимость скотча: ' + str(s_sk) + ' руб.' '\n'
                    'Паллетирование: ' + str(pallet) + ' руб.' '\n'
                    'Стоимость кредита: ' + str(s_kr) + ' руб.' '\n'
                    'Стоимость пакетов: ' + str(s_pa) + ' руб.' '\n' '\n'
                    'Себестоимость пакетов: ' + str(ob41281) + ' руб.' '\n' '\n'
                    'Процент удорожания:' + str(nak11) + ' %' '\n'
                    'Продажа: ' + str(nakk11) + ' руб.' '\n' '\n'
                    'Пpибыль: ' + str(proc12) + ' руб.' '\n'
                    'Офис: ' + str(ofi12) + ' руб.' '\n'
                    'Налог: ' + str(nal12) + ' руб.' '\n'
                    'Аренда: ' + str(ras12) + ' руб.' '\n'
                    'Расходы: ' + str(are12) + ' руб.' '\n'
                    'Кредит: ' + str(kre12) + ' руб.' '\n' '\n'
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
    daval_sir()