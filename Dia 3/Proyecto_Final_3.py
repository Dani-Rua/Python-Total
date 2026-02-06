
texto = input("Ingrese un texto: ").lower()
letras = list(input("Ingrese 3 letras: ").lower())

print("\n")
print("CANTIDAD DE LETRAS")

cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces")

print("\n")
print("CANTIDAD DE PALABRAS")
palabra = texto.split()
print(f"Hemos encontrado {len(palabra)} palabras en tu texto")

print("\n")
print("LETRA DE INICIO Y LETRA FIN")
primer_letra = texto[0]
ultima_letra = texto[-1]
print(f"La primer letra es '{primer_letra}' y la última letra es '{ultima_letra}'")

print("\n")
print("TEXTO INVERTIDO")
palabra.reverse()
texto_invertido = ' '.join(palabra)
print(f"Si ordenamos tu texto al revés va a decir: '{texto_invertido}'")

print("\n")
print("BUSCAR LA PALABRA PYTHON")
buscar_python = 'python' in texto
print(buscar_python)
dic = {True: 'sí', False: 'no'}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")
