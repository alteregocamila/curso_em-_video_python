#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
n = str(input('Digite o seu nome completo: '))
nome = n.strip().upper().split()
print('O seu primeiro nome é {} e o seu último nome é {}'.format(nome[0], nome[len(nome)-1]))

