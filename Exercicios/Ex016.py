# Conversão de moedas
# Dado:
# reais = 1500
# cotacao_dolar = 5.42
# Calcule quantos dólares podem ser comprados.

reais = 1500
cotacao_dolar = 5.42

conversao_dolares = reais / cotacao_dolar

print(f'R${conversao_dolares:.2f}'.replace('.',','))