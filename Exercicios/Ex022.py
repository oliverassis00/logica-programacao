# Sistema de Frete Inteligente para E-commerce

valor_compra = float(input('Digite o valor da compra (R$): '))
estado_destino = input('Digite o Estado Destino (Ex: SP): ').upper()
peso = float(input('Digite o peso da mercadoria (KG): '))

frete = 0

# Frete grátis para compras acima de R$300
if valor_compra >= 300:
    frete = 0

else:
    # Região Norte
    if estado_destino in ('AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO'):
        if peso <= 5:
            frete = 25
        else:
            frete = 45

    # Região Sudeste
    elif estado_destino in ('SP', 'RJ', 'MG', 'ES'):
        if peso <= 5:
            frete = 15
        else:
            frete = 30

    else:
        print('Estado não pertence às regiões cadastradas.')
        exit()

# Taxa adicional para peso acima de 20kg
if peso > 20:
    frete += 50

print(f'Valor final do frete: R${frete:.2f}')