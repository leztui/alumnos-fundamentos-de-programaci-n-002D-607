series = {
    'AN001': ['Attack on Titan', 'accion', 'MAPPA', 'M', False, 'Japon'],
    'AN002': ['Your Name', 'romance', 'CoMix Wave', 'PG', True, 'Japon'],
    'AN003': ['One Punch Man', 'comedia', 'J.C.Staff', 'PG', False, 'Japon'],
    'AN004': ['Kimetsu no Yaiba', 'accion', 'ufotable', 'PG', True, 'Japon'],
    'AN005': ['No Game No Life', 'isekai', 'Madhouse', 'PG', True, 'Japon'],
    'AN006': ['Violet Evergarden', 'drama', 'KyoAni', 'G', True, 'Japon'],
}

catalogo = {
    'AN001': [9990, 75],
    'AN002': [4990, 0],
    'AN003': [7990, 12],
    'AN004': [8990, 26],
    'AN005': [5990, 13],
    'AN006': [6990, 13],
}

animes_filtrados_por_rango_de_precio = []


def busqueda_precio(precio_minimo, precio_maximo):
    animes_filtrados_por_rango_de_precio.clear()  # evita que se acumulen resultados de búsquedas anteriores
    for cada_precio_en_el_catalogo in catalogo.items():
        if cada_precio_en_el_catalogo[1][0] >= precio_minimo and cada_precio_en_el_catalogo[1][0] <= precio_maximo:
            id_anime = cada_precio_en_el_catalogo[0]
            for cada_serie in series.items():
                if id_anime == cada_serie[0]:
                    dic_temporal_animes = {
                        "id_anime": cada_serie[0],
                        "nombre_anime": cada_serie[1][0],
                        "precio_anime": cada_precio_en_el_catalogo[1][0]
                    }
                    animes_filtrados_por_rango_de_precio.append(dic_temporal_animes)
    return animes_filtrados_por_rango_de_precio


def contar_capitulos_por_genero(genero_a_buscar):
    total_episodios_por_genero = 0
    for cada_serie in series.items():
        if cada_serie[1][1] == genero_a_buscar:
            for cada_serie_en_el_catalogo in catalogo.items():
                if cada_serie_en_el_catalogo[0] == cada_serie[0]:
                    total_episodios_por_genero += cada_serie_en_el_catalogo[1][1]
    return total_episodios_por_genero


def pedir_entero(mensaje):
    """Pide un valor por teclado hasta que sea un número entero válido."""
    while True:
        valor = input(mensaje)
        try:
            return int(valor)
        except ValueError:
            print("Debe ingresar valores enteros")


def opcion_episodios_por_genero():
    genero = input("Ingrese género a consultar: ").lower()
    total = contar_capitulos_por_genero(genero)
    print(f"El total de episodios disponibles es: {total}")


def opcion_busqueda_por_precio():
    precio_minimo = pedir_entero("Ingrese precio mínimo: ")
    precio_maximo = pedir_entero("Ingrese precio máximo: ")
    resultado = busqueda_precio(precio_minimo, precio_maximo)
    encontrados = [f"{anime['nombre_anime']}--{anime['id_anime']}" for anime in resultado]
    encontrados.sort()
    print(f"Las series encontradas son: {encontrados}")


def opcion_actualizar_precio():
    continuar = 's'
    while continuar == 's':
        codigo = input("Ingrese código de la serie: ").upper()
        nuevo_precio = pedir_entero("Ingrese nuevo precio: ")
        if codigo in catalogo:
            catalogo[codigo][0] = nuevo_precio
            print("Precio actualizado")
        else:
            print("El código no existe")
        continuar = input("¿Desea actualizar otro precio (s/n)?: ").lower()


def opcion_agregar_serie():
    codigo = input("Ingrese código de la serie: ").upper()
    titulo = input("Ingrese título: ")
    genero = input("Ingrese género: ").lower()
    estudio = input("Ingrese estudio: ")
    clasificacion = input("Ingrese clasificación (G/PG/M): ").upper()
    subtitulada = input("¿Está subtitulada al español? (s/n): ").lower() == 's'
    pais = input("Ingrese país de origen: ")
    precio = pedir_entero("Ingrese precio: ")
    episodios = pedir_entero("Ingrese episodios disponibles: ")

    series[codigo] = [titulo, genero, estudio, clasificacion, subtitulada, pais]
    catalogo[codigo] = [precio, episodios]
    print("Serie agregada")


def opcion_eliminar_serie():
    codigo = input("Ingrese código de la serie a eliminar: ").upper()
    if codigo in series:
        del series[codigo]
        del catalogo[codigo]
        print("Serie eliminada")
    else:
        print("El código no existe")


def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Episodios por género")
    print("2. Búsqueda de series por rango de precio")
    print("3. Actualizar precio de serie")
    print("4. Agregar serie")
    print("5. Eliminar serie")
    print("6. Salir")
    print("=====================================")


def main():
    mostrar_menu()
    opcion = None
    while opcion != 6:
        opcion = pedir_entero("Ingrese opción: ")

        if opcion == 1:
            opcion_episodios_por_genero()
        elif opcion == 2:
            opcion_busqueda_por_precio()
        elif opcion == 3:
            opcion_actualizar_precio()
        elif opcion == 4:
            opcion_agregar_serie()
        elif opcion == 5:
            opcion_eliminar_serie()
        elif opcion == 6:
            print("Programa finalizado.")
        else:
            print("Opción inválida, intente nuevamente")

        if opcion != 6:
            print()


main()