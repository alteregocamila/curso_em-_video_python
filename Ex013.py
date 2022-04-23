#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite o seu salário: R$ '))
aumento = salario + (salario * 15 / 100)
print('Seu salário de R$ {} com o aumento de 15% passa a ser R$ {}'.format(salario, aumento))
