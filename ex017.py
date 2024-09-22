from math import pow, sqrt
catetoop = float(input("Insira a medida do cateto oposto: "))
catetoadj = float(input("Insira a medida do cateto adjacente: "))
hipotenusa = sqrt(pow(catetoa, 2) + pow(catetob, 2))

print("A hipotenusa do seu triangulo, o maior lado, vale: {:.2f}".format(hipotenusa))