lista = ['a','b','c','d']

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"letra {numero_letra}: {letra}")

for letra in lista:
    print("Hola", letra)

lista = ['pablo', 'laura', 'fede', 'luis', 'julia']

for nombre in lista:
    if nombre.startswith('l'): #startswith comienza con un determinado caracter
        print(nombre)
    else:
        print("nombre que no comienza con L")

numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero

    print(mi_valor) #Print dentro del loop muestra todos las iteraciones
print(mi_valor) #Print a nivel del loop muestra solo el final de la iteracion

palabra = 'python'
for letra in palabra:
    print(letra)

for letra in 'python':
    print(letra)

for letra in [1,2,3]:
    print(letra)

for letra in (1,2,3):
    print(letra)

for objetos in [[1,2], [3,4], [5,6]]:
    print(objetos)

for a,b in [[1,2], [3,4], [5,6]]:
    print(a)
    print(b)

for a,b in [[1,2], [3,4], [5,6]]:
    print(a)

dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}
for item in dic:
    print(item)

dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}
for item in dic.items():
    print(item)

dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}
for item in dic.values():
    print(item)

dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}
for a,b in dic.items():
    print(a,b)