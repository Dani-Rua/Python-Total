monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:
    print("No tengo mas dinero")

respuesta = 's'

while respuesta == 's':
    respuesta = input("Quieres seguir? (s/n)")
else:
    print("Gracias")

while respuesta == 's':
    pass #Deja seguir el codigo, no se necesita la lógica todavía.
print("Hola")

nombre = input("Ingresa tu nombre: ")
for letra in nombre:
    if letra == 'r':
        break #Esto permite interrumpir la ejecución dado una condición, si la condición no se cumple el ciclo continua hasta que se cumpla. Las demas interaiones no continuan por eso muestra "fede"
    print(letra)

nombre = input("Ingresa tu nombre: ")
for letra in nombre:
    if letra == 'r':
        continue #Esto permite seguir con la ejecución, no muestrala condicion en este caso 'r', pero continua iterando "fedeico"
    print(letra)

