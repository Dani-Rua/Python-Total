from random import random, randint

nombre = input("Ingrese su nombre: ")
print(f'“Bueno, {nombre}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número')

numero_aleatorio = randint(1,5)
print(numero_aleatorio)

for num in range(1,9):
    numero = int(input('Ingrese un número: '))
    if numero_aleatorio == numero:
        print(f'Felicitaciones {nombre} has adivinado en {num} intentos')
        break
    if numero < 1:
        print('No puedes elegir un número menor que 1')
        break
    if numero > 100:
        print('No puedes elegir un número mayor que 100')
        break
    if numero > numero_aleatorio:
        print('El número ingresado es mayor que el aleatorio')
    else:
        print('El número ingresado es menor que el aleatorio')
else:
    print(f"Haz superado el número de intentos pemitidos el número secreto es {numero_aleatorio}")

'''EJEMPLO CON BUENAS PRACTICAS'''

intentos = 0
estimados = 0
numero_secreto = randint(1,100)
nombre = input("Ingrese su nombre: ")

print(f'Bueno {nombre}, he pensado un número del 1 al 100. Tienes 8 intentos para adivinar.')

while intentos < 8:
    estimados = int(input('Cual es el número?: '))
    intentos += 1

    if estimados not in range(1,101):
        print('Tú número no se encuentra entre el rango de 1 a 100')
    elif estimados < numero_secreto:
        print("Mi número es mas alto")
    elif estimados > numero_secreto:
        print("Mi número es mas bajo")
    else:
        print(f'Felicidades {nombre} has adivinado en {intentos} intentos')
        break

if estimados != numero_secreto:
    print(f'Lo siento se han agotado los intentos. El número secreto es {numero_secreto}')