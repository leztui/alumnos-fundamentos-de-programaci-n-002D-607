while True:
    try:
        N = int(input("Ingrese la cantidad de estudiantes: "))
        if N > 0:
            break
        print("Error: La cantidad debe ser mayor a 0.")
    except ValueError:
        print("Error: Ingrese un número entero válido.")

aprobados = 0
reprobados = 0

for i in range(N):
    while True:
        try:
            nota = float(input(f"Ingrese la nota del estudiante {i+1} (1.0 - 7.0): "))
            if 1.0 <= nota <= 7.0:
                break
            print("Error: La nota debe estar entre 1.0 y 7.0.")
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")
    
    if nota >= 4.0:
        aprobados += 1
    else:
        reprobados += 1

print("\n--- Resumen ---")
print(f"Total de estudiantes: {N}")
print(f"Aprobados (>= 4.0): {aprobados}")
print(f"Reprobados (< 4.0): {reprobados}")