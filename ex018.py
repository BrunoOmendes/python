import math
from math import sin, cos, tan
angulo = int(input("Digite um ângulo para ver seu seno, tangente e cosseno: "))
seno = sin(math.radians(angulo))
cos = cos(math.radians(angulo))
tan = tan(math.radians(angulo))
print("O seno do angulo {} é {:.2f}".format(angulo, seno))
print("O cosseno do angulo {} é {:.2f}".format(angulo, cos))
print("A tangente do angulo {} inserido é {:.2f}".format(angulo, tan))
