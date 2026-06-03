while True:
    try:
        n_equipos = int(input("Ingrese la cantidad de computadores a registrar: "))
        if n_equipos > 0:
            break
        print("Error: La cantidad debe ser mayor a 0.")
    except ValueError:
        print("Error: Ingrese un número entero válido.")

obsoletos = 0
vigentes = 0

for i in range(n_equipos):
    print(f"\n--- Computador {i+1} ---")
    
    while True:
        codigo = input("Ingrese el código de activo: ")
        if len(codigo) >= 6 and " " not in codigo:
            break
        print("Error: El código debe tener al menos 6 caracteres y no contener espacios.")
        
    while True:
        try:
            anio = int(input("Ingrese el año de fabricación (1990-2026): "))
            if 1990 <= anio <= 2026:
                break
            print("Error: El año de fabricación debe estar entre 1990 y 2026.")
        except ValueError:
            print("Error: Ingrese un número entero válido.")
            
    if anio < 2018:
        print("Clasificación: Equipo obsoleto")
        obsoletos += 1
    else:
        print("Clasificación: Equipo vigente")
        vigentes += 1

print("\n--- Resumen de Inventario ---")
print(f"Total registrados: {n_equipos}")
print(f"Equipos obsoletos: {obsoletos}")
print(f"Equipos vigentes: {vigentes}")