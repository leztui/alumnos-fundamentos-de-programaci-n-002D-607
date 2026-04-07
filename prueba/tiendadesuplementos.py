contador = 0
producto = 0
producto_a_vender = 0
total_ventas = 0
print("Bienvenido a mi tienda de confianza de suplementos ")
print()
print(" Cuántos productos quieres vender? ")
while True:
        precio = int(input("precio del suplemento a vender: "))
        producto_a_vender += 1
        total_ventas += precio
        print(f"Total de productos a vender: {producto_a_vender}")
        print(f"Total de ventas: {total_ventas}")
        if producto_a_vender >= 3: 
           total_ventas = total_ventas * 0.9
        print(f"por la compra de 3 productos le damos un descuento del 10%: {total_ventas}")
        contador += 1
        print(f"Producto {contador}: Precio = {precio}")
        print(f"Total de productos a vender: {producto_a_vender}")
        print(f"Total de ventas: {total_ventas}")
        if precio <= 0:
            break

