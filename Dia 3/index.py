mi_texto = "Esta es una prueba"
resultado = mi_texto[3]
print(resultado)

mi_texto = "Esta es una prueba"
resultado = mi_texto[-4]
print(resultado)

mi_texto = "Esta es una prueba"
resultado = mi_texto.index("p")
print(resultado)

mi_texto = "Esta es una prueba"
#Aparece 12 porque empieza en la letra p
resultado = mi_texto.index("prueba")
print(resultado)

#mi_texto = "Esta es una prueba"
#Muestra el indice 3 porque lee de izquierda a derecha y toma la primer a así hayan varias letras. (si yo le digo desde que indice hacia adelante toma me muestra que la a esta en posición 10. Con inicio 5 y final 10 nos da un error porque no toma la a así sea el decimo indice, porque no es inclusivo debe ser 11 para poder que tome la a
#resultado = mi_texto.index("a",5,10)
#print(resultado)

mi_texto = "Esta es una prueba"
#Este metodo busca de derecha a izquierda
resultado = mi_texto.rindex("a")
print(resultado)

mi_texto = "Esta es una prueba"
#Este da un error porque la X no existe en el texto
resultado = mi_texto.index("x")
print(resultado)

mi_texto = "Esta es una prueba"
#Este da un error porque la palabra no existe en el texto
resultado = mi_texto.index("prueva")
print(resultado)

mi_texto = "Esta es una prueba"
#Este da un error porque es sensible a las mayúsculas no existe en el texto
resultado = mi_texto.index("P")
print(resultado)



