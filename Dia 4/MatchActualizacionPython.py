from multiprocessing.util import close_all_fds_except

''''serie = 'N-02'''''

'''if serie == 'N-01':
    print("Samsung")
elif serie == 'N-02':
    print("Nokia")
elif serie == 'N-03':
    print("Motorola")
else:
    print("No existe este producto")'''


'''match serie:
    case 'N-01':
        print("Samsung")
    case 'N-02':
        print("Nokia")
    case 'N-03':
        print("Motorola")
    case _:
        print("No existe este producto")'''


cliente = {'nombre': 'Daniel',
           'edad': 20,
           'ocupacion': 'ingeniero'}

pelicula = {
    'titulo': 'Matrix',
    'ficha_tecnica': {'protagonista': 'Keanue reeves',
                      'director': 'Lana y Lili'}
    }
elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad': edad,
              'ocupacion': ocupacion}:
            print("Es un cliente")
            print(nombre, edad, ocupacion)
        case {'titulo': titulo,
              'ficha_tecnica': {'protagonista': protagonista,
                                'director': director}
              }:
            print("Es un pelicula")
            print(titulo, director, protagonista)
        case _:
            print("No se que es esto")