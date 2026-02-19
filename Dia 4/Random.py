from random import *

aleatorio = randint(1,50) # Genera números aleatorios
print(aleatorio)

aleatorio = uniform(1,5)
print(aleatorio)

aleatorio = round(uniform(1,5))
print(aleatorio)

aleatorio = round(uniform(1,5),1)
print(aleatorio)

aleatorio = random()
print(aleatorio)

colores = ['azul', 'rojo', 'verde', 'amarillo']
aleatorio = choice(colores) #Elije un string aleatorio
print(aleatorio)

numeros = list(range(5,50,5))
shuffle(numeros) # Hace una mezcla aleatorio de los números, no se puede usar con string por que los string son inmutables
print(numeros)