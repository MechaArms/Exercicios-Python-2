#Exercício 24
'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
    a. par ou ímpar;
    b. positivo ou negativo;
    c. inteiro ou decimal.
'''

def par_impar(num):
    if num % 2 == 0:
        print("Par")
    else:
        print("Impar")

def positivo_negativo(num):
    if num > 0:
        print("Positivo")
    else:
        print("Negativo")

def inteiro_decimal(num):
    if num == round(num):
        print("Inteiro")
    else:
        print("Decimal")

num = float(input("Numero original: "))

par_impar(num)
positivo_negativo(num)
inteiro_decimal(num)