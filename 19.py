#Exercício 19
'''Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
    Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''

def leitura(num):
    lista = []
    for casa in str(num):
        lista.append(casa)
    print(lista) #checagem da lista

    if len(lista) == 1:
        unidade = lista[0]
        print(f'unidade(s): {unidade}')
    
    elif len(lista) == 2:
        dezena = lista[0]
        unidade = lista[1]
        print(f'dezena(s): {dezena} // unidade(s): {unidade}')
    
    elif len(lista) == 3:
        centena = lista[0]
        dezena = lista[1]
        unidade = lista[2]
        print(f'centena(s): {centena} // dezena(s): {dezena} // unidade(s): {unidade}')
    else:
        print(f'O numero {num} é invalido')
        
    
numero = input("digite um numero menor que 1000: ")

leitura(numero)