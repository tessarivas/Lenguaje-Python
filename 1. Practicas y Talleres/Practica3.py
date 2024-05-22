#!/usr/bin/env python
# coding: utf-8

# In[17]:


# EJERCICIO 9
# Puede indicar el valor de un carácter en un programa encerrando ese carácter entre comillas, como en 'A'. 
# Para determinar el valor entero de un carácter, llame a la función integrada ord:
# Muestra los equivalentes enteros de B C D b c d 0 1 2 $ * + y el carácter de espacio.

ord('A'), ord('B'), ord('C'), ord('D'), ord('b'), ord('c'), ord('d'), ord('0'), ord('1'), ord('2'), ord('$'), ord('*'), ord('+'), ord(' ')


# In[52]:


# EJERCICIO 10
# Escriba un script(guión) que ingrese tres números enteros desde el usuario. Muestre la suma, el promedio, 
# el producto, el menor y el mayor de los 3 números. Tenga en cuenta que cada uno de estos es una reducción 
# en la programación de estilo funcional.

n1 = int(input('Ingrese el primer entero:'))
n2 = int(input('Ingrese el segundo entero:'))
n3 = int(input('Ingrese el tercer entero:'))

suma = n1 + n2 + n3

promedio = (n1 + n2 + n3) / 3

producto = n1 * n2 * n3

mayor = n1
if n2 > mayor:
    mayor = n2
if n3 > mayor:
    mayor = n3
    
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print(f'La suma de los numeros {n1:.1f}, {n2:.1f} y {n3:.1f} es: {suma:.1f}')
print(f'El promedio de los numeros {n1:.1f}, {n2:.1f} y {n3:.1f} es: {promedio:.1f}')
print(f'El producto  de los numeros {n1:.1f}, {n2:.1f} y {n3:.1f} es: {producto:.1f}')
print(f'El mayor de los numeros {n1:.1f}, {n2:.1f} y {n3:.1f} es: {mayor:.1f}')
print(f'El menor de los numeros {n1:.1f}, {n2:.1f} y {n3:.1f} es: {menor:.1f}')


# In[32]:


# EJERCICIO 11
# Escriba un script que ingrese un número entero de cinco dígitos desde el usuario. Separa el número en sus
# dígitos individuales.Imprímelos separados por tres espacios cada uno. Por ejemplo, si el usuario escribe 
# el número 42339, el script debería imprimirse de la siguiente forma:

numero = int(input('Ingrese un numero entero de 5 dígitos:'))

dig1 = numero // 10000
dig2 = (numero // 1000) % 10
dig3 = (numero // 100) % 10
dig4 = (numero // 10) % 10
dig5 = numero % 10

print(f'{dig1}   {dig2}   {dig3}   {dig4}   {dig5}')


# In[40]:


# EJERCICIO 12
# Algunos asesores de inversión afirman que es razonable esperar una rentabilidad del 7% a largo plazo en el 
# mercado de valores. Suponiendo que empiezas con $100,000.00 y dejas tu dinero invertido, calcula y visualiza 
# cuánto dinero tendrás al cabo de 10, 20 y 30 años. Utiliza la siguiente fórmula para determinar estas cantidades:

# Cantidad Original Invertida
p = 100000

# Taza de Rendimiento Anual
r = 0.07

# Años
n = int(input('Ingrese la cantidad de años (10, 20 o 30):'))

# Formula
a = p * (1 + r)**n

# Monto depositado al final
print(f'El monto depositado al final del enésimo año es: {a:.2f}')


# In[41]:


# EJERCICIO 13

numero_grande = 2 ** 14284
print(numero_grande)

import sys
numero_grande = 2 ** 14285
sys.set_int_max_str_digits(100000)
print(numero_grande)


# In[46]:


# EJERCICIO 14
#El usuario ingresa un número x tal que regresara el último dígito de ese número(utilizar la función print()). 
# Pista: utilizar el operador de residuo(%).

numero = int(input('Ingrese un numero para regresar el último dígito:'))

ultimo_digito = numero % 10

print(f'El último dígito del número {numero} es {ultimo_digito}')


# In[51]:


# EJERCICIO 15
# Se le solicita al usuario ingresar 3 valores(números enteros o de punto flotante) y como resultado muestra 
# el número menor de esos tres valores.

n1 = input('Ingrese el primer numero:')
n2 = input('Ingrese el segundo numero:')
n3 = input('Ingrese el tercer numero:')

menor = n1

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print(f'El número menor es: {menor}')


# In[55]:


# EJERCICIO 16
# Se le solicita al usuario ingresar 3 valores(números enteros o de punto flotante) y como resultado de salida 
# muestra si estos tres valores ingresados son iguales o no.

n1 = input('Ingrese el primer numero:')
n2 = input('Ingrese el segundo numero:')
n3 = input('Ingrese el tercer numero:')

if n1 == n2 == n3:
    print(f'Los valores {n1}, {n2} y {n3} son iguales')
if n1 != n2 or n2 != n3 or n1 != n3:
    print(f'Los valores {n1}, {n2} y {n3} no son iguales')


# In[56]:


# EJERCICIO 17
# (if anidados)Escriba un script que ingrese tres números diferentes de punto flotante desde el usuario. Muestre 
# los números en orden creciente. Recuerde que el conjunto de declaraciones if puede contener más de una declaración. 
# Demuestre que su script funciona ejecutándolo en los seis ordenamientos posibles de los números. ¿Su script funciona
# con números duplicados? [Esto es un desafío. En clases posteriores lo harás de manera más conveniente y con muchos más números.]

n1 = input('Ingrese el primer numero:')
n2 = input('Ingrese el segundo numero:')
n3 = input('Ingrese el tercer numero:')

if n1 <= n2 <= n3:
    print("El orden de los numeros en orden ascendente son:", n1, n2, n3)
if n1 <= n3 <= n2:
    print("El orden de los numeros en orden ascendente son:", n1, n3, n2)
if n2 <= n1 <= n3:
    print("El orden de los numeros en orden ascendente son:", n2, n1, n3)
if n2 <= n3 <= n1:
    print("El orden de los numeros en orden ascendente son:", n2, n3, n1)
if n3 <= n1 <= n2:
    print("El orden de los numeros en orden ascendente son:", n3, n1, n2)
if n3 <= n2 <= n1:
    print("El orden de los numeros en orden ascendente son:", n3, n2, n1)

