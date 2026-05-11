Libro = {
    "libro": "El principito",
    "autor": "Saint-Exupéry",
    "anio":"1934"
}

print("Nombre:",  {Libro["libro"]})
print("Edad:",  {Libro["autor"]})
print("Notas:", {Libro["anio"]})

Libro["anio"] : "2024"
Libro["Editorial"] = "Sudamerica" 
print("Diccionario actualizado:")
print(Libro)