# convertir los grados celsius a grados farenheit

print("Para convertir de grados Celsius a Farenheit marque 1, para convertir de Farenheit a Celsius marque 2")
opcion = int(input())

if opcion == 1:

    print("por favor ingrese los grados Celsius a convertir:")
    celsius = float(input())
    farenheit = (celsius*9/5) + 32
    print("los ", celsius, " grados Celsius ,equivalen a ",farenheit, " grados Farenheit")

elif opcion == 2:
    print("por favor ingrese los grados Farenheit a convertir")
    farenheit = int(input())
    celsius=(farenheit-32)*5/9
    print("los ", farenheit, " grados Farenheit ,equivalen a ",celsius, " grados Celsius")

else:
    print("opcion no valida")             

