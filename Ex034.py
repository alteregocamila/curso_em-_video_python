#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Qual o seu salário atual: R$ '))
a = salario + (salario * 0.10)
b = salario + (salario * 0.15)
if salario > 1250:
    print('O seu salário de {:.2f} passará a ser {:.2f} com o aumento de 10%.'.format(salario, a))
if salario <= 1250:
    print('O seu salário de {:.2f} passará a ser {:.2f} com o aumento de 15%.'.format(salario, b))
