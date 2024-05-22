#!/usr/bin/env python
# coding: utf-8

# In[75]:


# 1. Mostrar si los tres valores son iguales o no.
# 2. Mostrar los números en orden descendente. También debe funcionar para números duplicados.
# 3. Solo podrá utilizar los operadores, sentencia if(anidada), símbolos y funciones vistos en clase.
# 4. El resultado de salida debe ser idéntico al mencionado en este examen.

n1 = int(input('Ingrese el primer numero: '))
n2 = int(input('Ingrese el segundo numero: '))
n3 = int(input('Ingrese el tercer numero: '))

# sacar el menor
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
    
# sacar el mayor
mayor = n1
if n2 > mayor:
    mayor = n2
if n3 > mayor:
    mayor = n3
    
# sacar el del medio
medio = n2;
if n1 != menor:
    if n1 != mayor:
        medio = n1
if n2 != menor:
    if n2 != mayor:
        medio = n2
if n3 != menor:
    if n3 != mayor:
        medio = n3
        
# si no son iguales
if mayor == medio != menor:
    print('Los valores',mayor ,medio,'y', menor, 'no son iguales.')
    print('El orden de los numeros en forma descendiente son: ', mayor, medio,'y', menor)
if mayor != medio == menor:
    print('Los valores',mayor ,medio,'y', menor, 'no son iguales.')
    print('El orden de los numeros en forma descendiente son: ', mayor, medio,'y', menor)
if mayor != medio != menor:
    print('Los valores',mayor ,medio,'y', menor, 'no son iguales.')
    print('El orden de los numeros en forma descendiente son: ', mayor, medio,'y', menor)

# si son iguales
if mayor == medio == menor:
    print('Todos los numeros son iguales, por lo tanto no es importante mostrar su orden.')


# In[74]:


# Normalmente caben 6 huevos en una cartera. Escribe un script para calcular la cantidad de cajas que necesita un granjero para
# almacenar 28 huevos. El script también determinará cuántos huevos se colocan en la última cartera sin completar y cuántos
# huevos adicionales se necesitan para llenar esta última cartera.

# Se le solicita al usuario ingresar un valor(números enteros) y desplegar como resultado lo siguiente:
# 1. Los datos de salida deben ser idénticos a los mencionados en las imágenes de abajo de este examen.
# 2. Solo podrá utilizar los operadores, sentencia if(estructura de selección if sencilla), símbolos y funciones integradas
# vistas en clase.
# 3. Podrá anidar la sentencia de selección if sencillas en este ejercicio.huevos = int(input('Ingresa la cantidad de huevos obtenidos:'))

huevos = int(input('Ingrese la cantidad de huevos obtenidos:'))

if huevos <= 5:
    print('La cantidad de huevos que se necesitan para llenar una cartera es de:', 6 - huevos,'.')
    
if huevos == 6:
    print('Se lleno 1 cartera de 6 huevos.')
if huevos >= 7:
    if huevos <= 11:
        print('Se lleno 1 cartera de 6 huevos.')
        print('En la ultima cartera se colocaron', huevos - 6,'huevos.')
        print('La cantidad de huevos adicionales que se necesitan para llenar la ultima cartera es de:', 6 - (huevos - 6), '.')
        
if huevos == 12:
    print('Se llenaron 2 carteras de 6 huevos.')
if huevos >= 13:
    if huevos <= 17:
        print('Se llenaron 2 carteras de 6 huevos.')
        print('En la ultima cartera se colocaron', huevos - 12,'huevos.')
        print('La cantidad de huevos adicionales que se necesitan para llenar la ultima cartera es de:', 6 - (huevos - 12), '.')
        
if huevos == 18:
    print('Se llenaron 3 carteras de 6 huevos.')
if huevos >= 19:
    if huevos <= 23:
        print('Se llenaron 3 carteras de 6 huevos.')
        print('En la ultima cartera se colocaron', huevos - 18,'huevos.')
        print('La cantidad de huevos adicionales que se necesitan para llenar la ultima cartera es de:', 6 - (huevos - 18), '.')
        
if huevos == 24:
    print('Se llenaron 4 carteras de 6 huevos.')
if huevos >= 25:
    if huevos < 29:
        print('Se llenaron 4 carteras de 6 huevos.')
        print('En la ultima cartera se colocaron', huevos - 24,'huevos.')
        print('La cantidad de huevos adicionales que se necesitan para llenar la ultima cartera es de:', 6 - (huevos - 24), '.')
        
if huevos >= 29:
    print('Se cumplieron con los 28 huevos que se ocupaban almacenar, gracias.')

