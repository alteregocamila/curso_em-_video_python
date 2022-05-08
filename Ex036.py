#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Qual o valor do imóvel? R$ '))
salario = float(input('Qual o seu salário bruto? R$ '))
prazo = int(input('Em quantos anos pretende quitar o valor do imóvel? '))

credito = valor / (prazo * 12)
#print(credito)
a = salario * 0.30
#print(a)
if credito > a:
    print('Para comprar uma casa no valor de R$ {:.2f} a prestação mensal será de R$ {:.2f}. Seu crédito não foi aprovado!'.format(valor, credito))
else:
    print('Para comprar uma casa no valor de R$ {:.2f} a prestação mensal será de R$ {:.2f}. Seu crédito foi aprovado!'.format(valor, credito))

