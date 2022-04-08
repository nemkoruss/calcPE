import streamlit as st
import pandas as pd
import numpy as np
import local_settings as settings # Самописный модуль с информацией
#from PIL import Image # Для отображения изображений
import vibor_rascheta as vib # Модуль расчета продукции
from vibor_rascheta import products, orders, salarys



#imgs = Image.open('icon.jpg')
PAGE_CONFIG = {'page_title':'calcPe' , 'page_icon':'polietilen.png' , 'layout':'centered'}
st.set_page_config(**PAGE_CONFIG)
#st.set_page_config(page_title = 'calcPe', page_icon = 'imgs')

#–---------------------------------------------------------------------------

def main():
    menu = ['Инструкция', 'Калькулятор', 'Контакты']
    choice = st.sidebar.selectbox("Меню" ,menu)

    if choice == 'Инструкция':
            st.subheader ('Инструкция')
            st.subheader('Для работы калькулятора выберите в боковом меню нужный расчёт !')
            st.markdown('*Для входа в боковое меню на устройстве с маленьким экраном нажмите, в левом вверхнем углу, значок в виде стрелки  ">"*')
            st.markdown('*Для более комфортной работы, не забывайте "Очищать экран"  *')

    elif choice == 'Калькулятор':
           # st.subheader("Пароль верный")
            #username = st.sidebar.text_input("Имя")
            password = st.sidebar.text_input('Пароль', type='password')
            if st.sidebar.checkbox('Войти'):

                if password == settings.MYSQL_PASSWORD:

                    st.success('Верный пароль! ') # {}".format(username) )

                    zic = st.sidebar.selectbox('Что считаем?', ['Выбрать/Очистить','Продукция', 'Заказ', 'Зарплата'])
                    if zic == 'Продукция':
                        zic = products()

                    elif zic == 'Заказ':
                        zic = orders()

                    elif zic == 'Зарплата':
                        zic = salarys()

                else:
                    st.warning('Неверный пароль! ') # {}".format(username) )

    elif choice == 'Контакты':
                st.subheader('Контакты')
                st.markdown('**Корпоративный сайт: ** [tpkpromed.ru](https://tpkpromed.ru)')
                st.markdown('**Производство бахил: ** [bioinvn.ru](https://bioinvn.ru)')
                st.markdown('**Интернет магазин: ** [pmpsale.ru](https://pmpsale.ru)')
                # st.markdown('**Скачать приложение: ** [Скачать](https://goo.su/RH7qQ)')
                #image = Image.open('./img/qrcode.jpg')
                # st.image(image, width = 100, caption='QR код для скачивания',use_column_width=100)

                #Для файла Excel
                df = pd.read_excel('price.xlsx')
if __name__ == '__main__':
        main()
