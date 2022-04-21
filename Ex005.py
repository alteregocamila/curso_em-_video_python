#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
num = int(input('Digite um número inteiro: '))
#a = num - 1
#s = num + 1
#print('O antecessor de {} é {} e seu sucessor é {}.'.format(num, a, s))
print('Analizando o valor {}, seu antecessor é {} e seu sucessor é {}.'.format(num, (num-1), (num+1)))
