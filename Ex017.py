#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
'''o = float(input('Comprimento do cateto oposto: '))
a = float(input('Comprimento do cateto adjacente: '))
h = (o ** 2 + a ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(h))'''
'''import math
o = float(input('Comprimento do cateto oposto: '))
a = float(input('Comprimento do cateto adjacente: '))
h = math.hypot(o, a)
print('A hipotenusa vai medir {:.2f}'.format(h))'''
from math import hypot
o = float(input('Comprimento do cateto oposto: '))
a = float(input('Comprimento do cateto adjacente: '))
h = hypot(o, a)
print('A hipotenusa vai medir {:.2f}'.format(h))
