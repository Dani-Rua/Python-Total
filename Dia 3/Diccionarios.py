diccionario = {'c1':'valor1', 'c2':'valor2'}
diccionario1 = {'c1':'valor1', 'c3':'valor1'}
print(type(diccionario))
print(diccionario)
print(diccionario1)

resultado = diccionario['c2']
print(resultado)


cliente = {'nombre': 'Daniel', 'apellido': 'Rúa', 'peso': 94, 'talla': 1.80}
consulta = cliente['apellido']
print(consulta)

dic = {'c1': 55, 'c2':[10,20,30], 'c3':{'s1': 100, 's2': 200}}
print(dic['c3']['s2'])
print(dic['c2'][1])

dic1 = {'c1': ['a', 'b', 'c'], 'c2': ['d', 'e', 'f']}
print(dic1['c2'][1].upper())
print(dic1['c1'][0].upper())

dic2 = {1: 'a', 2: 'b'}
print(dic2)

dic2[3] = 'c'
print(dic2)

dic2[2] = 'B'
print(dic2)

print(dic2.keys())
print(dic2.values())
print(dic2.items())
