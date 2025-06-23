# Entradas
beneficiario = input('Ingrese el beneficiario: ')
codigo_orden = input('Ingrese el código de pago: ')
monto_nominal = float(input('Ingrese el monto nominal: '))

# DETECTAR MONEDA Y CALCULAR MONTO BASE...
if 'ARS' in codigo_orden:
    moneda = 'ARS'
    monto_base = round(monto_nominal - monto_nominal * 5 / 100, 2)
elif 'USD' in codigo_orden:
    moneda = 'USD'
    monto_base = round(monto_nominal - monto_nominal * 7 / 100, 2)
elif 'EUR' in codigo_orden:
    moneda = 'EUR'
    monto_base = round(monto_nominal - monto_nominal * 7 / 100, 2)
elif 'GBP' in codigo_orden:
    moneda = 'GBP'
    monto_base = round(monto_nominal - monto_nominal * 9 / 100, 2)
elif 'JPY' in codigo_orden:
    moneda = 'JPY'
    if 15000 <= monto_nominal <= 500000:
        monto_base = round(monto_nominal - monto_nominal * 9 / 100, 2)
    elif 500000 < monto_nominal <= 1500000:
        monto_base = round(monto_nominal - monto_nominal * 7.8 / 100, 2)
    elif 1500000 < monto_nominal <= 10000000:
        monto_base = round(monto_nominal - monto_nominal * 5.5 / 100, 2)
    elif 10000000 < monto_nominal:
        monto_base = round(monto_nominal - monto_nominal * 5 / 100, 2)
    else:
        monto_base = 0
        monto_final = 0
        moneda = "Monto mínimo para JPY no alcanzado"
    if monto_nominal - monto_base > 950000:
        monto_base = monto_nominal - 950000
else:
    moneda = 'Moneda no autorizada'
    monto_base = 0

# CALCULAR MONTO FINAL
if monto_base > 500000:
    monto_final = round(monto_base - monto_base * 21 / 100, 2)
else:
    monto_final = monto_base

# SALIDAS
print("Beneficiario:", beneficiario)
print("Moneda:", moneda)
print("Monto base (descontadas las comisiones):", monto_base)
print("Monto final (descontados los impuestos):", monto_final)
