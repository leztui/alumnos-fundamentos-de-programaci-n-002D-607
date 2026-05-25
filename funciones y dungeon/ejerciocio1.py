import random
import sys
import time
from pyfiglet import figlet_format
from tqdm import tqdm

hp_inicial = 20
ataque_inicial = 5
Salas_totales = 3

ROJO = "\033[1;31m"
BLANCO = "\033[1;37m"
RESET = "\033[0m"



def crear_jugador(nombre_ingresado):
    print(f"Creando jugador con nombre {nombre_ingresado}...")
    jugador = {
        "nombre": nombre_ingresado,
        "hp": hp_inicial,
        "hp_max": hp_inicial,
        "atk": ataque_inicial,
        "oro": 0,
        "inventario": ["Pocion"],
    }
    print(f"Jugador creado con éxito.\n")
    return jugador


def mostrar_estado_jugador(jugador):
    print("\n" + "=" * 40)
    print(f"Héroe   : {jugador['nombre']}")
    print(f"Vida    : {jugador['hp']}/{jugador['hp_max']}")
    print(f"Ataque  : {jugador['atk']}")
    print(f"Oro     : {jugador['oro']}")
    print(f"Items   : {jugador['inventario']}")
    print("=" * 40)


def crear_enemigo():

    ENEMIGOS_DISPONIBLES = [
        {"nombre": "El Cuero", "hp": 8, "atk": 2, "oro": 3},
        {"nombre": "La Fiura", "hp": 10, "atk": 3, "oro": 5},
        {"nombre": "Athrathrao", "hp": 12, "atk": 4, "oro": 7},
    ]

    enemigo = random.choice(ENEMIGOS_DISPONIBLES).copy()
    print(
        f"[DEBUG] Enemigo Generado: {enemigo['nombre']} (HP : {enemigo['hp']})"
    )
    return enemigo


def mostrar_estado_combate(jugador, enemigo):
    mostrar_estado_jugador(jugador)
    print(f"\n Enemigo: {enemigo['nombre']} | HP: {enemigo['hp']}")
    print("-" * 40)


ascii_art = figlet_format("DUNGEON", font="slant")
print(ROJO + ascii_art + RESET)
print(f"{BLANCO}Espere un momento a que cargue todo completamente..{RESET}")

time.sleep(0.5)
for i in tqdm(range(100), desc="Cargando datos", colour="red"):
    time.sleep(0.02)


print(
    "\nBienvenido a esta aventura RPG donde nos adentraremos a lo más profundo de estas cavernas, ¿estás preparado/a?"
)
opciones_ascii = figlet_format("SI / NO", font="small")
print(ROJO + opciones_ascii + RESET)

respuesta = input("Escriba su elección: ")

if respuesta.upper() != "SI":
    print(
        f"\n{ROJO}Has decidido retirarte. El calabozo permanecerá cerrado.{RESET}"
    )
    sys.exit()


print(f"\n{BLANCO}¡Excelente! Pues que comience esta aventura...{RESET}")
nombre_viajero = input("¿Primero, permíteme saber cuál es tu nombre viajero?: ")

jugador_actual = crear_jugador(nombre_viajero)

print("[INFO] Mostrando resultado inicial:")
mostrar_estado_jugador(jugador_actual)


time.sleep(1.5)
print(
    f"\n{BLANCO}Ajustas tu arma antes de emprender tu viaje y te adentras a la mazmorra...{RESET}"
)
time.sleep(2.0)

print(
    "Al apenas adentrarte, el aire se siente tenso y frío. Caminas hacia el fondo de un pasillo."
)
time.sleep(2.0)

print(
    "\nSientes que te observan por detrás y decides revisar un cuerpo que estaba tirado en el suelo..."
)
time.sleep(2.5)
print(
    "Al ver el cuerpo y notar que no tiene nada de importancia, te giras lentamente..."
)
print("-" * 50)

input(f"\n{ROJO}[Presiona ENTER para desenvainar tu arma y continuar]{RESET}")
print("-" * 50)


print("\n[CUIDADO] ¡Un enemigo salta hacia ti desde la oscuridad!")
time.sleep(1.0)

enemigo_actual = crear_enemigo()
mostrar_estado_combate( enemigo_actual)
def menu_batalla(jugado,enemigo):
    print