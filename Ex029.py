#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
km = float(input('Digite a sua velocidade: '))
multa = (km - 80) * 7
if km > 80:
    print('Você foi multado! Sua multa custará R$ {:.2f}'. format(multa))
else:
    print('PARABÉNS! Você está dentro do limite de velociade.')