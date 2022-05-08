#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
a = float(input('Digite o comprimento de uma reta: '))
b = float(input('Digite outro comprimento de uma reta: '))
c = float(input('Digite mais um comprimento de uma reta: '))
if a < b + c and b < a + c and c < a + b:
    print('Os comprimentos informados PODEM formar um Triângulo.')
else:
    print('Os comprimentos informados NÃO PODEM formar um Triângulo.')
