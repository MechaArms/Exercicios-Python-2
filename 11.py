#exercício 11
'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    + salários até R$ 280,00 (incluindo) : aumento de 20%
    + salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    + salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    + salários de R$ 1500,00 em diante : aumento de 5% 
Após o aumento ser realizado, informe na tela:
    + salário antes do reajuste;
    + percentual de aumento aplicado;
    + valor do aumento;
    + novo salário, após o aumento.
'''

'''
20% ==== se < 280
15% ==== se >= 280 e < 700
10% ==== se >= 700 e < 1500
 5% ==== se >= 1500
'''

sal = float(input("Digite o seu salário: R$ "))
rj = 0
nv_sal = 0
va = 0

print(f'+salário antes do reajuste R$ {sal}')

if sal >= 1 and sal <= 280:
    rj = ((100 + 20) / 100) * sal # 20% salario
    nv_sal += rj
    va = rj - sal
    print(f'+percentual de aumento aplicado é de 20%')
    print(f'+valor do aumento é de R$ {round(va)}')
    print(f'+novo salário, após o aumento é de R$ {round(nv_sal)}')
elif sal > 280 and sal <= 700:
    rj = ((100 + 15) / 100) * sal # 15% salario
    nv_sal += rj
    va = rj - sal
    print(f'+percentual de aumento aplicado é de 15%')
    print(f'+valor do aumento é de R$ {round(va)}')
    print(f'+novo salário, após o aumento é de R$ {round(nv_sal)}')
elif sal > 700 and sal <= 1500:
    rj = ((100 + 10) / 100) * sal # 10% salario
    nv_sal += rj
    va = rj - sal
    print(f'+percentual de aumento aplicado é de 10%')
    print(f'+valor do aumento é de R$ {round(va)}')
    print(f'+novo salário, após o aumento é de R$ {round(nv_sal)}')
elif sal > 1500:
    rj = ((100 + 5) / 100) * sal # 5% salario
    nv_sal += rj
    va = rj - sal
    print(f'+percentual de aumento aplicado é de 5%')
    print(f'+valor do aumento é de R$ {round(va)}')
    print(f'+novo salário, após o aumento é de R$ {round(nv_sal)}')
else:
    print('Valor Inválido.')