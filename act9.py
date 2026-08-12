def calcularimc(peso,altura):
    if altura <= 0:
        raise ValueError("Altura debe ser mayor que 0")
    imc = peso / (altura ** 2)
    return imc
def obtenercat(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif imc <= 24.9:
        return "Peso normal"
    elif imc <= 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"

print("Calcular imc")
try:
    pesousuario=float(input("Ingresa tu peso en kg: "))
    alturausuario=float(input("Ingresa tu altura en metros: "))
    imcres=calcularimc(pesousuario,alturausuario)
    catres=obtenercat(imcres)

    print(f"Tu IMC es {imcres:.2f}")
    print(f"Categoria: {catres}")
except ValueError:
    print("Ingresa valores validos")
except ZeroDivisionError:
    print("Altura no puede ser cero")

estudiantes=[
    {"num":1, "peso": 29.5, "imc": 16.43},
    {"num":2, "peso": 36.3, "imc": 19.31},
    {"num":3, "peso": 38.0, "imc": 10.25},
    {"num":4, "peso": 31.0, "imc": 18.63},
    {"num":5, "peso": 36.0, "imc": 17.85},
    {"num":6, "peso": 40.4, "imc": 19.76},
    {"num":7, "peso": 47.0, "imc": 23.64},
    {"num":8, "peso": 43.0, "imc": 21.94},
    {"num":9, "peso": 36.0, "imc": 21.30},
    {"num":10, "peso": 40.1, "imc": 22.67},
    {"num":11, "peso": 27.0, "imc": 16.48}
]

for estudiante in estudiantes:
    if estudiante["imc"] < 18.5:
        print(f"El estudiante {estudiante['num']} tiene bajo peso con un IMC de {estudiante['imc']:.2f}")