while True:
    try:
        usuario = input("Ingrese su nombre de usuario para nuestra app bancaria: ")
        if len(usuario) < 6 or " " in usuario:
            raise ValueError("El usuario no cumple con los requisitos mínimos.")
        break
    except ValueError:
        print("Nombre inválido. Debe tener al menos 6 caracteres y no contener espacios.")
    continue
print(f"Usuario creado: {usuario}")