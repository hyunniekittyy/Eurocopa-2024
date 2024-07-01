import time
import json
from requests import get
from gestion_partidos_estadios import GestionPartidosEstadios
from gestion_entrada import GestionAsistenciaPartidos, GestionVentaEntradas
from gestion_restaurante import GestionRestaurante, GestionVentaRestaurantes
from gestion_indicadores import IndicadoresGestion

# Función para cargar datos desde la API
def cargar_datos_api(url):
    try:
        response = get(url)
        if response.status_code == 200:
            data = json.loads(response.content)
            return data
        else:
            print(f"Error al cargar los datos desde {url}. Estado de la respuesta: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error al cargar los datos desde {url}: {str(e)}")
        return None

# Función para imprimir el mapa del estadio
def imprimir_mapa_estadio(venta_entradas):
    print("\nMapa del Estadio:\n")
    print("Campo")
    print("---------------------------------------------")
    print("  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O")
    print("---------------------------------------------")
    for fila in range(1, 11):
        fila_mapa = f"{fila} "
        for columna in range(ord('A'), ord('O') + 1):
            columna_mapa = chr(columna)
            if (fila, columna_mapa) in venta_entradas.asientos_ocupados:
                fila_mapa += "❌ "
            else:
                fila_mapa += "💺 "
        print(fila_mapa)
    print("---------------------------------------------")

# Función para mostrar los partidos y estadios
def mostrar_partidos_y_estadios(gestion_partidos_estadios):
    gestion_partidos_estadios.mostrar_partidos()
    gestion_partidos_estadios.mostrar_estadios()

# Función para vender una entrada
def vender_entrada(gestion_entradas):
    print("\nVenta de Entradas:")
    gestion_entradas.mostrar_partidos()
    id_partido = input("Ingrese el ID del partido para el cual desea comprar la entrada: ")
    tipo_entrada = input("Ingrese el tipo de entrada (General/VIP): ").lower()
    gestion_entradas.vender_entrada(id_partido, tipo_entrada)

# Función para registrar la asistencia a un partido
def registrar_asistencia(gestion_asistencia):
    print("\nRegistro de Asistencia a Partidos:")
    gestion_asistencia.mostrar_partidos()
    id_partido = input("Ingrese el ID del partido para registrar la asistencia: ")
    cantidad_asistentes = int(input("Ingrese la cantidad de personas que asistieron al partido: "))
    gestion_asistencia.registrar_asistencia(id_partido, cantidad_asistentes)

# Función para mostrar el menú de restaurantes
def mostrar_menu_restaurantes(gestion_restaurantes):
    print("\nMenú de Restaurantes:")
    gestion_restaurantes.mostrar_menu_restaurantes()

# Función para vender un producto de restaurante
def vender_producto_restaurante(gestion_venta_restaurantes):
    print("\nVenta de Productos del Restaurante:")
    gestion_venta_restaurantes.mostrar_menu_restaurantes()
    id_producto = input("Ingrese el ID del producto que desea comprar: ")
    cantidad = int(input("Ingrese la cantidad que desea comprar: "))
    gestion_venta_restaurantes.vender_producto_restaurante(id_producto, cantidad)

# Función para mostrar las opciones de estadísticas e interactuar con ellas
def menu_estadisticas(indicadores):
    while True:
        print("\nIndicadores de Gestión (Estadísticas):")
        print("1. Promedio de gasto de un cliente VIP")
        print("2. Tabla de asistencia a partidos")
        print("3. Partido con mayor asistencia")
        print("4. Partido con mayor cantidad de boletos vendidos")
        print("5. Top 3 productos más vendidos en el restaurante")
        print("6. Top 3 clientes que más compraron")
        print("7. Volver al menú principal")

        opcion_estadisticas = int(input("Seleccione una opción de estadísticas: "))

        if opcion_estadisticas == 1:
            print(f"Promedio de gasto de un cliente VIP: {indicadores.promedio_gasto_cliente_vip()}")

        elif opcion_estadisticas == 2:
            tabla_asistencia = indicadores.tabla_asistencia_partidos()
            print("\nTabla de Asistencia a Partidos:")
            for partido in tabla_asistencia:
                print(partido)

        elif opcion_estadisticas == 3:
            partido_max_asistencia = indicadores.partido_con_mayor_asistencia()
            if partido_max_asistencia:
                print(f"Partido con mayor asistencia: {partido_max_asistencia.nombre_partido()}")

        elif opcion_estadisticas == 4:
            partido_max_boletos = indicadores.partido_con_mas_boletos_vendidos()
            if partido_max_boletos:
                print(f"Partido con mayor boletos vendidos: {partido_max_boletos.nombre_partido()}")

        elif opcion_estadisticas == 5:
            top_productos = indicadores.top_productos_mas_vendidos()
            print("\nTop 3 Productos más Vendidos:")
            for i, producto in enumerate(top_productos, start=1):
                print(f"{i}. {producto[0]} - {producto[1]} unidades vendidas")

        elif opcion_estadisticas == 6:
            top_clientes = indicadores.top_clientes_mas_compras()
            print("\nTop 3 Clientes que más Compraron:")
            for i, cliente in enumerate(top_clientes, start=1):
                print(f"{i}. {cliente[0]} - {cliente[1]} compras")

        elif opcion_estadisticas == 7:
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del menú de estadísticas.\n")

# Función para el menú principal
def menu_principal():
    print("Cargando datos de la API del request...")
    time.sleep(2)  # Simulación de carga de datos
    datos_cargados = cargar_datos_api("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json")
    
    if datos_cargados:
        print("Datos cargados satisfactoriamente.")
        print("Bienvenido a la Eurocopa 2024\n")

        gestion_partidos_estadios = GestionPartidosEstadios(datos_cargados)
        gestion_entradas = GestionVentaEntradas(gestion_partidos_estadios)
        gestion_asistencia = GestionAsistenciaPartidos(gestion_partidos_estadios)
        gestion_restaurantes = GestionRestaurante(datos_cargados)
        gestion_venta_restaurantes = GestionVentaRestaurantes(gestion_restaurantes)
        indicadores = IndicadoresGestion(gestion_entradas, gestion_asistencia, gestion_venta_restaurantes)

        opcion = 0
        while opcion != 7:
            print("Menú Principal:")
            print("1. Gestión de partidos y estadios")
            print("2. Gestión de venta de entradas")
            print("3. Gestión de asistencia a partidos")
            print("4. Gestión de restaurantes")
            print("5. Gestión de venta de restaurantes")
            print("6. Indicadores de gestión (estadísticas)")
            print("7. Salir")

            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                while True:
                    print("\nMenú de Gestión de Partidos y Estadios:")
                    print("1. Mostrar partidos y estadios")
                    print("2. Volver al menú principal")

                    opcion_gestion_partidos = int(input("Seleccione una opción: "))

                    if opcion_gestion_partidos == 1:
                        mostrar_partidos_y_estadios(gestion_partidos_estadios)
                    elif opcion_gestion_partidos == 2:
                        break
                    else:
                        print("Opción no válida. Por favor, seleccione una opción válida.")

            elif opcion == 2:
                while True:
                    print("\nMenú de Gestión de Venta de Entradas:")
                    print("1. Vender entrada")
                    print("2. Mostrar mapa del estadio")
                    print("3. Volver al menú principal")

                    opcion_venta_entradas = int(input("Seleccione una opción: "))

                    if opcion_venta_entradas == 1:
                        vender_entrada(gestion_entradas)
                    elif opcion_venta_entradas == 2:
                        imprimir_mapa_estadio(gestion_entradas)
                    elif opcion_venta_entradas == 3:
                        break
                    else:
                        print("Opción no válida. Por favor, seleccione una opción válida.")

            elif opcion == 3:
                while True:
                    print("\nMenú de Gestión de Asistencia a Partidos:")
                    print("1. Registrar asistencia a partido")
                    print("2. Volver al menú principal")

                    opcion_asistencia_partidos = int(input("Seleccione una opción: "))

                    if opcion_asistencia_partidos == 1:
                        registrar_asistencia(gestion_asistencia)
                    elif opcion_asistencia_partidos == 2:
                        break
                    else:
                        print("Opción no válida. Por favor, seleccione una opción válida.")

            elif opcion == 4:
                while True:
                    print("\nMenú de Gestión de Restaurantes:")
                    print("1. Mostrar menú de restaurantes")
                    print("2. Volver al menú principal")

                    opcion_gestion_restaurantes = int(input("Seleccione una opción: "))

                    if opcion_gestion_restaurantes == 1:
                        mostrar_menu_restaurantes(gestion_restaurantes)
                    elif opcion_gestion_restaurantes == 2:
                        break
                    else:
                        print("Opción no válida. Por favor, seleccione una opción válida.")

            elif opcion == 5:
                while True:
                    print("\nMenú de Gestión de Venta de Restaurantes:")
                    print("1. Vender producto del restaurante")
                    print("2. Volver al menú principal")

                    opcion_venta_restaurantes = int(input("Seleccione una opción: "))

                    if opcion_venta_restaurantes == 1:
                        vender_producto_restaurante(gestion_venta_restaurantes)
                    elif opcion_venta_restaurantes == 2:
                        break
                    else:
                        print("Opción no válida. Por favor, seleccione una opción válida.")

            elif opcion == 6:
                menu_estadisticas(indicadores)

            elif opcion == 7:
                print("Saliendo del programa...")
                break

            else:
                print("Opción no válida. Por favor, seleccione una opción del menú.\n")

    else:
        print("No se pudieron cargar los datos. Revise la conexión a Internet o inténtelo más tarde.")

# Ejecutar el programa
if __name__ == "__main__":
    menu_principal()

