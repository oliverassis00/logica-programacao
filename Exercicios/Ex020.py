# Conversão de minutos
# Receba:
# minutos = 345
# Converta para:
# Horas
# Minutos restantes

minutos = 345

minutos_restantes = minutos % 60
horas = minutos // 60

print(f'''
horas: {horas}
minutos: {minutos_restantes}
    ''')