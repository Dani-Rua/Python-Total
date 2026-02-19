capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

conbinado = list(zip(capitales, paises))

for capitales, paises in conbinado:
    print(f'La capital de {paises} es {capitales}')