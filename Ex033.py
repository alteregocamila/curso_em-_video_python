#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))

'''lista = [a, b, c]
print('O maior número é {}.'.format(max(int(number) for number in lista)))
print('O menor número é {}.'.format(min(int(number) for number in lista)))'''

#Verificar quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior  = c
print('O menor número é {}.'.format(menor))
print('O maior número é {}.'.format(maior))

