import streamlit as st
import pandas as pd
import numpy as np
import local_settings as settings # Самописный модуль с информацией
#from PIL import Image # Для отображения изображений
import plenka as pl
from plenka import plastik
import products as pr
from products import paketi, bahili, perchatki
import zakaz as za
from zakaz import za_bahili, za_plenka, za_paketi, zaperchatki
import viplati as vi
from viplati import zp_bahili, zp_ekstruziya, zp_perchatki, zp_paketi


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
                        y = za_bahili
                        
                    #---------------------------
                    
                    if y == "Заказ на пленку":
                        y = zak_plenka
                        
                    #---------------------------
                    
                    if y == "Заказ на пакеты":
                        y = zak_paketi
                    
                    #--------------------------
                    
                    if y == "Заказ на перчатки":
                        y = zak_perchatki
                   
                    #-----------------------------------------------------------------
                    
                    z = st.sidebar.selectbox('РАСЧЁТ ВЫПЛАТ:', ['Выбрать/Очистить','Цех бахил','Цех экструзии', 'Цех перчатки','Цех пакеты',])
                    
                    if z == "Цех бахил":
                        z = zp_bahili
                    
                    #--------------------------
                    
                    if z == "Цех экструзии":
                        z = zp_ekstruziya   
                    
                    #--------------------------
                    
                    if z == "Цех перчатки":
                        z = zp_perchatki
                    
                    #--------------------------
                    
                    if z == "Цех пакеты":
                        z = zp_paketi    
                    
                    #-------------------------

                else:
                    st.warning("Неверный пароль! ") # {}".format(username) )

    elif choice == "Контакты":
                st.subheader("Контакты")
                st.markdown('**Корпоративный сайт: ** [tpkpromed.ru](https://tpkpromed.ru)')
                st.markdown('**Производство бахил: ** [bioinvn.ru](https://bioinvn.ru)')
                st.markdown('**Интернет магазин: ** [pmpsale.ru](https://pmpsale.ru)')
                # st.markdown('**Скачать приложение: ** [Скачать](https://goo.su/RH7qQ)')
                # image = Image.open('./qrcode/qrcode.jpg')
                # st.image(image, width = 100, caption='QR код для скачивания',use_column_width=100)

if __name__ == '__main__':
        main()
