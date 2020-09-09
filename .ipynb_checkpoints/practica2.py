

from math import acos, degrees, sqrt
import random

valores_lados = 'Los valores escogidos fueron: \nA = {lado_a} \nB = {lado_b} \nC = {lado_c}\n'

lado_a = round(float(random.randint(1,100)),2)
lado_b = round(float(random.randint(1,100)),2)
lado_c = round(float(sqrt((lado_a**2 + lado_b**2))),2)

print(valores_lados.format(lado_a = str(lado_a), lado_b = str(lado_b), lado_c = str(lado_c)))

def calcular_angulos(value_1,value_2,value_3):
    return degrees(acos((value_2**2 + value_3**2 - value_1**2)/(2 * value_2 * value_3)))

angulo_a = calcular_angulos(value_1=lado_a, value_2=lado_b, value_3=lado_c)
angulo_b = calcular_angulos(value_1=lado_b, value_2=lado_c, value_3=lado_a)
angulo_c = calcular_angulos(value_1=lado_c, value_2=lado_a, value_3=lado_b)

valores_angulos = 'Los valores de los ángulos son: \nA = {angulo_a} \nB = {angulo_b} \nC = {angulo_c}\n'

print(valores_angulos.format(angulo_c = str(round(angulo_c, 2)), angulo_a = str(round(angulo_a, 2)), angulo_b = str(round(angulo_b, 2))))

if (angulo_a + angulo_b + angulo_c) == 180:
    print('La suma de los ángulos es igual a', angulo_a + angulo_b + angulo_c)
elif (angulo_a + angulo_b + angulo_c) != 180:
    print('La suma de los angulos es', angulo_a + angulo_b + angulo_c)
