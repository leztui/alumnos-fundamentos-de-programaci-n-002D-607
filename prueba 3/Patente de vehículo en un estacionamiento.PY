while True:
    try:
        print("Su codigo solo debe de tener 6 caracteres")
        print("Su codigo ingresado no debe contener espacios")
        patente = input("Ingrese su patente: ").upper()
        if len(patente) != 6 and " " in patente:
            raise ValueError("Patente inválida. Ingresa exactamente 6 caracteres sin espacios")
        break
    except ValueError:
        print("[ERROR] PATENTE INVALIDO CARACTERES INCORRECTOS")
        continue
print(f"Patente registrado : {patente}")
