Membresía = 35.000
Casillero = 4.500
meses = int(input("Ingrese la cantidad de meses contratados: "))
plan = input("Ingrese el tipo de plan (1, 2, 3 o 4): ")
if meses <= 12: 
    if plan == "1" or plan == "2":
        desc_membresia = 0.22
    elif plan == "3" or plan == "4":
        desc_membresia = 0.15  
elif 6 <= meses < 12: 
    if plan == "1" or plan == "2": 
        desc_membresia = 0.12
    elif plan == "3" or plan == "4":
        desc_membresia = 0.07
else:
    desc_membresia = 0
if plan == "1" or plan == "2":
    desc_casillero = 0.15
    if meses >= 9:
        desc_casillero = desc_casillero + 0.05
        
valor_final_membresia = Membresía * (1 - desc_membresia)
valor_final_casillero = Casillero * (1 - desc_casillero)
total_pagar = valor_final_membresia + valor_final_casillero

print("\n" + "="*35)
print(f"DETALLE DEL CONTRATO (PLAN {plan})")
print(f"Meses contratados: {meses}")
print("-" * 35)
print(f"Membresía: ${valor_final_membresia:,.0f} (-{desc_membresia*100}%)")
print(f"Casillero: ${valor_final_casillero:,.0f} (-{desc_casillero*100}%)")
print("-" * 35)
print(f"VALOR TOTAL A PAGAR: ${total_pagar:,.0f}")
print("="*35)
