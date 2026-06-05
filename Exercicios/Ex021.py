# Sistema de Aprovação de Crédito Bancário 💳
# Crie um programa que receba:
# Salário
# Score de crédito
# Tempo de emprego (anos)
# Regras:
# Score < 500 → Crédito negado 
# Score ≥ 500 e salário ≥ 3000: ok
# Tempo emprego ≥ 2 anos → Aprovado ok
# Caso contrário → Análise manual ok
# Score ≥ 800 e salário ≥ 5000 → Pré-aprovado VIP ok

salario = float(input('Digite o salário: '))
score_credito = int(input('Digite o Score: '))
tempo_trabalho = int(input('Digite o tempo de trabalho: '))


if score_credito < 500:
    print('Credito Negado!')
if score_credito >= 500 and score_credito < 800 and salario >= 3000:
    if tempo_trabalho >= 2:
        print('Aprovado!')
    else: 
        print('Análise Manual')
if score_credito >= 800 and salario >= 5000:
    print('Pré-Aprovado VIP!')