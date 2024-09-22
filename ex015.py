km = float(input('Insira a quantidade de km rodados com o respectivo carro alugado: '))
dias = int(input('Insira quantos dias o carro foi ultilizado: '))
pc = (60 * dias) + (0.15 * km)
print('O preço total a ser pago pelo aluguel do carro será de R${:.2f}'.format(pc))
