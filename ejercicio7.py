#calcular y mostrar en pantalla la sombra de un edicifio de 20 metros cuando el angulo que forman los rayos del sol con el suelo son de 22 grados

import math

altura= 20
angulo=22
base=altura/math.atan(angulo)
print("La sombra es de ","{:.2f}".format(base)," metros")