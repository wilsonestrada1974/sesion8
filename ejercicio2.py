#convertir la cantidad de dolares ingresados por el usuario a pesos colombianos y mostrar en pantalla

print("Para convertir de dolares americanos a pesos marque 1, para convertir de pesos a dolares marque 2")
opcion=int(input())

if opcion == 1:

    print("por favor ingrese la cantidad de dolares a convertir:")
    dolares=float(input())
    print("la tasa de cambio es: 1 dolar = $3850.25 COP.  Desea aceptar esa tasa?  s/n")
    desicion=input()
    if desicion == "s":
        pesos=dolares*3850.25
        print("los ",dolares," dolares, equivalen a ",pesos," pesos")
    else:
        print("no se realiza la conversion")
else:
    if opcion ==2:
        print("por favor ingrese la cantidad de pesos a convertir")
        pesos=int(input())
        print("la tasa de cambio es 0.00026 dolares por cada peso colombiano.    Desea aceptar esa tasa?  s/n")
        desicion=input()
        if desicion == "s":
            dolares=pesos*0.00026
            print("los ",pesos," pesos, equivalen a ", dolares, " dolares americanos") 
        else:
            print("no se realiza la conversion")       
    else:
        print("opcion no valida")             

