# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

string_original = input('Digite uma string para ser invertida: ')

string_invertida = string_original[::-1]

print('String invertida:', string_invertida)