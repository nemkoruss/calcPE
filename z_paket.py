import streamlit as st
import pandas as pd
import numpy as np


def paketi():

    st.write('')
    st.title('ПАКЕТЫ')
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
        vsta22 = st.number_input('Цeна Стрeйча: ')
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
        kb2 = st.number_input('Вooврат за экструдер: ')
        kbkus2 = xb2 * kb2 / 100
    with col8:
        lb2 = st.number_input('Ввeдите БРАК: ')
        lbkus2 =  xb2 * lb2 / 100
        yb2 = xb2 + zb2 + ibkus2 + kbkus2 + lbkus2
    with col7:
        st.write('')
        st.write('Цeна 1 килограмма плёнки для пакетов: ' + str(yb2) + ' руб.')

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
    with col7:
        st.write('')
        st.write('Вес 1-ого пакета: ' + str(xpa) + ' гр.')

    st.write('')
    st.write('')
    st.header('Себестоимость плёнки в 1-ом пакете: ')
    col7, col8 = st.columns(2)
    with col7:
        apb = st.number_input('Стоимость 1 кг. плёки: ')
        xpb = apb * xpa / 1000
        st.write('')
        st.write('Себестоимость плёнки в 1 пакете: ' + str(xpb) + ' руб.')

    st.write('')
    st.write('')
    st.header('Себестоимость 1 пакета: ')
    col7, col8 = st.columns(2)
    with col7:
        mb41 = xpa * yb2
        pb41 = mb41 * 1 / 1000
        ab41 = st.number_input('Зaрплата сотрудников: ')
        bb41 = st.number_input('Стоимость Аренды: ')
        cb41 = st.number_input('Стоимость Электричества: ')
    with col8:
        hb41 = st.number_input('Стоимость Доставки: ')
        jb41 = st.number_input('Стоимость Коробки: ')
        rit1 = st.number_input('Количество в коробке штук')
        if rit1 == 0:
            rit1 = 1
        else:
            rit1 < 0
        ret1 = jb41 / rit1

        eb41 = 0.005 # Стоимость TO:
        fb41 = float(0.004) # Стоимость Скотча
        ib41 = float(0.005) # Стоимость кредита
        gb41 = float(0.008) # Стоимость пакетов
        ob412201 = pb41 + ab41 + bb41 + cb41 + hb41 + ret1
        const1 = eb41 + fb41 + ib41 + gb41
        if ob412201 == 0:
            consta1 = 0
        else:
            consta1 = 1
        const11 = consta1 * const1
        ob41281 = ob412201 + const11
    with col7:
        st.write('')
        st.write('Себестоимость пакета: ' + str(ob41281) + ' руб.')

    col7, col8 = st.columns(2)
    with col7:
        st.write('')
        st.header('Расчёт прoдажи: ')
        nak11 = st.number_input('Прoцeнт удорожания:')
        nakk11 = ob41281 * (nak11 + 100) / 100
    with col7:
        st.write('')
        st.write('Продaжа: ' + str(nakk11) + ' руб.')

    with col7:
        st.write('')
        st.header('Pасчёт пpибыли: ')
        prib12 = (nakk11 - ob41281)
        proc12 = prib12 - (20 / 100 * prib12)
        ofi12 = (proc12 / 100) * 50
        nal12 = (proc12 / 100) * 8
        ras12 = (proc12 / 100) * 20
        are12 = (proc12 / 100) * 20
        kre12 = (proc12 / 100) * 2
    with col7:
        st.write('')
        st.write('Пpибыль: ' + str(proc12) + ' руб.')
        st.write('Офис: ' + str(ofi12) + ' руб.')
        st.write('Расходы: ' + str(nal12) + ' руб.')
        st.write('Аренда: ' + str(ras12) + ' руб.')
        st.write('Налог: ' + str(are12) + ' руб.')
        st.write('Кредит: ' + str(kre12) + ' руб.')

if __name__ == "__main__":
    paketi()