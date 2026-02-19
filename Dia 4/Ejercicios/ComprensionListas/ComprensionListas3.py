temperatura_fahrenheit = [32, 212, 275]

grados_celsius = [(fahren - 32)*(5/9) for fahren in temperatura_fahrenheit]
print(grados_celsius)