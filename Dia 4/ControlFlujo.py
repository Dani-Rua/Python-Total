if 10 > 9:
    print("Es correcto")

if True:
    print("Es correcto")

x = True
if x:
    print("Es correcto")

if 5 == 2:
    print("Es correcto") #Python identifica que no se cumple y ni lee el print
else:
    print("No es correcto")

mascota = 'perro'
if mascota == 'gato':
    print('Tienes un gato')
elif mascota == 'perro':
    print('Tienes un perro')
elif mascota == 'pez':
    print('Tienes un pez')
else:
    print('No se que animal tienes')

mascota = 'pez'
if mascota == 'gato':
    print('Tienes un gato')
elif mascota == 'perro':
    print('Tienes un perro')
elif mascota == 'pez':
    print('Tienes un pez')
else:
    print('No se que animal tienes')

mascota = 'conejo'
if mascota == 'gato':
    print('Tienes un gato')
elif mascota == 'perro':
    print('Tienes un perro')
elif mascota == 'pez':
    print('Tienes un pez')
else:
    print('No se que animal tienes')

edad = 17
calificacion_escolar = 9
if edad < 18:
    print('Eres menor de edad')
    if calificacion_escolar >= 7:
        print('Aprobado')
    else:
        print('No aprobado')
else:
    print('Eres mayor de edad')