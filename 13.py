#exercício 13
#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), 
#se digitar outro valor deve aparecer valor inválido.

#==Metodo Simples==

dia = int(input('Digite um número de (1 a 7): '))

if dia == 1:
    print('Domingo')
elif dia == 2:
    print('Segunda')
elif dia == 3:
    print('Terça')
elif dia == 4:
    print('Quarta')
elif dia == 5:
    print('Quinta')
elif dia == 6:
    print('Sexta')
elif dia == 7:
    print('Sabado')
else:
    print('valor iválido')
    
#==Metodo Complexo==

dia_semana = int(input('Digite um número de (1 a 7): '))

def verificadia_semana(dia_semana):
    dicionario_dia_semana = {1: 'domingo', 2: 'segunda', 3: 'terça', 4: 'quarta', 5: 'quinta', 6: 'sexta', 7: 'sabado'}
    for dia in dicionario_dia_semana.keys():
        if dia_semana == dia:
            print('->',dicionario_dia_semana[dia].capitalize())
            break
    else:
        print('Dia não encontrando')

verificadia_semana(dia_semana)