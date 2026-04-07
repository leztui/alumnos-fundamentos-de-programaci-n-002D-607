almuerzo = 0 
impresiones = 0
gastos_semanales = 0
print(" Bienvenido a este programa que calcula tus gastos semanales ")
print()
print(" primera pregunta ")
print()
print("  cuánto dinero gasta diariamente en almuerzo? ")

while True: 
    try: 
        almuerzo = float(input(" Digite el valor: "))
        break
    except ValueError:
        print(" Por favor, ingrese un número válido para el almuerzo.")

print()
print(" segunda pregunta ") 
print()
print(" cuánto dinero gastas en impresiones?")
while True: 
    try:
        impresiones = float(input(" Digite el valor: "))
        break            
    except ValueError:
        print(" Por favor, ingrese un número válido para las impresiones.")

print()
print(" segunda pregunta ") 
print()
print(" cuánto dinero gastas en impresiones?")
while True: 
    try:
        impresiones = float(input(" Digite el valor: "))
        break
    except ValueError:
        print(" Por favor, ingrese un número válido para las impresiones.")
        continue
    print()
    gastos_semanales += almuerzo * 5 + impresiones * 5
print(f" tus gastos semanales total son: {gastos_semanales} ")
if gastos_semanales > 20000:
    print(" Has superado el límite de gastos semanales.")
else:
    print(" Tus gastos semanales están dentro del límite.")