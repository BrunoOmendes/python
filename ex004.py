algo = input('Digite alguma coisa: ')
print(' O tipo primitivo desse algo é: ', type(algo))
print('Apenas possui espaços?'.format(algo.isspace()))
print('É um numero?'.format(algo.isnumeric()))
print('É alfanumerico?'.format(algo.isalnum()))
print('É apenas uma palavra?'.format(algo.isalpha()))
print('Está em Caixa baixa?'.format(algo.islower()))
print('Está capitalizado? {}'.format(algo.isupper()))


