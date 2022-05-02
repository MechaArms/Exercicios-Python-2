#Exercício 26
'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
    + Álcool:
        -até 20 litros, desconto de 3% por litro
        -acima de 20 litros, desconto de 5% por litro
    + Gasolina:
        -até 20 litros, desconto de 4% por litro
        -acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''
def bomba(combustivel, litros):
    a = 2.50
    g = 1.90
    if combustivel == 'A':
        if litros <= 20:
            desconto = (a/100)*3
            print(f'O desconto é de {desconto} reais para {litros} litros')
        elif litros > 20:
            desconto = (a/100)*5
            print(f'O desconto é de {desconto} reais para {litros} litros')
        else:
            print('informação quantidade de litros de combustivel invalida')
    elif combustivel == 'G':
        if litros <= 20:
            desconto = (g/100)*4
            print(f'O desconto é de {desconto} reais para {litros} litros')
        elif litros > 20:
            desconto = (g/100)*6
            print(f'O desconto é de {desconto} reais para {litros} litros')
        else:
            print('informação quantidade de litros de combustivel invalida')
    else:
        print('informação tipo de combustivel invalida')

print('O preço do litro da gasolina é R$ 2,50 \nO preço do litro do álcool é R$ 1,90. \n')

combustivel = str(input('Digite o tipo de combustivel\nA-álcool, G-gasolina: ').upper())

litros = float(input('\nDigite a quantidade de litros de combustivel: '))

bomba(combustivel, litros)