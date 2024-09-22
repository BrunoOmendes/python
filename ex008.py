din = float(input('Coloque quanto dinheiro você possui em R$ em sua carteira: '))
contd = float(input('Coloque a cotaçao do dolar: '))
conteu = float(input('Coloque a cotação do euro'))
contyuan = float(input('Coloque a cotação do yen chines'))
d = din/contd
eu = din/conteu
yuan = din/contyuan
print('Seu dinheiro em R${:.2f} em sua carteira em dolar será de: ${:.2f}'.format(din,d))
print('Em euro será de: €{:.2f}'.format(eu))
print('E em yuan chines será de: ¥{:.2f}'.format(yuan))
