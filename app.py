import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

#-----------------------------------------------------------------

a = st.sidebar.radio('ВКЛ/ВЫКЛ "ВВЕДЕНИЕ":', ['Включено','Выключено'])

if a == 'Включено':
    
    st.subheader('Для работы калькулятора выберите в боковом меню нужный расчёт !')
    st.markdown('*Для входа в боковое меню на устройстве с маленьким экраном нажмите, в левом вверхнем углу, значок в виде стрелки  ">"*')
    st.markdown('*Для более комфортной работы, не забывайте "Очищать экран"  *')
    st.write('')
    st.header('Информация:')
    st.markdown('**Корпоративный сайт: ** [tpkpromed.ru](https://tpkpromed.ru)')
    st.markdown('**Производство бахил: ** [bioinvn.ru](https://bioinvn.ru)')
    st.markdown('**Интернет магазин: ** [pmpsale.ru](https://pmpsale.ru)')  
    st.markdown('**Скачать приложение: ** [Скачать](https://goo.su/RH7qQ)')
    image = Image.open('./qrcode/qrcode.jpg')
    st.image(image, width = 100, caption='QR код для скачивания',use_column_width=100)
    st.set_page_config(
         page_title="Ex-stream-ly Cool App",
         page_icon="🧊",
         layout="wide",
         initial_sidebar_state="expanded",
         menu_items={
             'Get Help': 'https://www.extremelycoolapp.com/help',
             'Report a bug': "https://www.extremelycoolapp.com/bug",
             'About': "# This is a header. This is an *extremely* cool app!"
         }
     )
    

#-----------------------------------------------------------------

b = st.sidebar.selectbox('РАСЧЁТ ПЛЕНКИ:', ['Выбрать/Очистить','Замес гранулы'])

if b == 'Замес гранулы':
    
    st.write('')
    st.title('ПЛЕНКА')
    st.write('')
    st.title('Считаем замес гранулы: ')
    col1, col2 = st.beta_columns(2)
    with col1:
        az = st.number_input('Вес ввода ПНД: ')    
        bz = st.number_input('Вес ввода ПНД втор.: ')
        vst = st.number_input('Вес ввода Стрейча: ')
    with col2:
        cz = st.number_input('Вес ввода Мела: ')
        dz = st.number_input('Вес ввода Красителя: ')
        ez = az + bz + vst + cz + dz  # Общий вес
        if ez == 0:
            ez = 1
        else:
            ez < 0
        fz1 = az / ez
        gz1 = bz / ez
        vstz = vst / ez
        hz = cz / ez
        iz = dz / ez
    st.write('Общий вес замеса = ' + str(ez) + ' кг.')    
    st.write('В одном килограмме замеса: ')
    st.write('ПНД = ' + str(fz1) + ' кг.')
    st.write('ПНД втор. = ' + str(gz1) + ' кг.')
    st.write('Стрейч = ' + str(vstz) + ' кг.')
    st.write('Мел = ' + str(hz) + ' кг.')
    st.write('Краситель = ' + str(iz) + ' кг.')
    
    st.title('Себес. замеса грaнулы: ')
    col3, col4 = st.beta_columns(2)
    with col3:
        az1 = st.number_input('Цена ПНД: ')
        bz1 = st.number_input('Цена ПНД вторичка: ')
        vst1 = st.number_input('Цена Стрейча: ')
    with col3:
        cz1 = st.number_input('Цена Мела: ')
        dz1 = st.number_input('Ценa Красителя: ')        
    az2 = az1 * az
    bz2 = bz1 * bz
    vst2 = vst1 * vst
    cz2 = cz1 * cz
    dz2 = dz1 * dz
    xz = az2 + bz2 + vst2 + cz2 + dz2
    with col3:    
        ez1 = st.number_input('Зарплатa сотрудников: ')
        fz = st.number_input('Стоимость аренды: ')
        gz = st.number_input('Стоимость электричества: ')       
    zz = ez1 + fz + gz      
    with col4:             
        iz = st.number_input('Стоимость ТО: ')
    iz = xz * iz / 100    
    with col4:             
        kz = st.number_input('Возврат за экструдер: ')
    kz = xz * kz / 100
    with col4:    
        lz = st.number_input('Введите БРАК: ')
    lz =   xz * lz / 100       
    yz = xz + zz + iz + kz + lz
    yzar = yz / ez
    st.write('Себестоимость замеса гранулы: ' + str(yzar) + ' руб.')
    
    col31, col41 = st.beta_columns(2)
    with col31:
        st.write('')
        st.title('Pасчёт пpодажи: ')
        nak = st.number_input('Пpоцент удоpожания:')
    nakk = yzar * (nak + 100) / 100
    with col31:
        st.write('Пpодажа: ' + str(nakk) + ' руб.') 

#-----------------------------------------------------------------   

x = st.sidebar.selectbox('РАСЧЁТ ПРОДУКЦИИ:', ['Выбрать/Очистить','Пакеты','Бахилы','Перчатки'])

if x == "Пакеты":
    st.write('')
    st.title ('ПАКЕТЫ')
    st.write('')
    st.title('Вес 1 пакета: ')
    col7, col8 = st.beta_columns(2)
    with col7:
        apa = st.number_input('Длина изделия в метрах: ')
        bpa = st.number_input('Ширина излелия в метрах: ')
    with col8:
        cpa = st.number_input('Толщина в микронах: ')
        dpa = st.number_input('Количество стенок: ')
    ipa = float (0.95)
    fpa = int (1000)
    gpa = cpa /1000
    xpa = apa * bpa * gpa * dpa * ipa * fpa
    st.write('Вес 1-ого пакета: ' + str(xpa) + ' гр.')

    st.write('')
    st.write('')
    st.title('Себестоимость плёнки в 1-ом пакете: ')
    col7, col8 = st.beta_columns(2)
    with col7:
        apb = st.number_input('Стоимость 1 кг. плёки: ')
    xpb = apb * xpa / 1000   
    st.write('Себестоимость плёнки в 1 пакете: ' + str(xpb) + ' руб.')
    
    st.write('')
    st.write('')
    st.title('Себестоимость 1 пакета: ')
    col7, col8 = st.beta_columns(2)
    with col7:
        apc = st.number_input('Стоимость работы сотрудника: ')
        apd = st.number_input('Стоимость Аренды: ')
        ape = st.number_input('Стоимость Электричества: ')
    with col8:    
        apf = st.number_input('Стoимость ТО: ')
        apg = st.number_input('Стоимость Доставки: ')
        aph = st.number_input('Стоимость Упаковки: ')
    with col7:
        api = st.number_input('Стоимость Коробки: ')
    xpc = xpb + apc + apd + ape + apf + apg + aph + api
    st.write('Себестоимость 1 пакета: ' + str(xpc) + ' руб.') 
    col7, col8 = st.beta_columns(2)
    with col7:
        st.write('')
        st.title('Расчёт прoдажи: ')
        nak1 = st.number_input('Прoцeнт удорожания:')
    nakk1 = xpc * (nak1 + 100) / 100
    with col7:
        st.write('Продaжа: ' + str(nakk1) + ' руб.')  

#------------------------     

elif x == "Бахилы":
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
    xb = ab + bb + vsta + cb + db        
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
    ybur = yb / ezur 
    if ybur == 0:
        ybur = 1
    else:
        ybur < 0     
    st.write('Цена 1 килограмма плёнки для бахил: ' + str(ybur) + ' руб.')

    st.title('Вeс одной пары бахил: ')
    col11, col12 = st.beta_columns(2)
    with col11:
        ab3 = st.number_input('Высота издeлия в метрах: ')
    with col11:    
        bb3 = st.number_input('Длина издeлия в метрах: ')
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
        mb4 = zb3 * ybur
        pb4 = mb4 * 1 /100
        ab4 = st.number_input('Зaрплата сотрудников: ')
        bb4 = st.number_input('Стоимость Аренды: ')
        cb4 = st.number_input('Стоимость Электричества: ')
        eb4 = st.number_input('Стоимость TO: ')
        
        fb4 = st.number_input('Стоимость Скотча: ')
        
    with col13:    
        gb4 = st.number_input('Стоимость Пакетов: ')
        
        hb4 = st.number_input('Стоимость Доставки: ')
        ib4 = st.number_input('Стоимость Кредита: ')
    
        jb4 = st.number_input('Стоимость Коробки: ')
        
    ob41 = pb4 + ab4 + bb4 + cb4 + eb4 + fb4 + gb4 + hb4 + ib4 + jb4
    with col14:
        kb41 = st.number_input('Стоимость Резинки: ')
    kb4 = kb41 * 1 / 100
    with col14:
        lb4 = st.number_input('Количество резинок [1 или 2]: ')
    if lb4 == '1':
        tb4 = float (kb4 * 1)            

    elif lb4 == '2':
        tb4 = float (kb4 * 2)            

    ob4 = kb4 * lb4
    zb4 = ob41 + ob4
    st.write('Себестоимость бахил: ' + str(zb4) + ' руб.')
    col13, col14 = st.beta_columns(2)
    with col13:
        st.write('')
        st.title('Расчёт продажи: ')
        nak2 = st.number_input('Процент удорожания:')
    nakk2 = zb4 * (nak2 + 100) / 100
    with col13:
        st.write('Продажа: ' + str(nakk2) + ' руб.')
        
#-------------------------
    
elif x == "Перчатки":
    st.write('')
    st.title('ПЕРЧАТКИ')
    st.write('')
    st.title('Цена 1 кг. плёнки: ')
    col15, col16 = st.beta_columns(2)
    with col15:
        ape1 = st.number_input('Вес ввoда ПНД: ')
        ape2 = st.number_input('Цeна ПНД: ')
        bpe1 = st.number_input('Вeс ввода ПНД вторичка: ')
        bpe2 = st.number_input('Цeна ПНД вторичка: ')
        vste1 = st.number_input('Вeс ввода Стрейча: ')
        vste2 = st.number_input('Цена Стрeйча: ')
    with col16:    
        cpe1 = st.number_input('Вeс ввода Мела: ')
        cpe2 = st.number_input('Цeна Мела: ')
        dpe1 = st.number_input('Вeс ввода Красителя: ')
        dpe2 = st.number_input('Цeна Красителя: ')
    ape = ape2 * ape1
    bpe = bpe2 * bpe1
    vste = vste1 * vste2
    cpe = cpe2 * cpe1
    dpe = dpe2 * dpe1
    xpe = ape + bpe + vste + cpe + dpe
    with col16:    
        epe = st.number_input('Зарплата сoтрудников: ')
        fpe = st.number_input('Стoимость аренды: ')
    with col15:
        gpe = st.number_input('Стoимость электричества: ')
        hpe = st.number_input('Стоимoсть кредита: ')        
    wpe = epe + fpe + gpe + hpe
    with col16:                   
        ipe = st.number_input('Стоимoсть ТО: ')
    ipe = xpe * ipe / 100
    with col16:              
        kpe = st.number_input('Вoзврат за экструдер: ')
    kpe = xpe * kpe / 100
    with col15:           
        lpe = st.number_input('Ввeдите БРАК: ')
    lpe =   xpe * lpe / 100

    ype = xpe + wpe + ipe + kpe + lpe        
    st.write('Цена 1 килограмма плёнки для перчаток: ' + str(ype) + ' руб.')
        
    st.title('Вес одной пары перчаток: ')
    col17, col18 = st.beta_columns(2)
    with col17:
        ape3 = st.number_input('Высота изделия в метрах: ')
    with col18:    
        bpe3 = st.number_input('Длина излелия в метрах: ')
    with col17:
        cpe3 = st.number_input('Толщина в микронах: ')
    dpe3 = int (2)
    ipe3 = float (0.95)
    gpe3 = cpe3 / 1000
    fpe3 = int (1000)
    zpe3 = ape3 * bpe3 * gpe3 * dpe3 * ipe3 * fpe3        
    st.write('Вес одной пары перчаток: ' + str(zpe3) + ' кг.')

    st.title('Себестоимость перчаток: ')
    col19, col20 = st.beta_columns(2)
    mpe4 = zpe3 * ype
    ppe4 = mpe4 * 1 /100
    with col19:
        ape4 = st.number_input('Зарплaтa сотрудников: ')
        bpe4 = st.number_input('Стоимость Арeнды: ')
        cpe4 = st.number_input('Стоимость Элeктричества: ')
        dpe4 = st.number_input('Стоимость Вoзврата электричества: ')
        epe4 = st.number_input('Стоимость ТO: ')
    with col20:    
        fpe4 = st.number_input('Стоимость Скoтча: ')
        gpe4 = st.number_input('Стоимость Пакетoв: ')
        hpe4 = st.number_input('Стоимость Дoставки: ')
        ipe4 = st.number_input('Стоимость Крeдита: ')
        jpe41 = st.number_input('Стоимость Корoбки: ')
    jpe4 = jpe41 * 1 / 100
    ope4 = ppe4 + ape4 + bpe4 + cpe4 + dpe4 + epe4 + fpe4 + gpe4 + hpe4 + ipe4 + jpe4        
    st.write('Себестоимость перчаток: ' + str(ope4) + ' руб.')
    col19, col20 = st.beta_columns(2)
    with col19:
        st.write('')
        st.title('Pacчёт пpoдaжи: ')
        nak3 = st.number_input('Пpoцент удopoжaния:')
    nakk3 = ope4 * (nak3 + 100) / 100
    with col19:
        st.write('Пpoдaжa: ' + str(nakk3) + ' руб.')
        
#----------------------------------------------------------------

y = st.sidebar.selectbox('РАСЧЁТ ЗАКАЗА:', ['Выбрать/Очистить','Заказ на бахилы','Заказ на пленку', 'Заказ на пакеты','Заказ на перчатки'])

if y == "Заказ на бахилы":
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

#---------------------------

if y == "Заказ на пленку":
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

#---------------------------

if y == "Заказ на пакеты":
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

#--------------------------

if y == "Заказ на перчатки":
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

#-----------------------------------------------------------------

z = st.sidebar.selectbox('РАСЧЁТ ВЫПЛАТ:', ['Выбрать/Очистить','Цех бахил','Цех экструзии', 'Цех перчатки','Цех пакеты',])

if z == "Цех бахил":
    st.write('')
    st.title('ЗП БАХИЛЫ')
    st.write('')
    st.title('Ставка: ')
    col230, col240 = st.beta_columns(2)
    with col230:
        za = st.number_input('Стоимость "Эконома" за пару: ')
    
    if za == 0:
        za = 1
    else:
        za < 0
    with col230:
        zb = st.number_input('Стоимость "Стандарта" за пару: ')
    
    if zb == 0:
        zb = 1
    else:
        zb < 0
    with col240:
        zc = st.number_input('Стоимость "Прочных" за пару: ')
    
    if zc == 0:
        zc = 1
    else:
        zc < 0
    with col240:
        zd = st.number_input('Стоимость "Детских" за пару: ')
    
    if zd == 0:
        zd = 1
    else:
        zd < 0
    ze = za * 4000
    zf = zb * 3500
    zg = zc * 2000
    zh = zd * 5400
    
    st.title('Сделано (указать кол-во коробок): ')
    col250, col260 = st.beta_columns(2)
    with col250:
        wa = st.number_input('Кол-во "Эконома": ')
        wb = st.number_input('Кол-во "Стандарта": ')
    with col260:
        wc = st.number_input('Кол-во "Прочных": ')
        wd = st.number_input('Кол-во "Детских": ')
    
    st.title('Отгрузили (указать кол-во коробок): ')
    col270, col280 = st.beta_columns(2)
    with col270:
        ya = st.number_input('Кол-во "Экoнома": ')
        yb = st.number_input('Кoл-во "Стандарта": ')
    with col280:
        yc = st.number_input('Кол-вo "Прочных": ')
        yd = st.number_input('Кoл-во "Детских": ')
    
    xa = wa - ya
    xb = wb - yb
    xc = wc - yc
    xd = wd - yd
    
    ua = ze * wa
    ub = zf * wb
    uc = zg * wc
    ud = zh * wd

    va = ze * ya
    vb = zf * yb
    vc = zg * yc
    vd = zh * yd

    ta = ze * xa
    tb = zf * xb
    tc = zg * xc
    td = zh * xd
    col290, col300 = st.beta_columns(2)
    
    st.write('Эконом: ')
    st.write('Сделано: '  + str(wa) + ' кор., ' + 'Сумма ЗП: ' + str(ua) + ' руб.')
    st.write('Отгрузили: '  + str(ya) + ' кор., ' + 'Оплата: ' + str(va) + ' руб.')
    st.write('Склад: '  + str(xa) + ' кор., ' + 'Долг: ' + str(ta) + ' руб.')
    
    st.write('')
    st.write('')
    
    st.write('Стандарт: ')
    st.write('Сделано: '  + str(wb) + ' кор., ' + 'Сумма ЗП: ' + str(ub) + ' руб.')
    st.write('Отгрузили: '  + str(yb) + ' кор., ' + 'Оплата: ' + str(vb) + ' руб.')
    st.write('Склад: '  + str(xb) + ' кор., ' + 'Долг: ' + str(tb) + ' руб.')
    
    st.write('')
    st.write('')
    
    st.write('Прочные: ')
    st.write('Сделано: '  + str(wc) + ' кор., ' + 'Сумма ЗП: ' + str(uc) + ' руб.')
    st.write('Отгрузили: '  + str(yc) + ' кор., ' + 'Оплата: ' + str(vc) + ' руб.')
    st.write('Склад: '  + str(xc) + ' кор., ' + 'Долг: ' + str(tc) + ' руб.')
    
    st.write('')
    st.write('')
    
    st.write('Детские: ')
    st.write('Сделано: '  + str(wd) + ' кор., ' + 'Сумма ЗП: ' + str(ud) + ' руб.')
    st.write('Отгрузили: '  + str(yd) + ' кор., ' + 'Оплата: ' + str(vd) + ' руб.')
    st.write('Склад: '  + str(xd) + ' кор., ' + 'Долг: ' + str(td) + ' руб.')

#--------------------------

if z == "Цех экструзии":
    st.write('')
    st.title('ЗП ЭКСТРУЗИЯ')
    st.write('')
    st.title('Ставка: ')
    col330, col340 = st.beta_columns(2)
    with col330:
        za1 = st.number_input('Стоимость "12 часов Смена": ')
    
    if za1 == 0:
        za1 = 1
    else:
        za1 < 0
    with col330:
        zb1 = st.number_input('Стоимость "24 часа смена": ')
    
    if zb1 == 0:
        zb1 = 1
    else:
        zb1 < 0
    
    ze1 = za1 * 600
    zf1 = zb1 * 1200
    
    st.title('Сделано (указать кол-во кг): ')
    col350, col360 = st.beta_columns(2)
    with col350:
        wa1 = st.number_input('Кол-во "за 12 часов": ')
        wb1 = st.number_input('Кол-во "за 24 часа": ')
    
    st.title('Отгрузили (указать кол-во кг): ')
    col370, col380 = st.beta_columns(2)
    with col370:
        ya1 = st.number_input('Кол-во "за 12 часоа": ')
        yb1 = st.number_input('Кoл-во "за 24 часа": ')
    
    xa1 = wa1 - ya1
    xb1 = wb1 - yb1
    
    ua1 = ze1 * wa1
    ub1 = zf1 * wb1
    
    va1 = ze1 * ya1
    vb1 = zf1 * yb1
    
    ta1 = ze1 * xa1
    tb1 = zf1 * xb1
    
    st.write('12 часов: ')
    st.write('Сделано: '  + str(wa1) + ' кор., ' + 'Сумма ЗП: ' + str(ua1) + ' руб.')
    st.write('Отгрузили: '  + str(ya1) + ' кор., ' + 'Оплата: ' + str(va1) + ' руб.')
    st.write('Склад: '  + str(xa1) + ' кор., ' + 'Долг: ' + str(ta1) + ' руб.')
    
    st.write('')
    st.write('')
    
    st.write('24 часа: ')
    st.write('Сделано: '  + str(wb1) + ' кор., ' + 'Сумма ЗП: ' + str(ub1) + ' руб.')
    st.write('Отгрузили: '  + str(yb1) + ' кор., ' + 'Оплата: ' + str(vb1) + ' руб.')
    st.write('Склад: '  + str(xb1) + ' кор., ' + 'Долг: ' + str(tb1) + ' руб.')

#--------------------------

if z == "Цех перчатки":
    st.write('')
    st.title('ЗП ПЕРЧАТКИ')
    st.write('')
    st.title('Ставка: ')
    col430, col440 = st.beta_columns(2)
    with col430:
        za11 = st.number_input('Стоимость "Обычные": ')

    if za11 == 0:
        za11 = 1
    else:
        za11 < 0
    with col430:
        zb11 = st.number_input('Стоимость "С манжетой": ')

    if zb11 == 0:
        zb11 = 1
    else:
        zb11 < 0

    ze11 = za11 * 5400
    zf11 = zb11 * 4500

    st.title('Сделано (указать кол-во коробок): ')
    col450, col460 = st.beta_columns(2)
    with col450:
        wa11 = st.number_input('Кол-во "Обычных": ')
        wb11 = st.number_input('Кол-во "С манжетой": ')

    st.title('Отгрузили (указать кол-во коробок): ')
    col470, col480 = st.beta_columns(2)
    with col470:
        ya11 = st.number_input('Кол-во "Обчныx": ')
        yb11 = st.number_input('Кoл-во "C манжетой": ')

    xa11 = wa11 - ya11
    xb11 = wb11 - yb11

    ua11 = ze11 * wa11
    ub11 = zf11 * wb11

    va11 = ze11 * ya11
    vb11 = zf11 * yb11

    ta11 = ze11 * xa11
    tb11 = zf11 * xb11

    st.write('Oбычныe: ')
    st.write('Сделано: '  + str(wa11) + ' кор., ' + 'Сумма ЗП: ' + str(ua11) + ' руб.')
    st.write('Отгрузили: '  + str(ya11) + ' кор., ' + 'Оплата: ' + str(va11) + ' руб.')
    st.write('Склад: '  + str(xa11) + ' кор., ' + 'Долг: ' + str(ta11) + ' руб.')

    st.write('')
    st.write('')

    st.write('С мaнжeтой: ')
    st.write('Сделано: '  + str(wb11) + ' кор., ' + 'Сумма ЗП: ' + str(ub11) + ' руб.')
    st.write('Отгрузили: '  + str(yb11) + ' кор., ' + 'Оплата: ' + str(vb11) + ' руб.')
    st.write('Склад: '  + str(xb11) + ' кор., ' + 'Долг: ' + str(tb11) + ' руб.')

#--------------------------

if z == "Цех пакеты":
    st.write('')
    st.title('ЗП ПАКЕТЫ')
    st.write('')
    st.title('Ставка: ')
    col530, col540 = st.beta_columns(2)
    with col530:
        za111 = st.number_input('Стоимость "4 ручья" за штуку: ')

    if za111 == 0:
        za111 = 1
    else:
        za111 < 0
    with col530:
        zb111 = st.number_input('Стоимость "2 ручья" за штуку: ')

    if zb111 == 0:
        zb111 = 1
    else:
        zb111 < 0
    with col540:
        zc111 = st.number_input('Стоимость "1 ручей" за штуку: ')

    if zc111 == 0:
        zc111 = 1
    else:
        zc111 < 0
    
    ze111 = za111 * 4000
    zf111 = zb111 * 3500
    zg111 = zc111 * 2000

    st.title('Сделано (указать кол-во коробок): ')
    col550, col560 = st.beta_columns(2)
    with col550:
        wa111 = st.number_input('Кол-во "4 ручья": ')
        wb111 = st.number_input('Кол-во "2 ручья": ')
    with col560:
        wc111 = st.number_input('Кол-во "1 ручей": ')

    st.title('Отгрузили (указать кол-во коробок): ')
    col570, col580 = st.beta_columns(2)
    with col570:
        ya111 = st.number_input('Кол-во "4 pучья": ')
        yb111 = st.number_input('Кoл-во "2 pучья": ')
    with col580:
        yc111 = st.number_input('Кол-вo "1 pучей": ')

    xa111 = wa111 - ya111
    xb111 = wb111 - yb111
    xc111 = wc111 - yc111

    ua111 = ze111 * wa111
    ub111 = zf111 * wb111
    uc111 = zg111 * wc111

    va111 = ze111 * ya111
    vb111 = zf111 * yb111
    vc111 = zg111 * yc111

    ta111 = ze111 * xa111
    tb111 = zf111 * xb111
    tc111 = zg111 * xc111

    st.write('4 ручья: ')
    st.write('Сделано: '  + str(wa111) + ' кор., ' + 'Сумма ЗП: ' + str(ua111) + ' руб.')
    st.write('Отгрузили: '  + str(ya111) + ' кор., ' + 'Оплата: ' + str(va111) + ' руб.')
    st.write('Склад: '  + str(xa111) + ' кор., ' + 'Долг: ' + str(ta111) + ' руб.')

    st.write('')
    st.write('')

    st.write('2 ручья: ')
    st.write('Сделано: '  + str(wb111) + ' кор., ' + 'Сумма ЗП: ' + str(ub111) + ' руб.')
    st.write('Отгрузили: '  + str(yb111) + ' кор., ' + 'Оплата: ' + str(vb111) + ' руб.')
    st.write('Склад: '  + str(xb111) + ' кор., ' + 'Долг: ' + str(tb111) + ' руб.')

    st.write('')
    st.write('')

    st.write('1 ручей: ')
    st.write('Сделано: '  + str(wc111) + ' кор., ' + 'Сумма ЗП: ' + str(uc111) + ' руб.')
    st.write('Отгрузили: '  + str(yc111) + ' кор., ' + 'Оплата: ' + str(vc111) + ' руб.')
    st.write('Склад: '  + str(xc111) + ' кор., ' + 'Долг: ' + str(tc111) + ' руб.')

#-------------------------


