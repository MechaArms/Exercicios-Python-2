#Exercício 16
'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
    A - Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
    B - Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    C - Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    D - Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''
# (-b² +- Raiz(Delta)) / 2*a
# Delta = b² - (4*a*c)

import math

a = int(input('digite o numero de a: '))

if a == 0:
    print('o valor de A igual a zero, a equação não é do segundo grau')
else:
    b = int(input('digite o numero de b: '))
    c = int(input('digite o numero de c: '))
    
    delta = (math.pow(b,2) - (4*a*c))

    if delta < 0:
        print(f"delta = {delta} a equacao nao possui raizes reais")
    elif delta == 0:
        print(f"delta = {delta} a equacao possui uma raiz")
        raiz = ((-1)*b + math.sqrt(delta))/(2*a)
        print(f"raiz da equacao = {raiz}")
    else:
        print(f"delta = {delta} a equacao possui duas raizes")
        raiz1 = ((-1)*b + math.sqrt(delta))/(2*a)
        raiz2 = ((-1)*b - math.sqrt(delta))/(2*a)
        print(f"raiz 1 da equacao = {raiz1}")
        print(f"raiz 2 da equacao = {raiz2}")