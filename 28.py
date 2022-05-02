#Exercicio 28
'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. 
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
'''

def carnes(tipo_carne, qtd_carne):
    f1 = 4.90
    f2 = 5.80
    a1 = 5.90
    a2 = 6.80
    p1 = 6.90
    p2 = 7.80

    if tipo_carne == 1:
        if qtd_carne > 1 and qtd_carne < 5:
            preco = qtd_carne * f1
        elif qtd_carne >= 5:
            preco = qtd_carne * f2
        else:
            print('valor digitado do Kg é invalido')
    elif tipo_carne == 2:
        if qtd_carne > 1 and qtd_carne < 5:
            preco = qtd_carne * a1
        elif qtd_carne >= 5:
            preco = qtd_carne * a2
        else:
            print('valor digitado do Kg é invalido')
    elif tipo_carne == 3:
        if qtd_carne > 1 and qtd_carne < 5:
            preco = qtd_carne * p1
        elif qtd_carne >= 5:
            preco = qtd_carne * p2
        else:
            print('valor digitado do Kg é invalido')
    else:
        print('valor digitado do tipo de carne é invalido! Digite apenas: [1, 2 ou 3]')

    pagamento(preco, tipo_pagm)

def pagamento(preco,tipo_pagm):
    if tipo_pagm == 1:
        desconto = preco - ((preco/100)*5)
        print(f'O valor a pagar é de R$ {desconto} com o desconto do Cartão Tabajara de 5%. Sem o desconto o valor seria de R$ {preco}')
    elif tipo_pagm == 2:
        print(f'O valor a pagar é de {preco} em dinheiro sem desconto')
    else:
        print('valor digitado do tipo de pagamento é invalido! Digite apenas: [1 ou 2]') 

tipo_carne = int(input('Digite o numero referente ao tipo de carne que será comprada:\n1 - File Duplo, 2- Alcatra, 3 - Picanha\nDigite aqui: '))
qtd_carne = float(input('\nDigite a quantidade de Carne adquirida em Kg: '))
tipo_pagm = int(input('\nDigite o numero referente ao tipo de pagamento:\n1 - Cartão Tabajara ou 2 - dinheiro\nDigite aqui: '))

carnes(tipo_carne, qtd_carne)