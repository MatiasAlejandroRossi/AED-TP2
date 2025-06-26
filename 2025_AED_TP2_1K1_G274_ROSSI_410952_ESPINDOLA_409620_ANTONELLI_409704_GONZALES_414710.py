# detecta el tipo de moneda en el codigo de orden...
def tipo_moneda(cod_orden):
    # flag ya hay un tipo de moneda...
    smon = False
    if 'ARS' in cod_orden:
        moneda = 'ARS'
        smon = True
    elif 'USD' in cod_orden:
        moneda = 'USD'
        if smon:
            moneda = 'Moneda incorrecta'
        smon = True
    elif 'EUR' in cod_orden:
        moneda = 'EUR'
        if smon:
            moneda = 'Moneda incorrecta'
        smon = True
    elif 'GBP' in cod_orden:
        moneda = 'GBP'
        if smon:
            moneda = 'Moneda incorrecta'
        smon = True
    elif 'JPY' in cod_orden:
        moneda = 'JPY'
        if smon:
            moneda = 'Moneda incorrecta'
        smon = True
    else:
        moneda = 'Moneda incorrecta'
    return moneda


# calcular monto base...
def monto_base(moneda):
    # ARS...
    monto_base = round(monto_nominal - monto_nominal * 5 / 100, 2)
    # USD...
    monto_base = round(monto_nominal - monto_nominal * 7 / 100, 2)
    # EUR...
    monto_base = round(monto_nominal - monto_nominal * 7 / 100, 2)
    # GBP...
    monto_base = round(monto_nominal - monto_nominal * 9 / 100, 2)
    # JPY...
    # enunciado adicional TP1...
    if 15000 <= monto_nominal <= 500000:
        monto_base = round(monto_nominal - monto_nominal * 9 / 100, 2)
    elif 500000 < monto_nominal <= 1500000:
        monto_base = round(monto_nominal - monto_nominal * 7.8 / 100, 2)
    elif 1500000 < monto_nominal <= 10000000:
        monto_base = round(monto_nominal - monto_nominal * 5.5 / 100, 2)
    elif 10000000 < monto_nominal:
        monto_base = round(monto_nominal - monto_nominal * 5 / 100, 2)
    # Moneda incorrecta...
    else:
        monto_base = 0


# calcular monto final...
def monto_final():
    if monto_base > 500000:
        monto_final = round(monto_base - monto_base * 21 / 100, 2)
    else:
        monto_final = monto_base


def principal():
    # definicion de variables...
    nom_dest = cod_ide = cod_op = monto_nominal = id_calc_com = id_calc_imp = ''

    # procesamiento del archivo ordenes.txt...
    m = open('ordenes.txt', 'rt')
    timestamp = m.readline()  # ignorar el timestamp...

    for linea in m:
        # procesamiento linea por linea de las ordenes de pago...
        # variables...
        nom_dest = linea[0:20]  # nombre del destsinatario...
        cod_ide = linea[20:30]  # codigo identificacion destinatario...
        cod_orden = linea[30:40]  # codigo orden de pago...
        monto_nominal = linea[40:50]  # monto nominal...
        id_calc_com = linea[50:52]  # identificador algoritmo calculo comision...
        id_calc_imp = linea[52:54]  # identificador algoritmo calculo impositivo...

        # procesos...

    # cerrar el .txt
    m.close()

    # salidas...
    print(' (r1) - Cantidad de ordenes invalidas - moneda no autorizada:', cant_minvalida)
    print(' (r2) - Cantidad de ordenes invalidas - beneficiario mal identificado:', cant_binvalido)
    print(' (r3) - Cantidad de operaciones validas:', cant_oper_validas)
    print(' (r4) - Suma de montos finales de operaciones validas:', suma_mf_validas)
    print(' (r5) - Cantidad de ordenes para moneda ARS:', cant_ARS)
    print(' (r6) - Cantidad de ordenes para moneda USD:', cant_USD)
    print(' (r7) - Cantidad de ordenes para moneda EUR:', cant_EUR)
    print(' (r8) - Cantidad de ordenes para moneda GBP:', cant_GBP)
    print(' (r9) - Cantidad de ordenes para moneda JPN:', cant_JPY)
    print('(r10) - Codigo de la orden de pago con mayor diferencia nominal - final:', cod_my)
    print('(r11) - Monto nominal de esa misma orden:', mont_nom_my)
    print('(r12) - Monto final de esa misma orden:', mont_fin_my)
    print('(r13) - Nombre del primer beneficiario del archivo:', nom_primer_benef)
    print('(r14) - Cantidad de veces que apareció ese mismo nombre:', cant_nom_primer_benef)
    print('(r15) - Porcentaje de operaciones inválidas sobre el total:', porcentaje)
    print('(r16) - Monto final promedio de las ordenes validas en moneda ARS:', promedio)


principal()
