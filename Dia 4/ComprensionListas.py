palabra = "python"

lista = []

for letra in palabra: # Es muy lago de esta forma, lo vamos a hacer con comprension de listas
    lista.append(letra)
print(lista)

#Comprension de listas
lista = [letra for letra in palabra]
print(lista)

lista = [xx for xx in palabra] #Funcinaría igual porque las xx son variables que asignamos al igual que letra
print(lista)

lista = [xx for xx in 'palabra']
print(lista)

lista = [n for n in range(0,21,2)]
print(lista)

lista = [n / 2 for n in range(0,21,2)] #Puedo alterar un número antes de incluirlo en la lista
print(lista)

lista = [n * 2 for n in range(0,21,2)]
print(lista)

lista = [n for n in range(0,21,2) if n * 2 > 10] # Podemos agregar un if
print(lista)

lista = [n if n * 2 > 10 else 'no' for n in range(0,21,2)] # Podemos agregar un if y tambien un else
print(lista)

pies = [10,20,30,40,50]
metros = [p / 3.281 for p in pies]
print(metros)