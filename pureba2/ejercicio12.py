sueldo = 550000
limite = 500000
deuda = 1 
cantidad_deudas= 0
if limite and cantidad_deudas> sueldo and deuda:
   print("aprobado")
else : 
    print("Rechazado")          


## mi otro codigo 
sueldo = 550000
cantidad_deudas = 1  # El ejercicio dice que tiene 1 deuda activa

# Verificamos ambas condiciones en la misma línea
if sueldo > 500000 and cantidad_deudas == 0:
    print("Aprobado")
else:
    print("Rechazado")