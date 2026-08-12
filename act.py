contraseña=input("Ingrese contraseña a añadir: ").capitalize()

while True:
    adivina=input("Ingrese contraseña: ").capitalize()
    if adivina==contraseña:
        print("Acceso autorizado")
        break
    else:
        print("Contraseña incorrecta")