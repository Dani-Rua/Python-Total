nombres = ['Ana', 'Aleja', 'Eduardo']
edades = [65, 32, 98]
ciudades = ['Lima', 'Madrid', 'Mexico']
combinados = list(zip(nombres,edades, ciudades))
print(combinados)

for nombre,edades,ciudades in combinados:
    print(f'{nombre} tiene {edades} y vive en {ciudades}')

nombres = ['Ana', 'Aleja', 'Eduardo']
edades = [65, 32, 98, 55] # No muestra el 55 porque lo que hace el zip es mostrar el largo de la listamas corta

combinados = list(zip(nombres,edades))
print(combinados)