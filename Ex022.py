# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome = str(input('Escreva seu nome: '))
print('Em letras minúsculas: ', nome.lower())
print('Em letras maiúsculas: ', nome.upper())
print('Seu nome tem ', len(nome), 'letras.')
print('Seu nome tem ', len(nome) - nome.count(' '), 'letras sem espaços.')

# pri_nome = nome.split(' ')[0]
# print('Seu primeiro nome tem ', len(pri_nome), 'letras.')
print('Seu nome tem ao todo {} letras'.format(nome.find(' ')))
