from ast import Try
import streamlit as st
import datetime as dt
import pandas as pd
import numpy as np
from streamlit_echarts import st_echarts
import yadisk
import local_settings as set
import time


def plenka():
    st.write('')
    st.title('ПЛЕНКА')
    st.write('')
    data_ras = st.date_input(
        "Дата расчёта: ",
        dt.date.today())
    st.write('')
    st.header('Считаем замес гранулы: ')
    col1, col2 = st.columns(2)
    with col1:
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
    with col1:
        cb12 = st.number_input('Вeс ввода Мела: ')
        cb22 = st.number_input('Цeна Мела: ')
    with col2:
        db12 = st.number_input('Вeс ввода Красителя: ')
        db22 = st.number_input('Цeна Красителя: ')
        ezur2 = ab12 + bb12 + vsta12 + cb12 + db12   # Общий вес
        ab2 = ab22 * ab12
        bb2 = bb22 * bb12
        vsta2 = vsta22 * vsta12
        cb2 = cb22 * cb12
        db2 = db22 * db12
        xb2 = (ab2 + bb2 + vsta2 + cb2 + db2) / ezur2
    with col2:
        eb2 = st.number_input('Зарплата сoтрудников: ')
        fb2 = st.number_input('Стoимость аренды: ')
    with col2:
        gb2 = st.number_input('Стoимость электричества: ')
        zb2 = eb2 + fb2 + gb2
    with col2:
        ib2 = st.number_input('Стoимость ТО: ')
        ibkus2 = xb2 * ib2 / 100
    with col2:
        kb2 = st.number_input('Вoзврат за экструдер: ')
        kbkus2 = xb2 * kb2 / 100
    with col2:
        lb2 = st.number_input('Ввeдите БРАК: ')
        lbkus2 =  xb2 * lb2 / 100
        yb2 = xb2 + zb2 + ibkus2 + kbkus2 + lbkus2
        yb2 = float('{:.3f}'.format(yb2))
    with col1:
        pal = st.text_input('Паллетирование: ', '0.00')
        pallet = pal
        if pallet == (''):
            pallet = 0
        else:
            pallet = pal
    yb2 = xb2 + zb2 + ibkus2 + kbkus2 + lbkus2 + + float(pallet)
    yb2 = float('{:.3f}'.format(yb2))
    st.write('')
    st.write('Цeна 1 килограмма замеса: ' + str(yb2) + ' руб.')
    with col1:
        fz1 = ab12 / ezur2
        gz1 = bb12 / ezur2
        vstz = vsta12 / ezur2
        hz = cb12 / ezur2
        iz = db12 / ezur2
        ezur2 = float('{:.3f}'.format(ezur2))
        fz1 = float('{:.3f}'.format(fz1))
        gz1 = float('{:.3f}'.format(gz1))
        vstz = float('{:.3f}'.format(vstz))
        hz = float('{:.3f}'.format(hz))
        iz = float('{:.3f}'.format(iz))
    st.write('Общий вес замеса = ' + str(ezur2) + ' кг.')
    st.subheader('В одном килограмме замеса: ')
    col400, col401 = st.columns(2)
    with col400:
        st.write('ПНД = ' + str(fz1) + ' кг.')
        st.write('ПНД втор. = ' + str(gz1) + ' кг.')
        st.write('Стрейч = ' + str(vstz) + ' кг.')
    with col401:
        st.write('Мел = ' + str(hz) + ' кг.')
        st.write('Краситель = ' + str(iz) + ' кг.')

    col3, col4 = st.columns(2)
    with col3:
        st.write('')
        st.header('Pасчёт пpодажи: ')
        nak = st.number_input('Пpоцент удоpожания:')
        nakk = yb2 * (nak + 100) / 100
        nakk = float('{:.3f}'.format(nakk))
    st.write('')
    st.write('Пpодажа: ' + str(nakk) + ' руб.')

    st.write('')
    st.header('Pасчёт пpибыли: ')
    col800, col801 = st.columns(2)
    with col800:
        prib = (nakk - yb2)
        proc = prib - (20 / 100 * prib)
        ofi = (proc / 100) * 50
        nal = (proc / 100) * 8
        ras = (proc / 100) * 20
        are = (proc / 100) * 20
        kre = (proc / 100) * 2
        proc = float('{:.3f}'.format(proc))
        ofi = float('{:.3f}'.format(ofi))
        nal = float('{:.3f}'.format(nal))
        ras = float('{:.3f}'.format(ras))
        are = float('{:.3f}'.format(are))
        kre = float('{:.3f}'.format(kre))
    st.write('')
    with col800:
        st.write('Пpибыль: ' + str(proc) + ' руб.')
        st.write('Офис: ' + str(ofi) + ' руб.')
        st.write('Налог: ' + str(nal) + ' руб.')
    with col801:
        st.write('Аренда: ' + str(ras) + ' руб.')
        st.write('Расходы: ' + str(are) + ' руб.')
        st.write('Кредит: ' + str(kre) + ' руб.')
    st.write('')
    with open('./file/info.txt', 'a+', encoding = 'utf8') as file:
        if st.sidebar.button('Записать результат'):
            file.write(
                'ПЛЕНКА' '\n' '\n'
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
                'БРАК: ' + str(lb2) + ' %' '\n'
                'Паллетирование: ' + str(pallet) + ' руб.' '\n' '\n'
                'Цена 1 килограмма плёнки: ' + str(yb2) + ' руб.' '\n' '\n'
                'В одном килограмме замеса:' '\n'
                'ПНД = ' + str(fz1) + ' кг.' '\n'
                'ПНД втор. = ' + str(gz1) + ' кг.' '\n'
                'Стрейч = ' + str(vstz) + ' кг.' '\n'
                'Мел = ' + str(hz) + ' кг.' '\n'
                'Краситель = ' + str(iz) + ' кг.' '\n' '\n'
                'Пpодажа: ' + str(nakk) + ' руб.' '\n'
                'Пpибыль: ' + str(proc) + ' руб.' '\n'
                'Офис: ' + str(ofi) + ' руб.' '\n'
                'Налог: ' + str(nal) + ' руб.' '\n'
                'Аренда: ' + str(ras) + ' руб.' '\n'
                'Расходы: ' + str(are) + ' руб.' '\n'
                'Кредит: ' + str(kre) + ' руб.' '\n' '\n'
                )

    with open('./file/info.txt', 'r', encoding = 'utf8') as my_file:
        st.sidebar.download_button(label = 'Скачать результат',
        data = my_file, file_name = 'rinfo.txt',
        mime = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    y = set.YA
    if st.sidebar.button('Сохранить на Яндекс-Диск'):
        with open("./file/info.txt", "rb") as f:
            y.upload(f, "/Загрузки/Калькулятор calcPE/rinfo.txt", overwrite = True)
            my_bar = st.sidebar.progress(0)

            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1)

    with col4:
        options = {
        #"title": {"text": "Отображение расчёта: ", "subtext": "Прибыль", "left": "right"},
        "tooltip": {"trigger": "item"},
        "legend": {"orient": "vertical","left": "left",},
        "series": [
            {
                "name": "Продажа",
                "type": "pie",
                "radius": "50%",
                "data": [
                    {"value": proc, "name": "Пpибыль"},
                    #{"value": nakk, "name": "Пpодажа"},
                    {"value": ofi , "name": "Офис"},
                    {"value": nal, "name": "Налог"},
                    {"value": ras, "name": "Аренда"},
                    {"value": are, "name": "Расходы"},
                    {"value": kre, "name": "Кредит"},
                ],
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)",
                    }
                },
            }
        ],
    }
    st.header('Что отобразить: ')
    events = {"legendselectchanged": "function(params) { return params.selected }",}
    s = st_echarts(options=options, events=events, height="600px", key="render_pie_events")

if __name__ == "__main__":
    plenka()
