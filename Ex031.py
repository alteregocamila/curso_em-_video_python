#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
distancia = float(input('Qual a distância em KM da viagem? '))

'''A = distancia * 0.5
B = distancia * 0.45
if distancia < 200:
    print('O valor da sua passagem será R$ {:.2f}'.format(A))
else:
    print('O valor da sua passagem será R$ {:.2f}'.format(B))'''

print('Você está prestes a começar uma viagem de {} km'.format(distancia))
preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagems será de R$ {:.2f}'.format(preco))
