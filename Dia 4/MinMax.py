menor = min(58,96,72,64,35)
mayor = max(58,96,72,64,35)
print(menor)
print(mayor)

lista = [58,96,72,64,35]
print(f'El menor es {menor} y el mayor es {mayor}')


nombres = ['Juan', 'Pablo', 'Alicia', 'Carlos']
print(min(nombres))

nombre = 'Carlos' # Busca primero en las letras mayúsculas por eso aparece la C
print(min(nombre))

nombre = 'carlos' # Sino hay mayúsculas busca la primer letra del alfabeto en este caso a
print(min(nombre))

nombre = 'carlOs' # Busca primero en las letras mayúsculas por eso aparece la O
print(min(nombre))

nombre = 'carlOs'
print(min(nombre.lower()))

dic = {'C1':45, 'C2':11}
print(min(dic)) #Busca la clave que es inferior alfabeticamente

dic = {'C1':45, 'C2':11}
print(min(dic.values()))