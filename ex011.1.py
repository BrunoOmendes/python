pc = float(input('Insira o preço atual do produto: R$'))
ds = pc - (pc * 10/100)
aumento = pc + (pc * 10/100)
print('O produto vale o seguinte preço: R${}'.format(pc))
print('Se comprar a vista o produto terá um desconto de 10% e valerá: R${}'.format(ds))
print('Se comprar parcelado tera um juros de 10% e valerá: R${}'.format(aumento))