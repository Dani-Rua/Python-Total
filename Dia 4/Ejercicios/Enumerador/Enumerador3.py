lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for index,name in enumerate(lista_nombres):
    if name.startswith('M'):
        print(index, name)