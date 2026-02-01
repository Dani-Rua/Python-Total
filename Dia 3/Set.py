mi_set = set([1,2,3,4,5])
print(mi_set)
print(type(mi_set))

#mi_set[0] = 5
#print(mi_set[0])

otro_set = {1, 2, 3, 4, 5}
print(type(otro_set))
print(otro_set)

mi_set1 = set([1,2,3,4,5,5,2,2,2,2,2,1,1,1,1,3,3,3,3,])
print("Set quita las repeticiones de números: ", mi_set1)

#mi_set2 = set([1,2,3,4,5,5,2,2,2,2,[2,1],1,1,1,3,3,3,3])
#print("Los set no admiten elementos de tipo lista: ", mi_set2)

#mi_set3 = set([1,2,3,4,5,5,2,2,2,2,{2,1},1,1,1,3,3,3,3])
#print("Los set no admiten elementos tipo diccionario: ", mi_set3)

mi_set4 = set([1,2,3,4,5,5,2,2,2,2,(2,1,3),6,1,1,3,3,3,3])
print("Los set admiten elementos de tipo tuples: ", mi_set4)

mi_set5 = set([1,2,3,4,5])
print(len(mi_set5))
print(2 in mi_set5)

s1 = set([1,2,3])
s1.add(4)
s1.add(2)
s1.remove(3)
##s1.remove(6) da error porqueno esta el 6
#s1.discard(6) no da error, el programa sigue así no tenga el 6
#s1.pop() elimina uno de sus elementos aleatorio
#s1.clear() vacia nuestro set
print(s1)
s2 = set([3,4,5])
s3 = s1.union(s2)
print(s3)

