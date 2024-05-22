# Creación de la lista de compras
lista_compras = []

# Agregar artículos a la lista
lista_compras.append("Leche")
lista_compras.append("Pan")
lista_compras.append("Manzanas")

# Mostrar la lista original
print("Lista de compras original:")
print(lista_compras)

# Ordenar alfabéticamente la lista de compras
lista_compras.sort()

# Mostrar la lista ordenada
print("\nLista de compras ordenada:")
print(lista_compras)

# Desafío opcional: Eliminar un artículo específico
# Por ejemplo, eliminar "Pan" de la lista
if "Pan" in lista_compras:
    lista_compras.remove("Pan")

# Mostrar la lista actualizada
print("\nLista de compras despues de eliminar 'Pan':")
print(lista_compras)
