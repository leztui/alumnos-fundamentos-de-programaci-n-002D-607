while True:
    try:
        print("Su codigo solo debe de tener 6 caracteres")
        print("Su codigo ingresado no debe contener espacios")
        codigo = input("Ingrese el codigo de su producto: ").upper()
        if len(codigo) != 6 or " " in codigo:
            raise ValueError("El codigo ingresado no cumple con los requisitos")
        break
    except ValueError:
        print("[ERROR] CODIGO INVALIDO CARACTERES INCORRECTOS")
        continue
print(f"Producto registrado con código: {codigo}")
