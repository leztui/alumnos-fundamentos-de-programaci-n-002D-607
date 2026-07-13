productos_detalles = {
    'CP001': ['Procesador i7', 'CPU', 'Intel', True, 2026],
    'CP002': ['Procesador R7', 'CPU', 'AMD', True, 2026],
    'RM001': ['RAM 16GB', 'RAM', 'Kingston', True, 2026],
    'RM002': ['RAM 32GB', 'RAM', 'Corsair', True, 2026],
    'GP001': ['RTX 4070', 'GPU', 'Nvidia', True, 2026],
    'SS001': ['SSD 1TB', 'SSD', 'Samsung', True, 2026],
}

inventario_financiero = {
    'CP001': [350000, 15],
    'CP002': [320000, 10],
    'RM001': [80000, 50],
    'RM002': [150000, 30],
    'GP001': [650000, 5],
    'SS001': [90000, 40],
}

productos_filtrados_temporalmente = []

def buscar_productos_por_precio(precio_minimo, precio_maximo):
    productos_filtrados_temporalmente.clear()
    for identificador, datos_financieros in inventario_financiero.items():
        if datos_financieros[0] >= precio_minimo and datos_financieros[0] <= precio_maximo:
            if identificador in productos_detalles:
                detalles = productos_detalles[identificador]
                diccionario_temporal = {
                    "id_producto": identificador,
                    "nombre_producto": detalles[0],
                    "precio_producto": datos_financieros[0]
                }
                productos_filtrados_temporalmente.append(diccionario_temporal)
    return productos_filtrados_temporalmente

def contar_stock_por_categoria(categoria_a_buscar):
    total_stock_por_categoria = 0
    for identificador, detalles in productos_detalles.items():
        if detalles[1] == categoria_a_buscar:
            if identificador in inventario_financiero:
                total_stock_por_categoria += inventario_financiero[identificador][1]
    return total_stock_por_categoria

def pedir_entero_valido(mensaje):
    while True:
        valor = input(mensaje)
        try:
            return int(valor)
        except ValueError:
            print("Debe ingresar un valor numérico entero.")

def opcion_stock_por_categoria():
    categoria = input("Ingrese categoría a consultar: ").upper()
    total = contar_stock_por_categoria(categoria)
    print(f"El total de unidades en stock para {categoria} es: {total}")

def opcion_busqueda_por_precio():
    minimo = pedir_entero_valido("Ingrese precio mínimo: ")
    maximo = pedir_entero_valido("Ingrese precio máximo: ")
    resultado = buscar_productos_por_precio(minimo, maximo)
    encontrados = [f"{p['nombre_producto']}--{p['id_producto']}" for p in resultado]
    encontrados.sort()
    print(f"Productos encontrados: {encontrados}")

def opcion_actualizar_precio():
    continuar = 's'
    while continuar == 's':
        codigo = input("Ingrese código del producto: ").upper()
        nuevo_precio = pedir_entero_valido("Ingrese nuevo precio: ")
        if codigo in inventario_financiero:
            inventario_financiero[codigo][0] = nuevo_precio
            print("Precio actualizado correctamente.")
        else:
            print("El código no existe en el sistema.")
        continuar = input("¿Desea actualizar otro precio (s/n)?: ").lower()

def opcion_agregar_producto():
    codigo = input("Ingrese nuevo código (Ej: CP003): ").upper()
    nombre = input("Ingrese nombre del producto: ")
    categoria = input("Ingrese categoría: ").upper()
    marca = input("Ingrese marca: ")
    anio = pedir_entero_valido("Ingrese año de lanzamiento: ")
    precio = pedir_entero_valido("Ingrese precio: ")
    stock = pedir_entero_valido("Ingrese stock inicial: ")

    productos_detalles[codigo] = [nombre, categoria, marca, True, anio]
    inventario_financiero[codigo] = [precio, stock]
    print("Producto agregado con éxito.")

def opcion_eliminar_producto():
    codigo = input("Ingrese código a eliminar: ").upper()
    if codigo in productos_detalles:
        del productos_detalles[codigo]
        del inventario_financiero[codigo]
        print("Producto eliminado.")
    else:
        print("El código no existe.")

def mostrar_menu():
    print("========== MENÚ TIENDA DE COMPUTADORES ==========")
    print("1. Stock total por categoría")
    print("2. Búsqueda por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("=================================================")

def main():
    opcion = None
    while opcion != 6:
        mostrar_menu()
        opcion = pedir_entero_valido("Ingrese opción: ")

        if opcion == 1:
            opcion_stock_por_categoria()
        elif opcion == 2:
            opcion_busqueda_por_precio()
        elif opcion == 3:
            opcion_actualizar_precio()
        elif opcion == 4:
            opcion_agregar_producto()
        elif opcion == 5:
            opcion_eliminar_producto()
        elif opcion == 6:
            print("Cerrando sistema de la tienda.")
        else:
            print("Opción inválida.")
        print()

main()