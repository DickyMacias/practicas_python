# Ángulos de un triangulo
## Usando la ley de cosenos se ingresa un valor para cada lado del triangulo

# Se importan desestructurados los metodos de la librería math para usarlos con la ley de cosenos.
from math import acos, degrees

#Se guarda una cadena de texto con los valores interpolados y salto de linea.
valores_lados = 'Los valores escogidos fueron: \nA = {lado_a} \nB = {lado_b} \nC = {lado_c}\n'

#Se reciben los valores a variables flotantes.
lado_a = float(input('Ingresa un valor númerico para el lado A: '))
lado_b = float(input('Ingresa un valor númerico para el lado B: '))
lado_c = float(input('Ingresa un valor númerico para el lado C: '))

#Se muestran los valores usando la interpolación y casteados a string.
print(valores_lados.format(lado_a = str(lado_a), lado_b = str(lado_b), lado_c = str(lado_c)))

#Se realizan las operaciones con los métodos importados.
angulo_a = degrees(acos((lado_b**2 + lado_c**2 - lado_a**2)/(2 * lado_b * lado_c)))
angulo_b = degrees(acos((lado_c**2 + lado_a**2 - lado_b**2)/(2 * lado_c * lado_a)))
angulo_c = degrees(acos((lado_a**2 + lado_b**2 - lado_c**2)/(2 * lado_a * lado_b)))

valores_angulos = 'Los valores de los ángulos son: \nA = {angulo_a} \nB = {angulo_b} \nC = {angulo_c}\n'

#Se usa el redondeo ya que el valor es flotante y no se puede acortar con slice.
print(valores_angulos.format(angulo_c = str(round(angulo_c, 2)), angulo_a = str(round(angulo_a, 2)), angulo_b = str(round(angulo_b, 2))))

#Se usa la concatenación de valores.
print('La suma de los ángulos es igual a ' + str(angulo_a + angulo_b + angulo_c))

