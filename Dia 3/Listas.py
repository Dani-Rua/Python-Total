mi_lista = ['a','b','c']
print(type(mi_lista))

otra_lista = ['Hola', 90, 3.5]
print(type(otra_lista))

mi_lista = ['a','b','c']
resultado = len(mi_lista)
print(resultado)

mi_lista = ['a','b','c']
resultado = mi_lista[0]
print(resultado)

mi_lista = ['a','b','c']
resultado = mi_lista[0:1]
print(resultado)

mi_lista = ['a','b','c']
resultado = mi_lista[0:2]
print(resultado)

mi_lista = ['a','b','c']
mi_lista_2 = ['d','e','f']
resultado = mi_lista[0:2]
print(mi_lista + mi_lista_2)

mi_lista = ['a','b','c']
mi_lista_2 = ['d','e','f']
mi_lista_3 = mi_lista + mi_lista_2
print(mi_lista_3)

mi_lista = ['a','b','c']
mi_lista_2 = ['d','e','f']
mi_lista_3 = mi_lista + mi_lista_2
mi_lista_3[0] = "Alfa"
print(mi_lista_3)

mi_lista = ['a','b','c']
mi_lista_2 = ['d','e','f']
mi_lista_3 = mi_lista + mi_lista_2
mi_lista_3.append('g')
print(mi_lista_3)

mi_lista = ['a','b','c']
mi_lista_2 = ['d','e','f']
mi_lista_3 = mi_lista + mi_lista_2
mi_lista_3.pop()
print(mi_lista_3)

mi_lista = ['a','b','c']
mi_lista_2 = ['d','e','f']
mi_lista_3 = mi_lista + mi_lista_2
mi_lista_3.pop(0)
print(mi_lista_3)

mi_lista = ['a','b','c']
mi_lista_2 = ['d','e','f']
mi_lista_3 = mi_lista + mi_lista_2
eliminado = mi_lista_3.pop(0)
print(mi_lista_3)
print(eliminado)

lista = ['g','o','b','m','c']
lista.sort()
print(lista)

lista = ['g','o','b','m','c']
nueva_lista = lista.sort()
print(type(nueva_lista))

lista = ['g','o','b','m','c']
lista.sort()
lista2 = lista
print(lista2)

lista = ['g','o','b','m','c']
lista.sort()
lista.reverse()
print(lista)


