# Separação de horas
# Você possui:
# segundos = 9876
# Descubra:
# Quantas horas completas existem
# Quantos minutos restantes
# Quantos segundos restantes
# Utilize apenas operadores matemáticos.

segundos = 9876

horas = segundos // 3600
resto = segundos % 3600

minutos = resto // 60
segundos_restantes = resto % 60

print("Horas:", horas)
print("Minutos:", minutos)
print("Segundos:", segundos_restantes)