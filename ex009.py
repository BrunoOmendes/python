largura = float(input('Insira a largura de sua parede em metros: '))
altura = float(input('Agora insira a altura de sua parede: '))
area = largura * altura
tinta = area / 2
print('As dimensões de sua pare é {}m x {}m e a área da parede é: {}m²'.format(largura, altura, area))
print('A quantidade de latas de tintas para pintar sua parede será de: {}L de tinta'.format(area / 2))
