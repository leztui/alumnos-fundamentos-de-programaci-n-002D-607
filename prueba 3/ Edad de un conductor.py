while True:
    try:
        edad = int(input("Ingrese su edad: "))
        if edad <= 0:
            print("Ingrese una edad válida")
            continue
        else:
            print(f" edad registrada : {edad} años")
        break
    except ValueError:
        print("Ingrese un número válido")

