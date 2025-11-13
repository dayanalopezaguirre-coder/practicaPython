numero_tabla = 0
print("bienvenido a la tabla de multiplicar")
numero_tabla = int(input ("ingrese el numero de la tabla que desea ver: "))
#validacion de datos y proceso i=
if (numero_tabla < 1 or numero_tabla > 10):
    print("Error: el numero ingresado no es valido, por favor ingrese un numero entre 1 y 10")
elif (numero_tabla == 1):
    print("apoco no sabes la tabla ")
elif (numero_tabla == 7):
    print("buena eleccion, la tabla del 7 es la mejor")
else:
    print("tabla de multiplicar del numero", numero_tabla)
    #impresion de tabla de multiplicar
    for i in range (1, 11):
         print(numero_tabla, "x", i, " = ",numero_tabla * i)
print("gracias por usar el programa")