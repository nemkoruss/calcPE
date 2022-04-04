def plastik():

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
        st.subheader('В одном килограмме замеса: ')
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
        xz = (az2 + bz2 + vst2 + cz2 + dz2) / ez
        # st.write(str(xz) + ' руб.')
    with col3:
        ez1 = st.number_input('Зарплатa сотрудников: ')
        fz = st.number_input('Стоимость аренды: ')
        gz = st.number_input('Стоимость электричества: ')
        zz = ez1 + fz + gz
    with col4:
        iz = st.number_input('Стоимость ТО: ')
        iz = xz * iz / 100
        st.write(str(iz) + ' руб.')
    with col4:
        kz = st.number_input('Возврат за экструдер: ')
        kz = xz * kz / 100
        st.write(str(kz) + ' руб.')
    with col4:
        lz = st.number_input('Введите БРАК: ')
        lz =   xz * lz / 100
        st.write(str(lz) + ' руб.')
        yz = xz + zz + iz + kz + lz
        st.write('')
        st.write('Себестоимость замеса гранулы: ' + str(yz) + ' руб.')

    col31, col41 = st.beta_columns(2)
    with col31:
        st.write('')
        st.title('Pасчёт пpодажи: ')
        nak = st.number_input('Пpоцент удоpожания:')
        nakk = yz * (nak + 100) / 100
    with col31:
        st.write('Пpодажа: ' + str(nakk) + ' руб.')

plastik()
