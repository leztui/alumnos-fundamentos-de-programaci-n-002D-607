criticas = 0 
normales = 0 
bajas = 0 
for i in range(5):
    temp = float (input(f"ingrese la temperatura del sensor {i+1}:"))
    if temp > 80:
        print("Alerta : temperatura critica")
        criticas += 1
    elif temp >=50 and temp <= 80:
        normales +=1 
        print(" normales operativo")
    elif temp < 50:
        print("Temperatura baja")
        bajas += 1
print("\n")
print(f"Temperaturas criticas: {criticas}")
print(f"Temperaturas medias: {normales}")
print(f"Temperaturas bajas: {bajas}")

