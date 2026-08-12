while True:
    try:
        num=int(input("Ingrese numero: "))
        break
    except ValueError:
        print("ingrese valor valido")

if num%2==0:
    print("Su numero es par")
else:
    print("Su numero es impar")