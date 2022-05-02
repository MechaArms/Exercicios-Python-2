#Exercício 21
'''
Faça um Programa para um caixa eletrônico. 
O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
O valor mínimo é de 10 reais e o máximo de 600 reais. 
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
'''
saque = int(input("digite o valor de saque: "))

if 10 <= saque <=600:
    cem = saque//100
    cinquenta = (saque%100)//50
    dez = ((saque%100)%50)//10
    cinco = (((saque%100)%50)%10)//5
    um = ((((saque%100)%50)%10)%5)//1

    print(um, "- notas de 1")
    print(cinco, "- notas de 5")
    print(dez, "- notas de 10")
    print(cinquenta, "- notas de 50")
    print(cem, "- notas de 100")

else:
    print("valor fora do intervalo, digite um valor entre [10 e 600] reais")

'''
Exemplo 256 reais
saque/100 = 2.56
saque//100 = 2
saque%100 = 56
(saque%100)//50 = 1
((saque%100)%50)//10 = 0
(((saque%100)%50)%10)//5 = 1
((((saque%100)%50)%10)%5)//1 = 1
'''