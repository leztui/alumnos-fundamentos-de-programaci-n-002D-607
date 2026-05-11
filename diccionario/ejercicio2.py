productos = [
    {
        "nombre": "Laptop",
        "precio": 800,
        "stock": 10
    },
    {
        "nombre": "mouse",
        "precio": 30, 
        "stock": 20 
    },
    {
        "nombre": "teclado",
        "precio": 40,
        "stock": 15
    }
]

print("///////////////////////////////////////////////////////")
print("//////////////LISTA DE PRODUCTOS //////////////////////")
print("///////////////////////////////////////////////////////")
disponibles = 0
for p in productos :
    print(f"Productos: {p["nombre"]} - Precio: {p["precio"]}")
if p['stock'] > 0:
        print("Estado: En stock")
        disponibles += 1
else :
        print("Estado: Sin stock")
        print("-" * 20)

print(f"Total de productos disponibles: {disponibles}")