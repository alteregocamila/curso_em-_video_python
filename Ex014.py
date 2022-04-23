#Escreva um programa que converta uma temperatura digitada em graus Celsius e converta para graus Fahrenheit.
c = float(input('Informe a temperatura em ºC: '))
f = ((c * 9) / 5) + 32
print('A temperatura de {} ºC corresponde a {} ºF!'.format(c, f))
