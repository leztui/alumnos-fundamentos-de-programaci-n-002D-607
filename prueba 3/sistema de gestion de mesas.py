def sistema_restaurante():
    CAPACIDAD_TOTAL = 20
    mesas_disponibles = CAPACIDAD_TOTAL

    while True:
        print("\n=== SISTEMA DE MESAS - RESTAURANTE EL FARO ===")
        print("1. Ver mesas disponibles")
        print("2. Asignar mesa(s)")
        print("3. Liberar mesa(s)")
        print("4. Mesas ocupadas actualmente")
        print("5. Salir")
        
        try:
            opcion = int(input("Seleccione una opción (1-5): "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if opcion == 1:
            print(f"\n[INFO] Mesas disponibles: {mesas_disponibles}")

        elif opcion == 2:
            if mesas_disponibles == 0:
                print("\n[ERROR] No hay mesas disponibles en este momento. Restaurante lleno.")
                continue
                
            try:
                cantidad = int(input(f"¿Cuántas mesas desea asignar? (Disponibles: {mesas_disponibles}): "))
                if cantidad <= 0:
                    print("[ERROR] La cantidad debe ser mayor a 0.")
                    continue
            except ValueError:
                print("[ERROR] Ingrese un número entero válido.")
                continue

            if cantidad > mesas_disponibles:
                print(f"[ERROR] No puedes asignar más mesas de las disponibles ({mesas_disponibles}).")
            else:
                mesas_disponibles -= cantidad
                print(f"[ÉXITO] Se han asignado {cantidad} mesas correctamente.")

        elif opcion == 3:
            mesas_ocupadas = CAPACIDAD_TOTAL - mesas_disponibles
            if mesas_ocupadas == 0:
                print("\n[ERROR] No hay mesas ocupadas para liberar.")
                continue

            try:
                cantidad = int(input(f"¿Cuántas mesas desea liberar? (Ocupadas: {mesas_ocupadas}): "))
                if cantidad <= 0:
                    print("[ERROR] La cantidad debe ser mayor a 0.")
                    continue
            except ValueError:
                print("[ERROR] Ingrese un número entero válido.")
                continue

            if cantidad > mesas_ocupadas:
                print(f"[ERROR] No puedes liberar más mesas de las que están ocupadas ({mesas_ocupadas}).")
            else:
                mesas_disponibles += cantidad
                print(f"[ÉXITO] Se han liberado {cantidad} mesas correctamente.")

        elif opcion == 4:
            mesas_ocupadas = CAPACIDAD_TOTAL - mesas_disponibles
            print(f"\n[INFO] Mesas ocupadas actualmente: {mesas_ocupadas}")

        elif opcion == 5:
            print("\nServicio finalizado. Buenas noches.")
            break
            
        else:
            print("[ERROR] Opción no válida. Intente de nuevo (1-5).")

if __name__ == "__main__":
    sistema_restaurante()