# 1. Configuración del rango
min_rango = 1
max_rango = 20

print(f"--- CONFIGURACIÓN DEL RANGO ({min_rango} a {max_rango}) ---")

# 2. Obligar al Jugador 1 a elegir dentro del rango
# Inicializamos la variable con un valor fuera del rango para que entre al bucle
numero_inicial = 0

while numero_inicial < min_rango or numero_inicial > max_rango:
    numero_inicial = int(input(f"Jugador 1, elige un número entre {min_rango} y {max_rango}: "))
    
    if numero_inicial < min_rango or numero_inicial > max_rango:
        print(f"¡Error! El número debe estar entre {min_rango} y {max_rango}. Intenta de nuevo.")

# 3. Aplicar reglas para que sea PAR
if numero_inicial % 2 != 0:  # Si es impar
    if numero_inicial + 1 <= max_rango:
        numero_secreto = numero_inicial + 1
    else:
        numero_secreto = numero_inicial - 1
else:
    numero_secreto = numero_inicial

# Limpiar pantalla (simulado)
print("\n" * 50)

# 4. Fase de adivinanza (Jugador 2)
print(f"¡Listo! Se ha guardado un número PAR entre {min_rango} y {max_rango}.")
intentos = 3

while intentos > 0:
    print(f"\nIntentos restantes: {intentos}")
    intento = int(input("¿Cuál crees que es el número?: "))
    
    if intento == numero_secreto:
        print(f"¡Increíble! Adivinaste, el número era {numero_secreto}.")
        break
    elif intento < numero_secreto:
        print("Pista: El número secreto es mayor.")
    else:
        print("Pista: El número secreto es menor.")
    
    intentos -= 1

if intentos == 0 and intento != numero_secreto:
    print(f"\nSe acabaron los intentos. El número era {numero_secreto}.")