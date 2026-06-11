from colorama import Back, Fore, init , Style
init()
menos_rojo = Fore.RED + "-" + Style.RESET_ALL
def init_hp_bar(fighter):
    print(f"La vida es")
    return fighter["hp"] * "/"
def init_name(figther):
    print(" EL nombre es")
    return figther["name"]
def init_id(figther):
    print("EL id es")
    return figther["id"]
def init_attack(figther):
    print("Lista de ataques")
    return figther["attack"]

def pelea( data_copper , data_thief ):
    print(f"El policia se llama {data_copper["name"]}")
    print(f"El ladron se llama {data_thief["name"]}")

copper = {
    "id" : "P-01",
    "name" : "Benajmin Moena",
    "hp" : 100,
    "attack" : [
        {"attack_name": "Pistola", "attack_damage" : 90 },
        {"attack_name": "BUKAKE", "attack_damage" : 15}
    ]
}    
human = {
    "id" : "P-02",
    "name" : "ABEL CAVER",
    "hp" : 150,
    "attack" : [
        {"attack_name": "MOMAZO_ABEL", "attack_damage" : 70 },
        {"attack_name": "QUIERO_KEKE", "attack_damage" : 20}

    ]
} 
thief= {

    "id" : "P-03",
    "name" : "AMARO",
    "hp" : 200,
    "attack" : [
        {"attack_name": "PORNAZO", "attack_damage" : 50 },
        {"attack_name": "SOY_UN_AUTO", "attack_damage" : 90}
        
    ]
}    
print(f"{menos_rojo}" "-"*10)
print(init_id(copper))
print(f"{menos_rojo}" "-"*10)
print(init_name(copper))
print(f"{menos_rojo}" "-"*10)
print(init_hp_bar(copper))
print(f"{menos_rojo}" "-"*10)
print(init_attack(copper))
print(f"{menos_rojo}" "-"*10)
