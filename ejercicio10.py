print("ingrese la nota de Español")
español=float(input())
print("Ingrese la nota de Matematicas")
matematicas=float(input())
print("ingrese la nota de Economia")
economia=float(input())
print("ingrese la nota de programacion")
programacion=float(input())
print("Ingrese la nota de Ingles")
ingles=float(input())

promedio=(español+matematicas+economia+programacion+ingles)/5

print("el promedio de todas las materias es", "{:.2f}".format(promedio))