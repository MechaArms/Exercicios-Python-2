#exercício 7
#Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 > num2 and num1 > num3:
    print(f'O maior é {num1}')
elif num2 > num1 and num2 > num3:
    print(f'O maior é {num2}')
else:
    print(f'O maior é {num3}')

if num1 < num2 and num1 < num3:
    print(f'O menor é {num1}')
elif num2 < num1 and num2 < num3:
    print(f'O menor é {num2}')
else:
    print(f'O menor é {num3}')