# calcular monto final...
def calcular_monto_final(base, id_impuesto):
    impuesto = 0
    # algoritmo 1...
    if id_impuesto in '1 ':
        if base <= 300000:
            impuesto = 0
        elif base > 300000:
            excedente = base - 300000
            impuesto = excedente * 25 // 100

    # algoritmo 2...
    elif id_impuesto in '2 ':
        if base < 50000:
            impuesto = 50
        elif base >= 50000:
            impuesto = 100

    # algoritmo 3...
    elif id_impuesto in '3 ':
        impuesto = base * 3 // 100

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
        comision = nominal * 9 // 100

    # algoritmo 2...
    elif id_comision in '2 ':
        if nominal < 50000:
            comision = 0
        elif 50000 <= nominal < 80000:
            comision = nominal * 5 // 100
        elif nominal > 80000:
            comision = nominal * 7.8 // 100

    # algoritmo 3...
    elif id_comision in '3 ':
        monto_fijo = 100
        if nominal > 25000:
            comision = nominal * 6 // 100

    # algoritmo 4...
    elif id_comision in '4 ':
        if nominal <= 100000:
            comision = 500
        elif nominal > 100000:
            comision = 1000

    # algoritmo 5...
    elif id_comision in '5 ':
        if nominal < 500000:
            comision = 0
        elif nominal >= 500000:
            comision = nominal * 7 // 100
            if comision > 50000:
                comision = 50000

    monto_base = nominal - (monto_fijo + comision)
    return monto_base


# valida el tipo de moneda...
def tipo_moneda(cod_orden):
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
    cod_ide = cod_ide.strip()
    if len(cod_ide) == 0:
        return False
    tiene_letra_o_digito = False
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
    cant_minvalida = 0
    cant_binvalido = 0
    cant_oper_validas = 0
    suma_mf_validas = 0

    cant_ARS = cant_USD = cant_EUR = cant_GBP = cant_JPY = 0

    max_diferencia = -1
    cod_orden_max = ''
    monto_nominal_max = 0
    monto_final_max = 0

    nom_primer_benef = None
    cant_nom_primer_benef = 0

    suma_ars_finales = 0
    cant_ars_validas = 0

    m = open('ordenes.txt', 'rt')
    timestamp = m.readline()
    total_ordenes = 0

    for linea in m:
        total_ordenes += 1

        nom_dest = linea[0:20]
        cod_ide = linea[20:30]
        cod_orden = linea[30:40]
        monto_nominal_str = linea[40:50]
        id_calc_com = linea[50:52]
        id_calc_imp = linea[52:54]

        moneda = tipo_moneda(cod_orden)
        monto_base = calcular_monto_base(monto_nominal_str, id_calc_com)
        monto_final = calcular_monto_final(monto_base, id_calc_imp)
        invalida = False

        if moneda == 'ARS':
            cant_ARS += 1
        elif moneda == 'USD':
            cant_USD += 1
        elif moneda == 'EUR':
            cant_EUR += 1
        elif moneda == 'GBP':
            cant_GBP += 1
        elif moneda == 'JPY':
            cant_JPY += 1

        if moneda == 'Moneda incorrecta':
            cant_minvalida += 1
            invalida = True

        if not destinatario_valido(cod_ide):
            cant_binvalido += 1
            invalida = True

        if not invalida:
            cant_oper_validas += 1
            suma_mf_validas += monto_final
            if moneda == 'ARS':
                suma_ars_finales += monto_final
                cant_ars_validas += 1

        monto_nominal_int = int(monto_nominal_str.strip())
        diferencia = abs(monto_nominal_int - monto_final)

        if diferencia > max_diferencia:
            max_diferencia = diferencia
            cod_orden_max = cod_orden.strip()
            monto_nominal_max = monto_nominal_int
            monto_final_max = monto_final

        if nom_primer_benef is None:
            nom_primer_benef = nom_dest

        if nom_dest == nom_primer_benef:
            cant_nom_primer_benef += 1

    m.close()

    total_invalidas = cant_minvalida + cant_binvalido
    porcentaje_invalidas = (total_invalidas * 100) // total_ordenes

    if cant_ars_validas > 0:
        promedio_ars = suma_ars_finales // cant_ars_validas
    else:
        promedio_ars = 0

    # Resultados
    print(' (r1) - Cantidad de ordenes invalidas - moneda no autorizada:', cant_minvalida)
    print(' (r2) - Cantidad de ordenes invalidas - beneficiario mal identificado:', cant_binvalido)
    print(' (r3) - Cantidad de operaciones validas:', cant_oper_validas)
    print(' (r4) - Suma de montos finales de operaciones validas:', suma_mf_validas)
    print(' (r5) - Cantidad de ordenes para moneda ARS:', cant_ARS)
    print(' (r6) - Cantidad de ordenes para moneda USD:', cant_USD)
    print(' (r7) - Cantidad de ordenes para moneda EUR:', cant_EUR)
    print(' (r8) - Cantidad de ordenes para moneda GBP:', cant_GBP)
    print(' (r9) - Cantidad de ordenes para moneda JPY:', cant_JPY)
    print(' (r10) - Código de la orden de pago con mayor diferencia:', cod_orden_max)
    print(' (r11) - Monto nominal de esa orden:', monto_nominal_max)
    print(' (r12) - Monto final de esa orden:', monto_final_max)
    print('(r13) - Nombre del primer beneficiario del archivo:', nom_primer_benef)
    print('(r14) - Cantidad de veces que apareció ese mismo nombre:', cant_nom_primer_benef)
    print('(r15) - Porcentaje de operaciones inválidas sobre el total:', porcentaje_invalidas)
    print('(r16) - Promedio del monto final de órdenes válidas (moneda y beneficiario) en ARS:', promedio_ars)


principal()
