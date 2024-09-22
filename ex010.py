pc = float(input('Preço do produto: R$ '))
ds = float(input('Coloque o desconto do cupom'))
pcds = pc - (pc * ds / 100)
print('O preço atual do produto é: R${:.2F}, O preço com o desconto aplicado é: R${:.2F}'.format(pc, pcds))
