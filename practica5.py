lista_frutas =[]
bandera = "si"
while bandera  == "si":
    n = input("ingrese el nombre de productos a registrar: " )
    p = float(input("ingrese el precio del producto: " ))
    c = int(input("ingrese la cantidad de productos a registrar: " ))
    fruta = {
        "nombre": n,
        "precio": p,
        "cantidad": c
    }
    lista_frutas.append(fruta)
    bandera = input("desea agregar otro producto? si/no: ").lower()

print("======================================================")
print("=                LISTADO DE PRODUCTOS                =")
print("======================================================")
print("= productos | cantidad  |  precio unitario  | total  =")
print("------------------------------------------------------")

for fruta in lista_frutas:
    print(f"- {fruta['nombre']:<12}|{fruta['cantidad']:<10}|{fruta['precio']:<17}| {fruta['cantidad'] * fruta['precio']:<11}")
   