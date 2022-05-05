#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('Digite um número inteiro: '))
resultado = num % 2 # O resto da divisão de qualquer número PAR por 2 é 0 e de qualquer número IMPAR é 1.
if resultado == 0:
    print('Esse número é PAR.')
else:
    print('Esse número é IMPAR.')