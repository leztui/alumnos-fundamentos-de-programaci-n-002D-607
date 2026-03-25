print("BIENVENIDO A ESTE PROGRAMA DE ADIVINANZA")
print()
print("########################################")
print("intenta adivinar el  numero del 1-10")
print("########################################")
print()
print("intenta adivinarlo ")
print()
numero_secreto = 6
while True:
    numero_usuario = int(input("ingresa un numero: "))
    if numero_usuario == numero_secreto:
        print("FELICIDADES ADIVINASTE EL NUMERO ")
        break
    else:
        print("intenta de nuevo")