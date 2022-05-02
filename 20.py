#Exercício 20
'''
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
    a - A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    b - A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    c - A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''
nota1 = int(input('Digite a primeira nota do aluno: '))
nota2 = int(input('Digite a segunda nota do aluno: '))
nota3 = int(input('Digite a terceira nota do aluno: '))

media = (nota1 + nota2 + nota3) / 3

if media >= 7 and media < 10:
    print(f'Média: {media} - Aprovado')
elif media == 10:
    print(f'Média: {media} - Aprovado com Distinção')
else:
    print(f'Média: {media} - Reprovado')