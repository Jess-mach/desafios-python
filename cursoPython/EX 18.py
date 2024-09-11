import math
angulo = float(input('Digite um valor para o ângulo:'))
rad = math.radians(angulo)
seno = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print('Ângulo:{}\nSeno:{:.2f}\nCosseno:{:.2f}\nTangente:{:.2f}'.format(angulo, seno, cos, tan))
