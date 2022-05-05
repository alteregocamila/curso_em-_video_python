#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).strip().upper()
print('Nessa frase tem {} A que aparece a primeira vez na posição {} e a ultima vez na posição {}.'.format(frase.count('A'), frase.find('A')+1, frase.rfind('A')+1))
