import random
import sys
import time
from pyfiglet import figlet_format
from tqdm import tqdm

hp_inicial = 20
ataque_inicial = 5
SALAS_TOTALES = 3
DAÑO_HUIDA = 2
HP_POCION = 8

ROJO = "\033[1;31m"
BLANCO = "\033[1;37m"
RESET = "\033[0m"

def crear_jugador(nombre_ingresado):
    print(f"Creando jugador con nombre {nombre_ingresado}...")
    jugador = {
        "nivel": 1,
        "xp": 0,
        "xp_max": 10,
        "nombre": nombre_ingresado,
        "hp": hp_inicial,
        "hp_max": hp_inicial,
        "atk": ataque_inicial,
        "oro": 0,
        "inventario": ["Poción"],
    }
    print(f"Jugador creado con éxito.\n")
    return jugador

def mostrar_estado_jugador(jugador):
    print("\n" + "=" * 40)
    print(f"Nivel   : {jugador['nivel']} (XP: {jugador['xp']}/{jugador['xp_max']})")
    print(f"Héroe   : {jugador['nombre']}")
    print(f"Vida    : {jugador['hp']}/{jugador['hp_max']}")
    print(f"Ataque  : {jugador['atk']}")
    print(f"Oro     : {jugador['oro']}")
    print(f"Items   : {jugador['inventario']}")
    print("=" * 40)

def crear_enemigo():
    ENEMIGOS_DISPONIBLES = [
        {"nombre": "El Cuero", "hp": 8, "atk": 2, "oro": 3, "xp": 5},
        {"nombre": "La Fiura", "hp": 10, "atk": 3, "oro": 5, "xp": 7},
        {"nombre": "Athrathrao", "hp": 12, "atk": 4, "oro": 7, "xp": 12},
    ]
    enemigo = random.choice(ENEMIGOS_DISPONIBLES).copy()
    print(f"[DEBUG] Enemigo Generado: {enemigo['nombre']} (HP : {enemigo['hp']})")
    return enemigo

def mostrar_estado_combate(jugador, enemigo):
    mostrar_estado_jugador(jugador)
    print(f"\n Enemigo: {enemigo['nombre']} | HP: {enemigo['hp']}")
    print("-" * 40)

def esta_vivo(personaje):
    return personaje["hp"] > 0

def subir_nivel(jugador):
    if jugador["xp"] >= jugador["xp_max"]:
        jugador["nivel"] += 1
        jugador["xp"] -= jugador["xp_max"]
        jugador["xp_max"] = int(jugador["xp_max"] * 1.5)
        jugador["hp_max"] += 5
        jugador["hp"] = jugador["hp_max"]
        jugador["atk"] += 2
        print(f"\n{BLANCO}¡Sube la determinación! Has alcanzado el NIVEL {jugador['nivel']}.{RESET}")

def dar_recompensa(jugador, enemigo):
    jugador["oro"] += enemigo["oro"]
    jugador["xp"] += enemigo["xp"]
    encontro_pocion = random.random() < 0.5  

    if encontro_pocion:
        jugador["inventario"].append("Poción")

    print(f"[DEBUG] Recompensa: +{enemigo['oro']} oro | +{enemigo['xp']} XP")
    subir_nivel(jugador)
    return encontro_pocion

def usar_pocion(jugador):
    if "Poción" in jugador["inventario"]:
        jugador["inventario"].remove("Poción")
        hp_antes = jugador["hp"]
        jugador["hp"] += HP_POCION

        if jugador["hp"] > jugador["hp_max"]:
            jugador["hp"] = jugador["hp_max"]

        print(f"[DEBUG] Poción usada → HP: {hp_antes} → {jugador['hp']}")
        return True

    print("[DEBUG] No había poción en el inventario.")
    return False

def jugador_ataca(jugador, enemigo):
    daño = jugador["atk"] + random.randint(0, 3)
    enemigo["hp"] -= daño
    print(f"[DEBUG] Jugador ataca → daño: {daño} | HP enemigo: {enemigo['hp']}")
    return daño

def enemigo_ataca(jugador, enemigo):
    daño = enemigo["atk"] + random.randint(0, 2)
    jugador["hp"] -= daño
    print(f"[DEBUG] Enemigo ataca → daño: {daño} | HP jugador: {jugador['hp']}")
    return daño

def mostrar_menu_combate():
    print(f"\n{ROJO}{RESET} Opciones de Combate:")
    print(f"  [{ROJO}1{RESET}]  Luchar")
    print(f"  [{ROJO}2{RESET}]  inspecionar")
    print(f"  [{ROJO}3{RESET}]  Objeto")
    print(f"  [{ROJO}4{RESET}]  Piedad")
    return input("Elige tu acción: ")

def combate(jugador, enemigo):
    print(f"\n[INFO] ¡Comienza el combate vs {enemigo['nombre']}!")

    while esta_vivo(jugador) and esta_vivo(enemigo):
        mostrar_estado_combate(jugador, enemigo)
        opcion = mostrar_menu_combate()

        if opcion == "1":
            daño = jugador_ataca(jugador, enemigo)
            print(f"  Golpeas y haces {daño} de daño.")
            if not esta_vivo(enemigo):
                print(f"  ¡Derrotaste a {enemigo['nombre']}!")
                encontro = dar_recompensa(jugador, enemigo)
                print(f"  Ganas {enemigo['oro']} de oro y {enemigo['xp']} XP.")
                if encontro:
                    print("  Encontraste una poción.")
                break
            daño_r = enemigo_ataca(jugador, enemigo)
            print(f"  {enemigo['nombre']} te hace {daño_r} de daño.")

        elif opcion == "2":
            print(f"  Revisas a {enemigo['nombre']}... parece un oponente muy fuerte . Te preparas para su ataque.")
            daño_r = enemigo_ataca(jugador, enemigo)
            print(f"  {enemigo['nombre']} te hace {daño_r} de daño.")

        elif opcion == "3":
            if usar_pocion(jugador):
                print("  Usas una poción y recuperas vida.")
            else:
                print("  No tienes pociones. Pierdes tu oportunidad.")
            
            if esta_vivo(enemigo):
                dano_r = enemigo_ataca(jugador, enemigo)
                print(f"  {enemigo['nombre']} te hace {dano_r} de daño.")

        elif opcion == "4":
            jugador["hp"] -= DAÑO_HUIDA
            print(f"  Consigues escapar. Pierdes {DAÑO_HUIDA} HP durante la huida. HP actual: {jugador['hp']}")
            break

        else:
            print(f"  Opción '{opcion}' inválida. Elige 1, 2, 3 o 4.")

    return esta_vivo(jugador)

def explorar_caminos():
    print(f"\n{BLANCO}Frente a ti se abren distintos caminos en la mazmorra...{RESET}")
    print("  [1] Ir por el pasillo de la izquierda (Se siente un aire helado)")
    print("  [2] Ir por el pasillo de la derecha (Escuchas un goteo constante)")
    print("  [3] Seguir todo recto (El camino está sumido en la oscuridad total)")
    eleccion = input("¿Hacia dónde decides ir? ")
    
    if eleccion == "1":
        print("\nTe adentras en el pasillo izquierdo temblando por el frío...")
    elif eleccion == "2":
        print("\nCaminas hacia la derecha esquivando charcos en el suelo...")
    else:
        print("\nAvanzas directamente hacia la oscuridad preparándote para lo peor...")
    time.sleep(1.5)

def jugar():
    ascii_art = figlet_format("DUNGEON", font="slant")
    print(ROJO + ascii_art + RESET)
    print(f"{BLANCO}Espere un momento a que cargue todo completamente..{RESET}")

    time.sleep(0.5)
    for i in tqdm(range(100), desc="Cargando datos", colour="red"):
        time.sleep(0.02)

    print("\nBienvenido a esta aventura RPG donde nos adentraremos a lo más profundo de estas cavernas, ¿estás preparado/a?")
    opciones_ascii = figlet_format("SI / NO", font="small")
    print(ROJO + opciones_ascii + RESET)

    respuesta = input("Escriba su elección: ")

    if respuesta.upper() != "SI":
        print(f"\n{ROJO}Has decidido retirarte. El calabozo permanecerá cerrado.{RESET}")
        sys.exit()

    print(f"\n{BLANCO}¡Excelente! Pues que comience esta aventura...{RESET}")
    nombre = input("¿Primero, permíteme saber cuál es tu nombre viajero?: ").strip()
    
    if nombre == "":
        nombre = "Héroe Anónimo"
        print("[INFO] Nombre vacío → usando 'Héroe Anónimo'")

    jugador = crear_jugador(nombre)
    print("[INFO] Mostrando resultado inicial:")
    mostrar_estado_jugador(jugador)

    time.sleep(1.5)
    print(f"\n{BLANCO}Ajustas tu arma antes de emprender tu viaje y te adentras a la mazmorra...{RESET}")
    time.sleep(2.0)
    print("Al apenas adentrarte, el aire se siente tenso y frío. Caminas hacia el fondo de un pasillo.")
    time.sleep(2.0)
    print("\nSientes que te observan por detrás y decides revisar un cuerpo que estaba tirado en el suelo...")
    time.sleep(2.5)
    print("Al ver el cuerpo y notar que no tiene nada de importancia, te giras lentamente...")
    print("-" * 50)
    input(f"\n{ROJO}[Presiona ENTER para desenvainar tu arma y continuar]{RESET}")
    print("-" * 50)

    sala_actual = 1

    while sala_actual <= SALAS_TOTALES and esta_vivo(jugador):
        print(f"\n{'─' * 45}")
        print(f"  SALA {sala_actual} de {SALAS_TOTALES}")
        print(f"{'─' * 45}")
        
        explorar_caminos()
        
        print("\n[CUIDADO] ¡Un enemigo salta hacia ti desde la oscuridad!")
        time.sleep(1.0)

        enemigo = crear_enemigo()
        sobrevivio = combate(jugador, enemigo)

        if not sobrevivio:
            print(f"[INFO] Jugador derrotado en sala {sala_actual}.")
            break

        print(f"[DEBUG] Sala {sala_actual} completada | HP: {jugador['hp']}")
        sala_actual += 1

        if sala_actual <= SALAS_TOTALES:
            input("\n  [Presiona ENTER para continuar...]")

    print("\n" + "=" * 45)
    if esta_vivo(jugador):
        print("  VICTORIA — Limpiaste la mazmorra.")
        print(f"  Héroe:  {jugador['nombre']}")
        print(f"  Nivel:  {jugador['nivel']}")
        print(f"  Oro:    {jugador['oro']}")
        print(f"  Vida:   {jugador['hp']}/{jugador['hp_max']}")
        print(f"  Items:  {jugador['inventario']}")
    else:
        print("  DERROTA — Caíste en las sombras.")
        print(f"  Llegaste hasta la sala {sala_actual} de {SALAS_TOTALES}.")
    print("=" * 45)

if __name__ == "__main__":
    jugar()