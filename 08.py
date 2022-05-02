#exercício 8
#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

prod1 = float(input("Digite o preço do primeiro produto: R$ "))
prod2 = float(input("Digite o preço do segundo produto: R$ "))
prod3 = float(input("Digite o preço do terceiro produto: R$ "))

if prod1 < prod2 and prod1 < prod3:
    print(f'O melhor preço é de R$ {prod1}')
elif prod2 < prod1 and prod2 < prod3:
    print(f'O melhor preço é de R$ {prod2}')
else:
    print(f'O melhor preço é de R$ {prod3}')