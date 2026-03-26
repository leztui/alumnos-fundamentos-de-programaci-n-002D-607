opcion_usuario1 = ""
opcion_usuario2 = ""

puntaje_usuario1 = 0
puntaje_usuario2 = 0
 

print("Bienvenido al juego de piedra, papel o tijera")
print()
print("porfavor ecribe la palabra piedra, papel o tijeras")
print()
opcion_usuario1 = input("J1 - Porfavor inrese su opcion: ")
print()
opcion_usuario2 = input("J2 - Porfavor inrese su opcion: ")

if opcion_usuario1 == "piedra" and opcion_usuario2 == "tijeras":
    print()
    print("J1 gana 1 punto")
    puntaje_usuario1 += 1
elif opcion_usuario1 == "papel" and opcion_usuario2 == "piedra":
    print()
    print("J1 gana 1 punto")
    puntaje_usuario1 += 1
elif opcion_usuario1 == "tijeras" and opcion_usuario2 == "papel":
    print()
    print("J1 gana 1 punto")
    puntaje_usuario1 += 1
elif opcion_usuario1 == opcion_usuario2:
    print("Empate")
else:
    print
    print("J2 gana 1 punto")
    puntaje_usuario2 += 1

