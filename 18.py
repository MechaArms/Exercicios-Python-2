#Exercício 18
#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

dia = int(input('Digite o dia: '))
if dia > 0 and dia <= 31:
    mes = int(input('Didite o mês: '))
    if mes > 0 and mes <= 12:
        ano = int(input('Digite o ano: '))
        if ano >= 0 and ano <= 9999:
            print(f'O formato da data {dia}/{mes}/{ano} é valido')
        else:
            print('O ano é invalido')
    else:
        print('O mes é invalido')
else:
    print('O dia é invalido')