lista = []
temp=''
items = []
ListaCompra=["Aguacate","Pepino","Rabano","Piedra","Coca","Chiles","Huevos","Katsup","Cafe","Arroz"]

with open("Lista_De_Compras.txt", "r") as fa:
       for linea in fa:
           lista.append(linea.strip())
while True:
    for i in range(len(lista)):
        print(lista[i])
    elment = input("ELIJE ALGO DE LA LISTA TONOTO: ")

    band=0
    for c in lista:
        if elment == c:
            items.append(c)
            lista.remove(c)
            band=0
            break
        else:
            band=1


    if len(items)==10:
        print("Haz terminado de hacer las compras ")
        break
    
    if band == 1:
        print("Articulo no encontrado")
        a=input("Ingresa una tecla para continuar: ")

for i in range(len(ListaCompra)):
    if items[i] != ListaCompra[i]:
        print("Esto no lo que te pedi. No eres un papu pro >:(")
        break

if i==9:
    print("FELICIDADES PAPU PRO HCISTE LO QUE TE PEDI BV")




