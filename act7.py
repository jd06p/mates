def celsiusafah(celsius):
    fah=(9/5)*celsius+32
    return round(fah,2)

celsius=float(input("Ingrese los grados Celsius: "))

resultado=celsiusafah(celsius)

print(f"la temperatura en fahrenheit es {resultado}")