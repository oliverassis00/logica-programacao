# Conversão de temperatura
# Receba uma temperatura em Celsius e converta para Fahrenheit.
# Fórmula:
# F = C × 9/5 + 32

temp_celsius = float(input('Digite a temperatura em Celsius (Cº): '))

con_fahrenheit = (temp_celsius * 1.8) + 32 # já tem ordem de precedencia por ser multiplicação, mas enfatizei a prioridade

print(f'A conversão de Cº {temp_celsius} para Fº {con_fahrenheit}')