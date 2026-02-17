lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares += numero
    if numero % 2 == 1:
        suma_impares += numero

print(f"La suma de los número pares es {suma_pares} y la de los impares es {suma_impares}")