#exercício 9
#Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

lista = [n1, n2, n3]
lista.sort(reverse=True)
print(lista)