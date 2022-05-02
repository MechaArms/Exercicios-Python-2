#exercício 12
'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
mas não é descontado (é a empresa que deposita). 
O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
'''

# -*- coding: latin-1 -*-
valor_hora = float(input('Digite o valor da hora de trabalho: '))
quant_hora_trabalhada = float(input('Digite a quantidade de hora trabalhada no mês: '))
salario_bruto = (valor_hora*quant_hora_trabalhada)


def descontos(salario_bruto):
    desc_sindicato = (salario_bruto/100)*3
    fgts = (salario_bruto/100)*11
    ir = 0
    if salario_bruto <= 900:
        salario_liquido = salario_bruto - desc_sindicato
        
    elif salario_bruto <= 1500:
        ir = (salario_bruto/100)*5
        salario_liquido = salario_bruto - desc_sindicato - ir
        
    elif salario_bruto <= 2500:
        ir = (salario_bruto/100)*10
        salario_liquido = salario_bruto - desc_sindicato - ir
        
    else:
        ir = (salario_bruto/100)*20
        salario_liquido = salario_bruto - desc_sindicato - ir
        
    imprime_desconto(salario_bruto, desc_sindicato, ir, fgts, salario_liquido)

def imprime_desconto(salario_bruto, desc_sindicato, ir, fgts, salario_liquido):
    print('''
    Salario Bruto: %.2f
    Desconto Sindicato: %.2f
    Desconto IR: %.2f
    FGTS: %.2f
    
    Salario Liquido: %.2f
    '''%(salario_bruto, desc_sindicato, ir, fgts, salario_liquido))

descontos(salario_bruto)