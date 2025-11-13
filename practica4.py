nombre =[]
cantidad = []
precio = []
bandera = "si"
while bandera  == "si":
    n = input("ingrese el nombre de productos a registrar: " )
    p = float(input("ingrese el precio del producto: " ))
    c = int(input("ingrese la cantidad de productos a registrar: " ))
    nombre.append (n)   
    precio.append (p)
    cantidad.append (c) 
    bandera = input("desea agregar otro producto? si/no: ").lower()

print("======================================================")
print("=                LISTADO DE PRODUCTOS                =")
print("======================================================")
print("= productos | cantidad  |  precio unitario  | total  =")
print("------------------------------------------------------")
#print("-   Manzana     |   10     |   $10.00    |  $100.00  -")
for i in range(len(nombre)):
    print(f"- {nombre[i]:<12}|{cantidad[i]:<10}|{precio[i]:<17}|{cantidad[i] * precio[i]}-")
    #print("-", nombre[i],"|",cantidad[i],"|",precio[i],"|",cantidad[i] * precio[i],"-")