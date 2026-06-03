# Salário com aumento
# Um funcionário recebe:
# salario = 3500
# A empresa concedeu aumento de 12%.
# Calcule o novo salário.

salario = 3500
novo_salario = ((salario * 12) / 100) + salario

print(f'Novo salário R${novo_salario:.2f}'.replace('.',','))