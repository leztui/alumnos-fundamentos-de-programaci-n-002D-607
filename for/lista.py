canciones_favoritas = ["Para amar - Los Prisioneros ", "Una nube cuelga sobre mi - Los Bunker", " La lisa - Lisa", "Milaagrosa - Milo J ", "Ven aqui - Los Bunkers"]

print("cantidad de canciones en la lista")

print(len(canciones_favoritas))

print(canciones_favoritas[len(canciones_favoritas)-1])

print(canciones_favoritas[-1])




canciones_favoritas.append("Congelao - cachureo")
canciones_favoritas.append("Mi gran noche - Rafael")

canciones_favoritas.pop()

contador = 0

for cancion in canciones_favoritas: 
    print(f"el nombre de la cancion es : {contador}es:{cancion}")
    contador = contador +1