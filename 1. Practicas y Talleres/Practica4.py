#!/usr/bin/env python
# coding: utf-8

# In[24]:


## 18 ##
# Enteros del 1 al 5 ascendente, decrementando en 1.

numero = 0

while numero < 5:
    numero = numero + 1
    print(numero)


# In[29]:


## 19 ##
# Enteros del 1 al 5 descendente, decrementando en 1.

numero = 5

while numero > 0:
    print(numero)
    numero = numero - 1


# In[32]:


## 20 ##
# Enteros del 1 al 5 ascendente, decrementando en 1.

numero = 0

while numero < 5:
    numero = numero + 1
    print(numero, end = ',')


# In[30]:


## 21 ##
# Enteros del 1 al 5 descendente, decrementando en 1.

numero = 5

while numero > 0:
    print(numero, end = ',')
    numero = numero - 1


# In[47]:


## 22 ##
# Sumatoria calculada con el numero ingresado: osea si pongo 5 es 15

numero = int(input('Ingresar numero entero para obtener la sumatoria de:'))
suma = 0

while numero > 0:
    suma = suma + numero
    numero = numero - 1

print("La sumatoria es:", suma)


# In[4]:


## 23 ##
# Hay un detalle que se debe modificar en el siguiente código en
# Python, favor de encontrar el problema para poder ejecutar el script
# correctamente.

renglon = 0
max_renglon = 10
max_columna = 16
cadena_renglon_columna = ''

while renglon < max_renglon:
    columna = 0
    while columna < max_columna:
        cadena_renglon_columna = cadena_renglon_columna + '♥' + ' '
        columna = columna + 1
    cadena_renglon_columna = cadena_renglon_columna + '\n'
    renglon = renglon + 1
print(cadena_renglon_columna)


# In[15]:


## 24 ##
# Generar script donde el usuario ingrese dos datos de entrada, nombre y caracter que sera el marco que rodee
# el texto, usando while y la funcion len(), salida de ejemplo:
####################
#Teresa Rivas Gomez#
####################

nombre_completo = input('Ingresa tu nombre completo: ')
caracter_marco = input('Ingresa un solo caracter que quieres que rodee el texto: ')

while len(caracter_marco) != 1:
    caracter_marco = input('Ingresa un solo caracter que quieres que rodee el texto: ')
    
print(caracter_marco * (len(nombre_completo) + 4))
print(caracter_marco + ' ' + nombre_completo + ' ' + caracter_marco)
print(caracter_marco * (len(nombre_completo) + 4))    


# In[20]:


## 25 ##
# Escriba un script para que imprima una figura de rombo donde debe
# leer un número impar de manera que especifique el número de filas
# en el rombo y también debe leer el carácter con el que pintara el
# rombo. La salida es la siguiente:

longitud = int(input('Ingrese un numero impar para que sea la longitud maxima del rombo:'))
caracter = input('Ingrese el caracter que tendra el rombo:')

if longitud % 2 == 0:
    print("Por favor, ingrese un número impar para la longitud.")
else:
    i = 1
    while i <= longitud // 2 + 1:
        print((caracter * (2 * i - 1)).center(longitud, ' '))
        i += 1
    i = longitud // 2
    while i >= 1:
        print((caracter * (2 * i - 1)).center(longitud, ' '))
        i -= 1


# In[ ]:




