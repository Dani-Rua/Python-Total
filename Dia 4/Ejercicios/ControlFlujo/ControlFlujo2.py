edad = 18
tiene_licencia = True

if edad < 18 and not tiene_licencia:
    print('No puedes conducir aún. Debes tener 18 años y contar con una licencia')
elif edad >= 18 and not tiene_licencia:
    print('No puedes conducir. Necesitas contar con una licencia')
else:
    print('Puedes conducir')
