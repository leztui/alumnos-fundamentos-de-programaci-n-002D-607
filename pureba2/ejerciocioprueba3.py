mensualidad = 85000
kit = 18000
desc_mensualidad = 0
edad_meses = int(input("Ingrese la cantidad de meses contratados: "))
nivel = input("Ingrese el tipo de kit (1, 2, 3 o 4): ")
if edad_meses <= 18:
    if nivel == "1" or nivel == "2":
        desc_membresia = 0.20
    elif nivel == "3" or nivel == "4":
        desc_membresia = 0.13
elif 19 <= edad_meses <= 36: 
    if nivel == "1" or nivel == "2":
        desc_membresia = 0.12
    elif nivel == "3" or nivel == "4":
        desc_membresia = 0.07
elif edad_meses > 36 :
    desc_membresia = 0
else :
    desc_membresia = 0  
desc_kit = 0
if nivel == "1" or  nivel == "2":
    desc_kit = 0.10
    if edad_meses <= 12:
        desc_kit = desc_kit + 0.05

valor_final_mensualidad = mensualidad * (1 - desc_mensualidad)
valor_final_kit = kit * (1 - desc_kit)
total_final = valor_final_mensualidad + valor_final_kit

print("\n" + "="*30)
print(f"resumen Jardin Infantiñ")
print(f"Edad: {edad_meses} meses | Nivel: {nivel}")
print("-" * 30)
print(f"Mensualidad: ${valor_final_mensualidad:,.0f}")
print(f"Kit Materiales: ${valor_final_kit:,.0f}")
print("-" * 30)
print(f"Total a pagar: ${total_final:,.0f}")
print("="*30)
    
