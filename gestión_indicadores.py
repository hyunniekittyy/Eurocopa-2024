from collections import defaultdict
import matplotlib.pyplot as plt

class IndicadoresGestion:
    """
        Inicializa los indicadores de gestión con las instancias de gestión de partidos, entradas y restaurante.

        Args:
        - gestion_partidos (GestionPartidos): Instancia de gestión de partidos.
        - gestion_entradas (GestionEntradas): Instancia de gestión de entradas.
        - gestion_restaurante (GestionRestaurante): Instancia de gestión de restaurante.
    """
    def __init__(self, gestion_partidos, gestion_entradas, gestion_restaurante):
        self.gestion_partidos = gestion_partidos
        self.gestion_entradas = gestion_entradas
        self.gestion_restaurante = gestion_restaurante

    def promedio_gasto_cliente_vip(self):
        """
        Calcula el promedio de gasto de los clientes VIP en el restaurante.

        Returns:
        - float: Promedio de gasto de los clientes VIP.
        """
        total_gastos = 0
        num_clientes_vip = 0
        for venta in self.gestion_restaurante.ventas:
            cliente = venta['cliente']
            productos = venta['productos']  # Se obtienen los productos de la venta
            if self.gestion_entradas.validar_cliente_vip(cliente.cedula):
                total_gastos += venta['costo']  # Se suma el costo de la venta
                num_clientes_vip += 1

        if num_clientes_vip > 0:
            promedio = total_gastos / num_clientes_vip
            return promedio
        else:
            return 0.0

    def tabla_asistencia_partidos(self):
        """
        Genera una tabla con información de asistencia a los partidos, ordenada por la relación asistencia/venta.

        Returns:
        - list: Lista de diccionarios con la información de cada partido ordenada.
        """
        partidos = self.gestion_partidos.obtener_todos_partidos()
        partidos_ordenados = sorted(partidos, key=lambda partido: partido.asistencia(), reverse=True)
        tabla = []
        for partido in partidos_ordenados:
            fila = {
                'Nombre del partido': partido.nombre,
                'Estadio': partido.estadio.nombre,
                'Boletos vendidos': partido.boletos_vendidos,
                'Personas que asistieron': partido.personas_asistieron,
                'Relación asistencia/venta': partido.relacion_asistencia_venta()
            }
            tabla.append(fila)
        return tabla

    def partido_con_mayor_asistencia(self):
        """
        Encuentra el partido con la mayor cantidad de personas que asistieron.

        Returns:
        - Partido: Objeto Partido con la mayor asistencia.
        """
        partidos = self.gestion_partidos.obtener_todos_partidos()
        partido_mayor_asistencia = max(partidos, key=lambda partido: partido.personas_asistieron)
        return partido_mayor_asistencia

    def partido_con_mas_boletos_vendidos(self):
        """
        Encuentra el partido con la mayor cantidad de boletos vendidos.

        Returns:
        - Partido: Objeto Partido con la mayor cantidad de boletos vendidos.
        """
        partidos = self.gestion_partidos.obtener_todos_partidos()
        partido_mas_boletos = max(partidos, key=lambda partido: partido.boletos_vendidos)
        return partido_mas_boletos

    def top_productos_mas_vendidos(self):
        """
        Encuentra los tres productos más vendidos en el restaurante.

        Returns:
        - list: Lista de productos (objetos Producto) ordenados por cantidad de ventas descendente.
        """
        productos = self.gestion_restaurante.productos
        productos_ordenados = sorted(productos, key=lambda producto: producto.ventas, reverse=True)
        return productos_ordenados[:3]

    def top_clientes_mas_activos(self):
        """
        Encuentra los tres clientes con más compras de entradas.

        Returns:
        - list: Lista de tuplas (cedula_cliente, cantidad_compras) ordenadas por cantidad de compras descendente.
        """
        clientes = defaultdict(int)
        for entrada in self.gestion_entradas.entradas:
            clientes[entrada.cliente.cedula] += 1
        
        clientes_ordenados = sorted(clientes.items(), key=lambda item: item[1], reverse=True)[:3]
        return clientes_ordenados

    def generar_graficos(self):
        """
        Genera gráficos y visualizaciones basadas en los indicadores calculados.
        """
        # Gráfico de promedio de gasto de cliente VIP
        labels = ['Clientes VIP', 'Clientes Normales']
        sizes = [self.gestion_entradas.num_clientes_vip(), self.gestion_entradas.num_clientes_normales()]
        colors = ['#ff9999','#66b3ff']
        explode = (0.1, 0)  # explode 1st slice

        plt.pie(sizes, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.title('Gráfico de clientes VIP')
        plt.show()

        # Otros gráficos y visualizaciones según los requerimientos adicionales

    def ejecutar_indicadores(self):
        """
        Ejecuta todos los indicadores de gestión e imprime los resultados por consola.
        """
        print(f"Promedio de gasto de cliente VIP: ${self.promedio_gasto_cliente_vip():.2f}")

        print("Tabla de asistencia a los partidos:")
        tabla = self.tabla_asistencia_partidos()
        for fila in tabla:
            print(fila)

        partido_mayor_asistencia = self.partido_con_mayor_asistencia()
        print(f"Partido con mayor asistencia: {partido_mayor_asistencia.nombre}")

        partido_mas_boletos = self.partido_con_mas_boletos_vendidos()
        print(f"Partido con más boletos vendidos: {partido_mas_boletos.nombre}")

        top_productos = self.top_productos_mas_vendidos()
        print("Top 3 productos más vendidos:")
        for producto in top_productos:
            print(f"{producto.nombre} - Ventas: {producto.ventas}")

        top_clientes = self.top_clientes_mas_activos()
        print("Top 3 clientes más activos:")
        for cliente, cantidad in top_clientes:
            print(f"Cédula: {cliente} - Boletos comprados: {cantidad}")

        self.generar_graficos()
