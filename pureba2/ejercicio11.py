intentos_fallidos = 0 
clave = "Admin123"
clave_correcta = "secreto"

if  clave.lower() == clave_correcta:
   print("entraste")
else: 
   intentos_fallidos =+1 
print(f"Intentos fallidos: {intentos_fallidos}")
