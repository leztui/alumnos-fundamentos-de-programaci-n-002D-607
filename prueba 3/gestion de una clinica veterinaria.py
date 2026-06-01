def registrar_animales():
    while True:
        try:
            n_animales = int(input("¿Cuántos animales se registrarán?: "))
            if n_animales > 0:
                break
            print("[ERROR] Debe ser un número entero positivo.")
        except ValueError:
            print("[ERROR] Ingrese un número entero válido.")

    grandes = 0
    pequenos = 0

    for i in range(n_animales):
        print(f"\n--- Registro del animal {i+1} ---")
        
        while True:
            id_animal = input("ID del animal: ")
            if len(id_animal) >= 6 and " " not in id_animal:
                break
            print("[ERROR] El ID debe tener mínimo 6 caracteres y no contener espacios.")
            
        while True:
            try:
                peso = int(input("Peso en kg: "))
                if peso > 0:
                    break
                print("[ERROR] El peso debe ser un entero positivo.")
            except ValueError:
                print("[ERROR] Ingrese un número válido para el peso.")
                
        if peso > 25:
            grandes += 1
        else:
            pequenos += 1

    print(f"\nLa clínica ha registrado {grandes} pacientes grandes y {pequenos} pacientes pequeños. ¡Bienvenidos!")

def agenda_veterinaria():
    HORAS_TOTALES = 30
    horas_disponibles = HORAS_TOTALES

    while True:
        print("\n=== AGENDA CLÍNICA VETERINARIA PATITAS ===")
        print("1. Ver horas disponibles")
        print("2. Reservar hora(s)")
        print("3. Cancelar hora(s)")
        print("4. Ver historial de reservas")
        print("5. Salir")
        
        try:
            opcion = int(input("Seleccione una opción (1-5): "))
        except ValueError:
            print("[ERROR] Por favor, ingrese un número válido.")
            continue

        if opcion == 1:
            print(f"\n[INFO] Horas disponibles: {horas_disponibles}")

        elif opcion == 2:
            if horas_disponibles == 0:
                print("\n[ERROR] No hay horas disponibles en este momento.")
                continue
                
            try:
                cantidad = int(input(f"¿Cuántas horas desea reservar? (Disponibles: {horas_disponibles}): "))
                if cantidad <= 0:
                    print("[ERROR] La cantidad debe ser mayor a 0.")
                    continue
            except ValueError:
                print("[ERROR] Ingrese un número entero válido.")
                continue

            if cantidad > horas_disponibles:
                print(f"[ERROR] No puedes reservar más horas de las disponibles ({horas_disponibles}).")
            else:
                horas_disponibles -= cantidad
                print(f"[ÉXITO] Se han reservado {cantidad} hora(s) correctamente.")

        elif opcion == 3:
            horas_reservadas = HORAS_TOTALES - horas_disponibles
            if horas_reservadas == 0:
                print("\n[ERROR] No hay horas reservadas para cancelar.")
                continue

            try:
                cantidad = int(input(f"¿Cuántas horas desea cancelar? (Reservadas: {horas_reservadas}): "))
                if cantidad <= 0:
                    print("[ERROR] La cantidad debe ser mayor a 0.")
                    continue
            except ValueError:
                print("[ERROR] Ingrese un número entero válido.")
                continue

            if cantidad > horas_reservadas:
                print(f"[ERROR] No puedes cancelar más horas de las que están reservadas ({horas_reservadas}).")
            else:
                horas_disponibles += cantidad
                print(f"[ÉXITO] Se han cancelado {cantidad} hora(s) correctamente.")

        elif opcion == 4:
            horas_reservadas = HORAS_TOTALES - horas_disponibles
            print(f"\n[INFO] Historial: Hay {horas_reservadas} hora(s) ocupada(s) actualmente.")

        elif opcion == 5:
            print("\nSistema cerrado. ¡Hasta pronto!")
            break
            
        else:
            print("[ERROR] Opción no válida. Intente de nuevo (1-5).")

if __name__ == "__main__":
    registrar_animales()
    agenda_veterinaria()