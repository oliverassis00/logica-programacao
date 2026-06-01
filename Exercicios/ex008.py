# Ficha de Funcionário
# Crie variáveis para armazenar:
# Nome
# Idade
# Cargo
# Salário
# Exiba todas as informações em uma única mensagem.

nome = input('Qual o nome do funcionário: ')
idade = int(input('Qual a idade do funcionario?: '))
cargo = input('Qual o cargo do funcionário?: ')
salario = float(input('Qual o salário do funcionário?: '))

print(f'O nome é {nome}, a idade é {idade} anos de idade, o cargo é {cargo} e o salário é R${salario}!')