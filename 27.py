#Exercício 27
'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''

def frutas(morango_kg, maca_kg):
    mor1 = 2.50
    mor2 = 2.20
    mac1 = 1.80
    mac2 = 1.50

    if morango_kg > 0 and morango_kg < 4:
        preço_mor = morango_kg * mor1
    elif morango_kg >= 5:
        preço_mor = morango_kg * mor2
    else:
        print('valor digitado invalido')

    if maca_kg > 0 and maca_kg < 4:
        preço_mac = maca_kg * mac1
    elif maca_kg >= 5:
        preço_mac = maca_kg * mac2
    else:
        print('valor digitado invalido')

    pagamento(preço_mor,preço_mac, maca_kg, morango_kg)

def pagamento(preço_mor, preço_mac, maca_kg, morango_kg):
    total_kg = maca_kg + morango_kg
    total_pgm = preço_mor + preço_mac
    desconto = 0
    if total_pgm > 25 or total_kg > 25:
        desconto = (total_pgm/100)*10
        preco_final = total_pgm - desconto
        print(f'+ morangos = R$ {preço_mor}')
        print(f'+ maças = R$ {preço_mac}')
        print(f'- desconto = R$ {desconto}')
        print(f' total a pagar = R$ {preco_final}')
    else:
        print(f'+ morangos = R$ {preço_mor}')
        print(f'+ maças = R$ {preço_mac}')
        print(f'Total a pagar = R$ {total_pgm}')

morango_kg = float(input('Digite a quantidade de Morangos adquiridos em Kg: '))
maca_kg = float(input('Digite a quantidade de Maçãs adquiridos em Kg: '))

frutas(morango_kg, maca_kg)