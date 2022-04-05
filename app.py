import streamlit as st
import pandas as pd
import numpy as np
import local_settings as settings # Самописный модуль с информацией
from PIL import Image # Для отображения изображений
import plenka as pl # Модуль расчета замеса пленки
from plenka import plastik 
import products as pr # Молуль расчета пролукции
from products import paketi, bahili, perchatki
import zakaz # Модуль расчета выполнения заказа
from zakaz import zabahili, zaplenka, zapaketi, zaperchatki
import viplati # Модуль расчета зарплат
from viplati import zpbahili, zpekstruziya, zpperchatki, zppaketi

imgs = Image.open('./img/icon.jpg')
#PAGE_CONFIG = {'page_title':'calcPe' , 'page_icon':'./img/icon.jpg' , 'layout':'centered'}
#st.set_page_config(**PAGE_CONFIG)
st.set_page_config(page_title = 'calcPe', page_icon = 'imgs')

#–---------------------------------------------------------------------------

def main():
    menu = ["Инструкция", "Калькулятор", "Контакты"]
    choice = st.sidebar.selectbox("Меню" ,menu)

    if choice == "Инструкция":
            st.subheader ("Инструкция")
            st.subheader('Для работы калькулятора выберите в боковом меню нужный расчёт !')
            st.markdown('*Для входа в боковое меню на устройстве с маленьким экраном нажмите, в левом вверхнем углу, значок в виде стрелки  ">"*')
            st.markdown('*Для более комфортной работы, не забывайте "Очищать экран"  *')

    elif choice == "Калькулятор":
           # st.subheader("Пароль верный")
            #username = st.sidebar.text_input("Имя")
            password = st.sidebar.text_input("Пароль", type='password')
            if st.sidebar.checkbox("Войти"):

               # if password == 'tatoshka12':
                if password == settings.MYSQL_PASSWORD:

                    st.success("Верный пароль! ") # {}".format(username) )
                                        
                    b = st.sidebar.selectbox('РАСЧЁТ ПЛЕНКИ:', ['Выбрать/Очистить','Замес гранулы'])
                    
                    if b == 'Замес гранулы':
                        b = plastik() 
           
                    #-----------------------------------------------------------------
                    
                    x = st.sidebar.selectbox('РАСЧЁТ ПРОДУКЦИИ:', ['Выбрать/Очистить','Пакеты','Бахилы','Перчатки'])
                    
                    if x == "Пакеты":
                        x = paketi()
                        
                    #------------------------
                    
                    elif x == "Бахилы":
                        x = bahili()                   
                       
                    #-------------------------
                    
                    elif x == "Перчатки":
                        x = perchatki() 
                        
                    #----------------------------------------------------------------
                    
                    y = st.sidebar.selectbox('РАСЧЁТ ЗАКАЗА:', ['Выбрать/Очистить','Заказ на бахилы','Заказ на пленку', 'Заказ на пакеты','Заказ на перчатки'])
                    
                    if y == "Заказ на бахилы":
                        y = zabahili()
                        
                    #---------------------------
                    
                    if y == "Заказ на пленку":
                        y = zaplenka()
                        
                    #---------------------------
                    
                    if y == "Заказ на пакеты":
                        y = zapaketi()
                    
                    #--------------------------
                    
                    if y == "Заказ на перчатки":
                        y = zaperchatki()
                   
                    #-----------------------------------------------------------------
                    
                    z = st.sidebar.selectbox('РАСЧЁТ ВЫПЛАТ:', ['Выбрать/Очистить','Цех бахил','Цех экструзии', 'Цех перчатки','Цех пакеты',])
                    
                    if z == "Цех бахил":
                        z = zpbahili()
                    
                    #--------------------------
                    
                    if z == "Цех экструзии":
                        z = zpekstruziya()  
                    
                    #--------------------------
                    
                    if z == "Цех перчатки":
                        z = zpperchatki()
                    
                    #--------------------------
                    
                    if z == "Цех пакеты":
                        z = zppaketi()  
                    
                    #-------------------------

                else:
                    st.warning("Неверный пароль! ") # {}".format(username) )

    elif choice == "Контакты":
                st.subheader("Контакты")
                st.markdown('**Корпоративный сайт: ** [tpkpromed.ru](https://tpkpromed.ru)')
                st.markdown('**Производство бахил: ** [bioinvn.ru](https://bioinvn.ru)')
                st.markdown('**Интернет магазин: ** [pmpsale.ru](https://pmpsale.ru)')
                # st.markdown('**Скачать приложение: ** [Скачать](https://goo.su/RH7qQ)')
                image = Image.open('./img/iconq.jpg')
                # st.image(image, width = 100, caption='QR код для скачивания',use_column_width=100)

if __name__ == '__main__':
        main()
