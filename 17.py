#Exercício 17
#Faça um Programa que peça um número correspondente a um determinado ano 
#e em seguida informe se este ano é ou não bissexto

# -*- coding: latin-1 -*-
ano = int(input("digite um ano (XXXX): "))
if (ano % 4 == 0 and ano % 100!= 0) or ano % 400 == 0:
    print(f' {ano} O ano informado é Bissexto')
else:
    print(f' {ano} O ano informado não é bissexto')