#exercício 3
#Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''
A primeira linha do código "# -*- coding: latin-1 -*" é para podermos usar todos os caracteres da língua portuguesa. 
Se não colocarmos o coding: latin-1 ou utf-8 teremos erro quando usarmos: "´", "~", "^"... em nossas strings.
'''

# -*- coding: latin-1 -* 

sexo = str(input('Digite (F)-Feminino, (M)-Masculino: ').upper())
if sexo == 'M':
    print('Sexo Masculino.')
elif sexo == 'F':
    print('Sexo Feminino.')
else:
    print('Sexo Inválido.')