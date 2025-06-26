# calcular monto final...
def calcular_monto_final(base, id_impuesto):
    impuesto = 0
    #algoritmo 1...
    if id_impuesto in '1 ':
        if base <= 300000:
            impuesto = 0
        elif base > 300000:
            excedente = base - 300000
            impuesto = excedente * 25 / 100

    #algoritmo 2...
    elif id_impuesto in '2 ':
        if base < 50000:
            impuesto = 50
        elif base >= 50000:
            impuesto = 100

    #algoritmo 3...
    elif id_impuesto in '3 ':
        impuesto = base * 3 / 100

    monto_final = base - impuesto
    return round(monto_final, 2)


# calcular monto base...
def calcular_monto_base(nominal, id_comision):
    nominal = int(nominal)
    monto_base = 0
    comision = 0
    monto_fijo = 0
    # algoritmo 1...
    if id_comision in '1 ':
        comision = nominal * 9 / 100
    
    # algoritmo 2...
    elif id_comision in '2 ':
        if nominal < 50000:
            comision = 0
        elif 50000 <= nominal < 80000:
            comision = nominal * 5 / 100
        elif nominal > 80000:
            comision = nominal * 7.8 / 100
    
    # algoritmo 3...
    elif id_comision in '3 ':
        monto_fijo = 100
        if nominal > 25000:
            comision = nominal * 6 / 100

    # algoritmo 4...
    elif id_comision in '4 ':
        if nominal <= 100000:
            comision = 500
        
    elif id_comision in '4 ':
        if nominal > 100000:
            comision = 1000

    # algoritmo 5...
    elif id_comision in '5 ':
        if nominal < 500000:
            comision = 0
        elif nominal >= 500000:

            comision = nominal * 7 / 100
        elif comision > 50000:
            comision = 50000

    # calculo del monto base...
    monto_base = nominal - (monto_fijo + comision)
    return monto_base


# valida el tipo de moneda...
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


# valida destinatario...
def destinatario_valido(cod_ide):
    cod_ide = cod_ide.strip()  # elimina espacios en blanco...
    # valida que no este vacio el campo...
    if len(cod_ide) == 0:
        return False
    tiene_letra_o_digito = False  # flag...
    for c in cod_ide:
        if c.isupper() or c.isdigit():
            tiene_letra_o_digito = True
        elif c != '-':
            return False
    if '-' in cod_ide and not tiene_letra_o_digito:
        return False
    elif not tiene_letra_o_digito:
        return False
    return True


def principal():
    # definicion de variables...
    nom_dest = cod_ide = cod_op = monto_nominal = id_calc_com = id_calc_imp = ''

    # contadores para los resultados...
    cant_minvalida = 0  # cantidad moneda invalida...
    cant_binvalido = 0  # cantidad beneficiario invalido...
    cant_oper_validas = 0  # cantidad operaciones validas...
    suma_mf_validas = 0 # r4...
    # procesamiento del archivo ordenes.txt...
    m = open('ordenes.txt', 'rt')
    timestamp = m.readline()  # ignora el timestamp...

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
        moneda = tipo_moneda(cod_orden)
        if moneda == 'Moneda incorrecta':
            cant_minvalida += 1


        elif not destinatario_valido(cod_ide):
            cant_binvalido += 1


         # Aquí está la suma del punto (r3):
        elif destinatario_valido(cod_ide):
            cant_oper_validas += 1
            # Requerimiento 2 (r4)...
            monto_base = calcular_monto_base(monto_nominal, id_calc_com)
            monto_final = calcular_monto_final(monto_base, id_calc_imp)
            suma_mf_validas += monto_final
            
    # cerrar el .txt
    m.close()

    # salidas...
    print(' (r1) - Cantidad de ordenes invalidas - moneda no autorizada:', cant_minvalida)
    print(' (r2) - Cantidad de ordenes invalidas - beneficiario mal identificado:', cant_binvalido)
    print(' (r3) - Cantidad de operaciones validas:', cant_oper_validas)
    print(' (r4) - Suma de montos finales de operaciones validas:', suma_mf_validas)
"""    print(' (r5) - Cantidad de ordenes para moneda ARS:', cant_ARS)
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
"""

principal()
