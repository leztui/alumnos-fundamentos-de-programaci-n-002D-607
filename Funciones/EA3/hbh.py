import random
import sys
import time
from pyfiglet import figlet_format
from tqdm import tqdm

ROJO_E = "\033[1;31m"
NARANJA_E = "\033[38;5;208m"
GRIS_OSCURO = "\033[1;30m"
BLANCO = "\033[1;37m"
RESET = "\033[0m"

SALAS_TOTALES = 5
DAÑO_HUIDA = 3
HP_POCION = 15

CLASES = {
    "1": {"nombre": "Guerrero de la Escoria", "hp": 30, "atk": 5, "arma": "Espada Dentada Oxidada"},
    "2": {"nombre": "Mago de Plasma", "hp": 18, "atk": 9, "arma": "Guantelete de Energía Inestable"},
    "3": {"nombre": "Arquero Mecánico", "hp": 22, "atk": 7, "arma": "Ballesta de Poleas"}
}

OBJETOS_MEJORA = [
    {"nombre": "Núcleo de Poder Sobrecargado", "mejora": "atk", "valor": 3, "desc": "Aumenta tu daño base permanentemente."},
    {"nombre": "Placas de Titanio Ensangrentadas", "mejora": "hp_max", "valor": 15, "desc": "Aumenta tu salud máxima."},
    {"nombre": "Inyector de Nanobots", "mejora": "cura", "valor": 50, "desc": "Una curación de emergencia masiva."}
]

def imprimir_lento(texto, retardo=0.03):
    for caracter in texto:
        sys.stdout.write(caracter)
        sys.stdout.flush()
        time.sleep(retardo)
    print()

def elegir_clase():
    print(f"\n{NARANJA_E}=== SELECCIÓN DE CLASE ==={RESET}")
    for clave, datos in CLASES.items():
        print(f" {ROJO_E}[{clave}]{RESET} {datos['nombre']} (Vida: {datos['hp']} | Daño Base: {datos['atk']})")
    
    eleccion = input(f"\n{BLANCO}Elige tu senda (1/2/3): {RESET}")
    while eleccion not in CLASES:
        eleccion = input(f"{ROJO_E}Elección inválida. Elige 1, 2 o 3: {RESET}")
    
    return CLASES[eleccion]

def crear_jugador(nombre_ingresado, clase_elegida):
    jugador = {
        "nivel": 1,
        "xp": 0,
        "xp_max": 10,
        "puntos_habilidad": 0,
        "nombre": nombre_ingresado,
        "clase": clase_elegida["nombre"],
        "arma": clase_elegida["arma"],
        "hp": clase_elegida["hp"],
        "hp_max": clase_elegida["hp"],
        "atk": clase_elegida["atk"],
        "oro": 0,
        "pociones": 1,
        "artefactos": []
    }
    return jugador

def mostrar_estado_jugador(jugador):
    print(f"\n{NARANJA_E}========================================{RESET}")
    print(f"{BLANCO}Operario : {jugador['nombre']} el {jugador['clase']}{RESET}")
    print(f"{GRIS_OSCURO}Nivel    : {jugador['nivel']} (XP: {jugador['xp']}/{jugador['xp_max']}){RESET}")
    print(f"{ROJO_E}Integridad: {jugador['hp']}/{jugador['hp_max']} | Daño: {jugador['atk']}{RESET}")
    print(f"{NARANJA_E}Créditos : {jugador['oro']} | Pociones: {jugador['pociones']}{RESET}")
    if jugador["artefactos"]:
        print(f"{BLANCO}Artefactos: {', '.join(jugador['artefactos'])}{RESET}")
    print(f"{NARANJA_E}========================================{RESET}")

def arbol_habilidades(jugador):
    while jugador["puntos_habilidad"] > 0:
        print(f"\n{NARANJA_E}=== TERMINAL DE MEJORAS ==={RESET}")
        print(f"Tienes {ROJO_E}{jugador['puntos_habilidad']}{RESET} puntos de habilidad disponibles.")
        print(f" {ROJO_E}[1]{RESET} Entrenar Fuerza (+3 Daño)")
        print(f" {ROJO_E}[2]{RESET} Reforzar Armadura (+10 Vida Máxima)")
        print(f" {ROJO_E}[3]{RESET} Guardar puntos para después")
        
        opcion = input("Elige una mejora: ")
        if opcion == "1":
            jugador["atk"] += 3
            jugador["puntos_habilidad"] -= 1
            imprimir_lento(f"{ROJO_E}Tus músculos se tensan. Tu daño ha aumentado.{RESET}")
        elif opcion == "2":
            jugador["hp_max"] += 10
            jugador["hp"] += 10
            jugador["puntos_habilidad"] -= 1
            imprimir_lento(f"{NARANJA_E}Tu resistencia es formidable. Vida máxima aumentada.{RESET}")
        elif opcion == "3":
            break
        else:
            print("Entrada no reconocida por el sistema.")

def generar_mazmorra():
    salas = ["Combate"] * (SALAS_TOTALES - 2)
    salas.append("Tesoro")
    random.shuffle(salas)
    salas.append("Jefe")
    return salas

def crear_enemigo(es_jefe=False):
    if es_jefe:
        return {"nombre": "Amalgama de Carne y Metal", "hp": 45, "atk": 8, "oro": 20, "xp": 30}
    
    ENEMIGOS = [
        {"nombre": "Dron Oxidado Mutante", "hp": 12, "atk": 3, "oro": 4, "xp": 5},
        {"nombre": "Sabueso de Neón", "hp": 18, "atk": 4, "oro": 6, "xp": 8},
        {"nombre": "Sectario Cibernético", "hp": 22, "atk": 5, "oro": 8, "xp": 12},
    ]
    return random.choice(ENEMIGOS).copy()

def subir_nivel(jugador):
    if jugador["xp"] >= jugador["xp_max"]:
        jugador["nivel"] += 1
        jugador["xp"] -= jugador["xp_max"]
        jugador["xp_max"] = int(jugador["xp_max"] * 1.6)
        jugador["hp_max"] += 5
        jugador["hp"] = jugador["hp_max"]
        jugador["puntos_habilidad"] += 1
        imprimir_lento(f"\n{NARANJA_E}¡Tus capacidades se expanden! Has alcanzado el NIVEL {jugador['nivel']}.{RESET}")
        arbol_habilidades(jugador)

def combate(jugador, enemigo, es_jefe):
    imprimir_lento(f"\n{ROJO_E}¡Una amenaza inminente bloquea tu camino: {enemigo['nombre']}!{RESET}")
    
    while jugador["hp"] > 0 and enemigo["hp"] > 0:
        print(f"\n{BLANCO}Tú: {jugador['hp']}/{jugador['hp_max']} HP | {ROJO_E}{enemigo['nombre']}: {enemigo['hp']} HP{RESET}")
        print(f" {NARANJA_E}[1]{RESET} Atacar con {jugador['arma']}")
        print(f" {NARANJA_E}[2]{RESET} Inyectar Poción ({jugador['pociones']} restantes)")
        print(f" {NARANJA_E}[3]{RESET} Huir cobardemente")
        
        accion = input("Ejecuta tu acción: ")
        
        if accion == "1":
            daño_infligido = jugador["atk"] + random.randint(0, 4)
            enemigo["hp"] -= daño_infligido
            print(f"{BLANCO}Acometes con violencia infligiendo {ROJO_E}{daño_infligido}{BLANCO} de daño.{RESET}")
            
            if enemigo["hp"] <= 0:
                imprimir_lento(f"{NARANJA_E}El {enemigo['nombre']} se desploma en un charco de fluidos oscuros.{RESET}")
                jugador["oro"] += enemigo["oro"]
                jugador["xp"] += enemigo["xp"]
                print(f"Obtienes {enemigo['oro']} créditos y {enemigo['xp']} puntos de experiencia.")
                if random.random() < 0.4:
                    jugador["pociones"] += 1
                    print(f"{BLANCO}Encontraste una poción intacta entre los restos.{RESET}")
                subir_nivel(jugador)
                return True
                
        elif accion == "2":
            if jugador["pociones"] > 0:
                jugador["pociones"] -= 1
                jugador["hp"] = min(jugador["hp_max"], jugador["hp"] + HP_POCION)
                print(f"{NARANJA_E}El líquido ardiente recorre tus venas. Recuperas vitalidad. (HP: {jugador['hp']}){RESET}")
            else:
                print(f"{GRIS_OSCURO}Buscas en tus bolsillos, pero no quedan pociones...{RESET}")
                continue
                
        elif accion == "3":
            if es_jefe:
                imprimir_lento(f"{ROJO_E}No puedes huir de tu destino. El jefe te acorrala.{RESET}")
                continue
            jugador["hp"] -= DAÑO_HUIDA
            imprimir_lento(f"{GRIS_OSCURO}Corres hacia las sombras tropezando con los escombros. Recibes {DAÑO_HUIDA} de daño en la huida.{RESET}")
            return True
            
        else:
            print("El pánico nubla tu mente. Pierdes tu turno.")
            
        if enemigo["hp"] > 0:
            daño_recibido = enemigo["atk"] + random.randint(0, 3)
            jugador["hp"] -= daño_recibido
            print(f"{ROJO_E}{enemigo['nombre']} contraataca ferozmente causándote {daño_recibido} de daño.{RESET}")

    return jugador["hp"] > 0

def sala_tesoro(jugador):
    imprimir_lento(f"\n{NARANJA_E}Entras a una recámara iluminada por una luz ámbar parpadeante...{RESET}")
    imprimir_lento(f"{BLANCO}En el centro del lugar, sobre un pedestal de engranajes, descansa un objeto milenario.{RESET}")
    
    objeto = random.choice(OBJETOS_MEJORA)
    print(f"\nHas descubierto: {ROJO_E}{objeto['nombre']}{RESET}")
    print(f"{GRIS_OSCURO}{objeto['desc']}{RESET}")
    
    if objeto["mejora"] == "atk":
        jugador["atk"] += objeto["valor"]
    elif objeto["mejora"] == "hp_max":
        jugador["hp_max"] += objeto["valor"]
        jugador["hp"] += objeto["valor"]
    elif objeto["mejora"] == "cura":
        jugador["hp"] = min(jugador["hp_max"], jugador["hp"] + objeto["valor"])
        
    jugador["artefactos"].append(objeto["nombre"])
    time.sleep(1)

def jugar():
    titulo = figlet_format("SECTOR 7", font="slant")
    print(ROJO_E + titulo + RESET)
    
    for i in tqdm(range(100), desc=f"{NARANJA_E}Inicializando sistemas{RESET}", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}"):
        time.sleep(0.01)

    print(f"\n{BLANCO}Las compuertas del complejo industrial se abren con un chirrido ensordecedor.{RESET}")
    nombre = input(f"{NARANJA_E}Ingresa tu designación operativa: {RESET}").strip() or "Sujeto de Pruebas"
    
    clase_elegida = elegir_clase()
    jugador = crear_jugador(nombre, clase_elegida)
    
    mostrar_estado_jugador(jugador)
    input(f"\n{ROJO_E}[Presiona ENTER para descender al abismo]{RESET}")

    mapa = generar_mazmorra()
    
    for indice, tipo_sala in enumerate(mapa, 1):
        print(f"\n{NARANJA_E}{'=' * 40}{RESET}")
        print(f"{BLANCO} ZONA {indice} de {SALAS_TOTALES} {RESET}")
        print(f"{NARANJA_E}{'=' * 40}{RESET}")
        time.sleep(1)
        
        if tipo_sala == "Tesoro":
            sala_tesoro(jugador)
        elif tipo_sala == "Combate":
            imprimir_lento(f"{GRIS_OSCURO}Avanzas por pasillos húmedos que huelen a óxido y muerte...{RESET}")
            enemigo = crear_enemigo()
            if not combate(jugador, enemigo, False):
                break
        elif tipo_sala == "Jefe":
            imprimir_lento(f"{ROJO_E}El suelo tiembla. Las luces de emergencia se encienden.{RESET}")
            imprimir_lento(f"{ROJO_E}Has llegado al núcleo del complejo.{RESET}")
            enemigo = crear_enemigo(es_jefe=True)
            if not combate(jugador, enemigo, True):
                break

        mostrar_estado_jugador(jugador)
        if indice < SALAS_TOTALES:
            input(f"\n{GRIS_OSCURO}[Presiona ENTER para avanzar a la siguiente zona...]{RESET}")

    print(f"\n{NARANJA_E}" + "=" * 45 + RESET)
    if jugador["hp"] > 0:
        print(f"{BLANCO}  TRANSMISIÓN COMPLETADA — Sobreviviste al Sector 7.{RESET}")
        print(f"  Operario:  {jugador['nombre']}")
        print(f"  Nivel Final: {jugador['nivel']}")
        print(f"  Créditos Extraídos: {jugador['oro']}")
    else:
        print(f"{ROJO_E}  SEÑAL PERDIDA — Tu biomasa ahora pertenece al complejo.{RESET}")
        print(f"  Caíste en la zona {indice} de {SALAS_TOTALES}.")
    print(f"{NARANJA_E}" + "=" * 45 + RESET)

if __name__ == "__main__":
    jugar()