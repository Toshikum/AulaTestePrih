#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
#e todas as informações possiveis sobre ele.

n = input('Digite qualquer coisa')

print(type(n))
print('Isso que você escreveu é númerico? {}'.format(n.isnumeric()))
print('Isso que você escreveu é letra? {}'.format(n.isalpha()))
print('Isso que você escreveu é alphanumerico? {}'.format(n.isalnum()))
