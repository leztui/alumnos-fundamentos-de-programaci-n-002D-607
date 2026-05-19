##tqdm es una libreria para crear barras de proceso
from tqdm import tqdm
##pyfiglet es una libreria para hacer un texto mas agradable
from pyfiglet import figlet_format
import time 
## me da herramientas para controlar variables y funciones
import sys
import random
import pyfiglet
## Colores ansi 
hp_inicial = 20 
ataque_inicial = 5
Salas_totales = 3

## Colores ansi 
ROJO = "\033[1;31m"
BLANCO = "\033[1;37m"
RESET = "\033[0m"

## FRont(fuente) definimos el estilo de diseño que tendran las letras
ascii_art = figlet_format ("DUNGEON", font="slant")
print(ROJO + ascii_art + RESET)
print()
print(f"{BLANCO}Espere un momento a que cargue todo completamente..{RESET}")
time.sleep(1.5)
for i in tqdm(range(100), desc="Cargando datos", colour="red"):
    time.sleep(0.03)
    
print("Bienvenido a esta aventura rpg donde nos adentraremos a lo mas profonda de estas cavernas , estas preparado/a?")
opciones_ascii = figlet_format("SI/NO", font ="small")
print(ROJO + opciones_ascii + RESET)
respuesta = input("Escriba su eleccion:")
if respuesta.upper() == "SI":
    print(f"\n{BLANCO}¡Excelente! Que comience la aventura...{RESET}")
else:
    print(f"\n{ROJO}Has decidido retirarte. El calabozo permanecerá cerrado.{RESET}")

def crear_jugador(nombre_ingreado):
    print(str(f"Creando jugador con nombre {nombre_ingreado}"))
    jugador = {
        "nombre" : nombre_ingreado,
        "hp": hp_inicial,
        "atk": ataque_inicial,
        "oro": 0,
        "inventario": ["Pocion"]
    }
    print(f"dato del jugador creados {jugador}")
    print()
    return jugador
if respuesta.upper() == "SI":
    print(f"\n{BLANCO} Pues que comienze esta aventura..{RESET}")
    nombre_viajero = input("¿Primero , permiteme saber cual es tu nombre viajero? :")
    jugador_actual = crear_jugador(nombre_viajero)
    print(f"Bienvenido al calabozo, {jugador_actual['nombre']}")
else:
    print(f"\n{ROJO}Has decidido retirarte {RESET}")