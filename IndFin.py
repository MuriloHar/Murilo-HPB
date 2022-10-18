import json

txt = '[{"securityIdentificationCode":10014464,"description":"DIF OPER CASADA - COMPRA","groupDescription":"TAXAS DE CÂMBIO","value":"","rate":"15,76","lastUpdate":"17/10/2022"},{"securityIdentificationCode":10008989,"description":"DÓLAR CUPOM LIMPO","groupDescription":"TAXAS DE CÂMBIO","value":"5,2890","rate":"","lastUpdate":"17/10/2022"},{"securityIdentificationCode":10009506,"description":"DÓLAR BMF SPOT - 2 DIAS","groupDescription":"TAXAS DE CÂMBIO","value":"5,2901","rate":"","lastUpdate":"17/10/2022"},{"securityIdentificationCode":9800508,"description":"DOLAR SPOT BMF PARA 1 DIA","groupDescription":"TAXAS DE CÂMBIO","value":"5,2879","rate":"","lastUpdate":"17/10/2022"},{"securityIdentificationCode":10014538,"description":"TAXA LIBOR - BRADIES","groupDescription":"TAXAS DE JUROS INTERNACIONAL","value":"3,480","rate":"","lastUpdate":"17/10/2022"},{"securityIdentificationCode":9800656,"description":"TAXA SELIC","groupDescription":"TAXAS DE JUROS NACIONAL","value":"","rate":"13,65","lastUpdate":"17/10/2022"},{"securityIdentificationCode":9800334,"description":"TAXA CDI CETIP","groupDescription":"TAXAS DE JUROS NACIONAL","value":"","rate":"13,65","lastUpdate":"17/10/2022"}]'

a = json.loads(txt)
indicadores = []
cont = 0
cont2 = 0

for y in a:
    h = y.items()
    for z in h:
        if z[0] == 'value':
            indicadores.append(z[1])
        elif z[0] == 'rate':
            indicadores.append(z[1])
        else:
            continue

for b in indicadores:
    if b == '':
        indicadores.pop(cont)
        cont += 1
    elif b == ' ':
        indicadores.pop(cont)
        cont += 1
    else:
        cont += 1

for c in indicadores:
    if c == '':
        indicadores.pop(cont2)
        cont2 += 1
    elif c == ' ':
        indicadores.pop(cont2)
        cont2 += 1
    else:
        cont2 += 1

print(indicadores)
