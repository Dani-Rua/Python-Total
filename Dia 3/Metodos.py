texto = "Este es el texto de Daniel"
resultado = texto
print(resultado)

texto = "Este es el texto de Daniel"
resultado = texto.upper()
print(resultado)

texto = "Este es el texto de Daniel"
resultado = texto[2].upper()
print(resultado)

texto = "Este es el texto de Daniel"
resultado = texto.lower()
print(resultado)

texto = "Este es el texto de Daniel"
resultado = texto.split()
print(resultado)

texto = "Este es el texto de Daniel"
resultado = texto.split("t")
print(resultado)

# Join
a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a, b, c, d])
print(e)

texto = "Este es el texto de Daniel"
resultado = texto.find("s")
print(resultado)

texto = "Este es el texto de Daniel"
resultado = texto.find("g")
print(resultado)

texto = "Este es el texto de Daniel"
resultado = texto.replace("Daniel", "todos")
print(resultado)

texto = "Este es el texto de Daniel"
resultado = texto.replace("e", "x")
print(resultado)