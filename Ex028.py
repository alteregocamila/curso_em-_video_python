#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''import random
resposta = str(input('Eu pensei em um número de 0 a 5. Qual número eu pensei? ')).strip()
n = 0
n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5
lista = [n, n1, n2, n3, n4, n5]
escolhido = str(random.choice(lista))
if escolhido == resposta:
    print('Nascemos um para o outro! Você acertou! Pensei em {}.'.format(escolhido))
else:
    print('Que pena, você não acertou! Pensei em {}.'.format(escolhido))'''

from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador sortear um número de 0 a 5
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) #Jogador inseri um número
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}.'.format(computador, jogador))