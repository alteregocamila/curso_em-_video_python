#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = float(input('Valor do produto: R$ '))
np = p - (p * 5 / 100)
print('O preço do produto com 5% de desconto é R$ {}'.format(np))

