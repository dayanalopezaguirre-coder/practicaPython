#declaracion de variables
bandera = 0
numero1 = 0
numero2 = 0
#FUNCION SUMAR
def sumar():
    #impresion de resultado
    print("El resultado de la suma es:", numero1 + numero2)

#FUNCION RESTAR
def restar():
    #impresion de resultado
    print("El resultado de la resta es:", numero1 - numero2)

#funcion multiplicar
def multiplicar():
    #impresion de resultado
    print("El resultado de la multiplicación es:", numero1 * numero2)

#funcion dividir
def dividir():  
        #impresion de resultado
        print("El resultado de la división es:", numero1 / numero2)  


print("bienvenido al programa calculadora")
while bandera != 5:
    print("listado de opcines:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir") 
    print("5. Salir")
    bandera = int(input("Seleccione una opción 1-5: "))
    if bandera >= 1 and bandera <= 4:
        numero1= int(input("Ingrese el primer número: "))
        numero2= int(input("Ingrese el segundo número: "))
    if bandera == 1:
        sumar()
    elif bandera == 2:
        restar()
    elif bandera == 3:
        multiplicar()
    elif bandera == 4:
        dividir()
    elif bandera == 5:
        print("Gracias por usar la calculadora. ¡Hasta luego!")
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

    
   