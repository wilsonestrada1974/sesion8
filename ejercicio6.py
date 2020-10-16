#calcular el numero de vueltas que da una llanta en 1 kilometro si el diametro de la lanta es 50cm.

diametro=50
distancia=100000
pi=3.141592
perimetro=pi*diametro
vueltas=distancia/perimetro
print("la rueda da ", "{:.2f}".format(vueltas), "en 1 kilometro")