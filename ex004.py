# Faça um programa que leia pelo teclado e mostre na tela o seu tipo primitivo e todos as informações possíveis sobre ela

n = input('digite o valor para reconhecimento ')

print('O tipo primitivo é', type(n))
print('É espaço?', n.isspace())
print('é um número?', n.isnumeric())
print('É alfebetico', n.isalpha())
print('é alfanumerico', n.isalnum())
print('é Maiusculo', n.isupper())
print('é minusculo', n.islower())
print('é TItulo', n.istitle())

