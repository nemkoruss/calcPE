import streamlit as st
import datetime as dt
import pandas as pd
import numpy as np

def individualka():

    st.write('')
    st.title('ИНДИВИДУАЛЬНАЯ УПАКОВКА')
    st.write('')
    data_ras = st.date_input(
        "Дата расчёта: ",
        dt.date.today())
    st.write('')
    st.header('Себестоимость упаковки: ')
    col123, col124 = st.columns(2)
    with col123:
        v_ip = st.text_input('Вес упаковки: ', '0.00')
        v_up = v_ip
        if v_up == (''):
            v_up = 0
        else:
            v_up = v_ip
        s_ip = st.text_input('Стоимость 1 кг. упаковочной плёнки: ', '0.00')
        s_up = s_ip
        if s_up == (''):
            s_up = 0
        else:
            s_up = s_ip
        zup = ((float(v_up) * float(s_up)) / 100 ) * 1
        up = float(zup) * 100
        a_ip = st.text_input('Аренда: ', '0.00')
        a_up = a_ip
        if a_up == (''):
            a_up = 0
        else:
                a_up = a_ip
        e_ip = st.text_input('Электричество: ', '0.00')
        e_up = e_ip
        if e_up == (''):
            e_up = 0
        else:
            e_up = e_ip
    with col124:
        t_ip = st.text_input('ТО: ', '0.00')
        t_up = t_ip
        if t_up == (''):
            t_up = 0
        else:
            t_up = t_ip
        r_ip = st.text_input('Работа: ', '0.00')
        r_up = r_ip
        if r_up == (''):
            r_up = 0
        else:
            r_up = r_ip
        q_ip = st.text_input('Этикетка: ', '0.00')
        q_up = q_ip
        if q_up == (''):
            q_up = 0
        else:
            q_up = q_ip
        d_ip = st.text_input('Доставка: ', '0.00')
        d_up = d_ip
        if d_up == (''):
            d_up = 0
        else:
            d_up = d_ip
        iup =  float(up) + float(a_up) + float(e_up) + float(t_up) + float(r_up) + float(q_up) + float(d_up)
    iup = float('{:.3f}'.format(iup))
    st.write('Себестоимость упаковки: ' + str(iup) + ' руб.')
    st.write('')
    st.header('Себестоимость изделия в инд. упак.: ')
    col125, col126 = st.columns(2)
    with col125:
        s_ui = st.text_input('Себестоимость упаковываемой продукции: ', '0.00')
        qe_up = s_ui
        if qe_up == (''):
            qe_up = 0
        else:
            qe_up = s_ui
    with col125:
        pal = st.text_input('Паллетирование: ', '0.00')
        pallet = pal
        if pallet == (''):
            pallet = 0
        else:
            pallet = pal
    with col126:
        k_ui = st.text_input('Количество продукции в упаковке: ', '0.00')
        qw_up = k_ui
        if qw_up == (''):
            qw_up = 0
        else:
            qw_up = k_ui
        vi_iup = (float(s_ui) * float(k_ui)) + float(iup) + float(pallet)
    vi_iup = float('{:.3f}'.format(vi_iup))
    st.write('Себестоимость изделия в инд. упак.: ' + str(vi_iup) + ' руб.')

    col13, col14 = st.columns(2)
    with col13:
        st.write('')
        st.header('Расчёт продажи: ')
        nak2 = st.number_input('Процент удорожания:')
        nakk2 = vi_iup * (nak2 + 100) / 100
        nakk2 = float('{:.3f}'.format(nakk2))
    nakk2 = float('{:.3f}'.format(nakk2))
    st.write('Продажа: ' + str(nakk2) + ' руб.')

    st.write('')
    st.header('Pасчёт пpибыли: ')
    col800, col801 = st.columns(2)
    with col800:
        prib1 = (nakk2 - vi_iup)
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

    with open('./file/info.txt', 'a+', encoding = 'utf8') as file:
        if st.sidebar.button('Записать результат'):
            file.write(
                'Индивидуальная упаковка' '\n' '\n'
                'Дата выполнения расчёта: ' + str(data_ras)  + '\n' '\n'
                'Вес упаковки: ' + str(v_ip) + ' кг.' '\n'
                'Стоимость 1 кг. упаковочной плёнки: ' + str(s_ip) + ' руб.' '\n'
                'Зарплата сoтрудников: ' + str(r_ip) + ' руб.' '\n'
                'Стoимость аренды: ' + str(a_ip) + ' руб.' '\n'
                'Стoимость электричества: ' + str(e_ip) + ' руб.' '\n'
                'Стoимость ТО: ' + str(t_ip) + ' %' '\n'
                'Доставка: ' + str(d_ip) + ' %' '\n'
                'Этикетка: ' + str(q_ip) + ' руб.' '\n' '\n'
                'Себестоимость упаковки: ' + str(iup) + ' руб.' '\n' '\n'
                'Себестоимость изделия в инд. упак.: ' + str(vi_iup) + ' руб.' '\n' '\n'
                'Процент удорожания:' + str(nak2) + ' %' '\n'
                'Продажа: ' + str(nakk2) + ' руб.' '\n' '\n'
                'Пpибыль: ' + str(proc1) + ' руб.' '\n'
                'Офис: ' + str(ofi1) + ' руб.' '\n'
                'Налог: ' + str(nal1) + ' руб.' '\n'
                'Аренда: ' + str(ras1) + ' руб.' '\n'
                'Расходы: ' + str(are1) + ' руб.' '\n'
                'Кредит: ' + str(kre1) + ' руб.' '\n' '\n'
                )

    with open('./file/info.txt', 'r', encoding = 'utf8') as my_file:
        st.sidebar.download_button(label = 'Скачать результат',
        data = my_file, file_name = 'rinfo.txt',
        mime = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

if __name__ == "__main__":
    individualka()
