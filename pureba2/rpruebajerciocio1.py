def calcular_cuenta_electrica():
    VALOR_CUENTA_BASE = 45000
    VALOR_MEDICION_BASE = 6000

    print("--- Sistema de Cálculo de Energía Eléctrica ---")
    
   
    try:
        consumo = float(input("Ingrese el consumo en kWh: "))
        tarifa = input("Ingrese el tipo de tarifa (A, B, C o D): ").upper()
    except ValueError:
        print("Error: Por favor, ingrese un número válido para el consumo.")
        return

    desc_cuenta = 0
    
    if consumo >= 500:
        if tarifa in ['A', 'B']:
            desc_cuenta = 0.20
        elif tarifa in ['C', 'D']:
            desc_cuenta = 0.14
    elif 200 <= consumo < 500:
        if tarifa in ['A', 'B']:
            desc_cuenta = 0.12
        elif tarifa in ['C', 'D']:
            desc_cuenta = 0.08
    else:
        desc_cuenta = 0 
    desc_medicion = 0
    
    if tarifa in ['A', 'B']:
        desc_medicion += 0.10 
        if consumo >= 400:
            desc_medicion += 0.05  

    valor_final_cuenta = VALOR_CUENTA_BASE * (1 - desc_cuenta)
    valor_final_medicion = VALOR_MEDICION_BASE * (1 - desc_medicion)
    total_a_pagar = valor_final_cuenta + valor_final_medicion

    print("\n--- Resumen de Facturación ---")
    print(f"Consumo registrado: {consumo} kWh")
    print(f"Tarifa aplicada: {tarifa}")
    print("-" * 30)
    print(f"Cuenta mensual: ${valor_final_cuenta:,.0f} (Desc: {desc_cuenta*100}%)")
    print(f"Cargo medición: ${valor_final_medicion:,.0f} (Desc: {desc_medicion*100}%)")
    print(f"TOTAL A PAGAR:  ${total_a_pagar:,.0f}")

if __name__ == "__main__":
    calcular_cuenta_electrica()