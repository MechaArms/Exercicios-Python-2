#Exercício 15
'''
Faça um Programa que peça os 3 lados de um triângulo. 
O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
-Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
-Triângulo Equilátero: três lados iguais;
-Triângulo Isósceles: quaisquer dois lados iguais;
-Triângulo Escaleno: três lados diferentes;
'''
#Triângulo Equilátero: a = b and a = c and b = c
#Triângulo Isósceles: a = b or a = c or b = c
#Triângulo Escaleno: a != b and a != c and b != c

a = int(input('digite o valor do primeiro lado do triângulo: '))
b = int(input('digite o valor do segundo lado do triângulo: '))
c = int(input('digite o valor do terceiro lado do triângulo: '))

if a == b and a == c and b == c:
    print('O Triângulo é Equilátero')
elif a == b or a == c or b == c:
    print('O Triângulo é Isósceles')
else:
    print('O Triângulo Escaleno')