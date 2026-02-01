nombre = input("Ingrese su nombre: ")
ventas_mes = int(input("Ingrese sus ventas: "))
comision = round(ventas_mes * 13/100)

print(f"Hola {nombre} su venta de este mes fue de {ventas_mes} pesos por lo tanto su comisión es de ${comision} pesos")