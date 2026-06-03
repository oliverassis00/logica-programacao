# Cálculo de bônus
# Um vendedor recebe:
# salario = 2500
# vendas = 18000
# O bônus corresponde a 5% das vendas.
# Calcule:
# Valor do bônus
# Salário final

salario = 2500
vendas = 18000

bonus = (vendas * 5) / 100

salario = bonus + salario

print(f'Valor Salário Atualizado R${salario:.2f} e o Valor do Bonus R${bonus:.2f}')