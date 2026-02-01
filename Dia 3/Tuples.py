mi_tuples = (1,2,(10,22),4)
print(mi_tuples)
print(type(mi_tuples))
print((mi_tuples)[0])
print((mi_tuples)[-2])
print((mi_tuples[2][0]))
mi_tuple = list(mi_tuples)
print(type(mi_tuple))
mi_tuple = tuple(mi_tuple)
print(type(mi_tuple))

mi_tuples1 = (1, 2.3, 'Daniel',)
#mi_tuples1[0] = 5 No se le puede asignar valor porque es un tuple
print(mi_tuples1)

t = (1,2,3,1)

print(len(t))
print(t.count(1))
print(t.index(2))

x,y,z = t
print(x,y,z)