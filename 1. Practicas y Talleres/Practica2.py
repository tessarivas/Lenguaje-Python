#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# TERESA RIVAS GOMEZ
# 372565


# In[3]:


# EJERCICIO 1
# Crear las variables:
x = 2
y = 3
print('x =', x)
print('Value of', x, '+', x, 'is', (x + x))
print('x =')
print((x + y), 'x =', (y + x))


# In[13]:


# EJERCICIO 2
# ¿Qué hay de malo con este código?, Debe leer un entero en la variable calificación:
# Flataba agregar int para determinar que solo son validos enteros.
calificacion = int(input('Ingrese una calificacion entre 1 y 100: '))


# In[18]:


# EJERCICIO 3
# Reemplace *** en el siguiente código con una sentencia que imprimirá un mensaje como ‘¡Felicitaciones! Tu calificación 
# de 91 te otorga una A en este curso‘. Su declaración debe imprimir el valor almacenado en la variable calificación:

if calificacion >= 90:
    print('¡Felicitaciones! Tu calificación de', calificacion, 'te otorga una A en este curso.')


# In[16]:


# EJERCICIO 4
# (Área, diámetro y circunferencia del círculo) Para un círculo de radio 2, muestre el diámetro, la circunferencia y el área.
# Utilice el valor 3,14159 para π. Utilice las siguientes fórmulas (r es el radio): diámetro = 2r, circunferencia = 2πr y área = π r2.
radio = 2
pi = 3.14159

Diametro = 2 * radio
Circunferencia = 2 * pi * radio
Area = pi * (radio**2)

print(f'Radio: {radio: .0f}')
print(f'Pi: {pi: .5f}')
print(f'Diametro: {Diametro: .0f}')
print(f'Circunferencia: {Circunferencia: .5f}')
print(f'Area: {Area: .5f}')


# In[29]:


# EJERCICIO 5
# Utilice sentencias if para determinar si un número entero es par o impar. [Sugerencia: utilice el operador residuo. 
# Un número par es múltiplo de 2. Cualquier múltiplo de 2 deja un residuo de 0 cuando se divide por 2.
numero = int(input('Ingrese un numero entero para evaluar si es par o impar: '))

if numero % 2 == 0:
    print(numero, 'es par.')
if numero % 2 != 0:
    print(numero, 'es impar.')


# In[32]:


# EJERCICIO 6
# Utilice sentencias if para determinar si 1024 es múltiplo de 4 y si 2 es múltiplo de 10. (Sugerencia: utilice el
# operador de residuo).

x = int(input('Ingrese el primer entero: '))
y = int(input('Ingrese el segundo entero: '))

if x % y == 0:
    print(x,"es multiplo de",y)
if x % y != 0:
    print(x,"no es multiplo de",y)


# In[41]:


# EJERCICIO 7
# Escriba un guión(script) que calcule los cuadrados y cubos de los números del 0 al 5. Imprima los valores
# resultantes en formato de tabla, como se muestra a continuación. Utilice la secuencia de escape de tabulación 
# para lograr el resultado de tres columnas.

print('numero', '\t', 'cuadrado', ' ', 'cubo')
print('0', '\t', 0**2, '\t', ' ', 0**3)
print('1', '\t', 1**2, '\t', ' ', 1**3)
print('2', '\t', 2**2, '\t', ' ', 2**3)
print('3', '\t', 3**2, '\t', ' ', 3**3)
print('4', '\t', 4**2, '\t', ' ', 4**3)
print('5', '\t', 5**2, '\t', ' ', 5**3)


# In[44]:


# EJERCICIO 8
# Muestra cómo "alinear a la derecha" los números. Podrías intentarlo aquí como un reto extra. La salida sería:
# Pista: Podrías usar los “Literales de cadena formateados”(también llamados f-strings para abreviar).

print(f'{"numero":>7} {"cuadrado":>9} {"cubo":>6}')
print(f'{0:>7} {0**2:>9} {0**3:>6}')
print(f'{1:>7} {1**2:>9} {1**3:>6}')
print(f'{2:>7} {2**2:>9} {2**3:>6}')
print(f'{3:>7} {3**2:>9} {3**3:>6}')
print(f'{4:>7} {4**2:>9} {4**3:>6}')
print(f'{5:>7} {5**2:>9} {5**3:>6}')

