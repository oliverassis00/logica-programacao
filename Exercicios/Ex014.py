# Valor total da compra
# Uma loja vende:
# Produto: R$ 89,90
# Quantidade: 3 unidades
# Calcule:
# Valor bruto
# Desconto de 10%
# Valor final

produto = 89.90
quantidade = 3

valor_bruto = produto * 3
desconto = valor_bruto - ((valor_bruto * 10) / 100)

print(f'Valor do produto R${valor_bruto:.2f},'.replace('.',','),f'valor com desconto ofertado R${desconto:.2f}'.replace('.',','))