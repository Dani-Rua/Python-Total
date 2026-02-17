hablar_ingles = True
sabe_python = True

if not hablar_ingles and not sabe_python:
    print('Para postularte, necesitas saber programar en Python y tener conocimientos de inglés')
elif sabe_python and not hablar_ingles:
    print('Para postularte, necesitas tener conocimientos de inglés')
elif hablar_ingles and not sabe_python:
    print('Para postularte, necesitas saber programar en Python')
else:
    print('Cumples con los requisitos para postularte')