from cliente import Cliente
from producto import Producto

url_estadios_restaurantes = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json"

# Función para cargar datos desde una URL
def cargar_datos(url):
    """
    Carga datos desde una URL y retorna el contenido en formato JSON.

    Args:
        url (str): URL desde la cual se cargarán los datos.

    Returns:
        dict: Datos cargados en formato JSON, o None si hay un error en la carga.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error al cargar los datos")
        return None

# Cargar datos de los estadios y restaurantes
datos_estadios_restaurantes = cargar_datos(url_estadios_restaurantes)

# Listas para almacenar los datos
restaurantes = []
productos = []

if datos_estadios_restaurantes:
    for estadio in datos_estadios_restaurantes:
        for restaurante in estadio.get("restaurantes", []):
            restaurantes.append(restaurante)
            for producto in restaurante.get("productos", []):
                productos.append(producto)

# Imprimir los datos para verificar

class GestionRestaurante:
    """
        Inicializa la clase GestionRestaurante con una lista vacía de productos.
    """
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, clasificacion, tipo, precio):
        """
        Agrega un producto a la lista de productos.

        Args:
            nombre (str): Nombre del producto.
            clasificacion (str): Clasificación del producto.
            tipo (str): Tipo del producto.
            precio (float): Precio del producto.
        """
        producto = Producto(nombre, clasificacion, tipo, precio)
        self.productos.append(producto)
        print(f"Producto '{nombre}' agregado correctamente.")

    def guardar_productos(self, filename="productos.txt"):
        """
        Guarda los productos en un archivo.

        Args:
            filename (str): Nombre del archivo donde se guardarán los productos. Por defecto es "productos.txt".
        """
        with open(filename, 'w') as file:
            for producto in self.productos:
                file.write(f"{producto.nombre},{producto.clasificacion},{producto.tipo},{producto.precio}\n")

    def cargar_productos_desde_archivo(self, filename="productos.txt"):
        """
        Carga los productos desde un archivo.

        Args:
            filename (str): Nombre del archivo desde el cual se cargarán los productos. Por defecto es "productos.txt".
        """
        try:
            with open(filename, 'r') as file:
                for line in file:
                    nombre, clasificacion, tipo, precio = line.strip().split(',')
                    self.agregar_producto(nombre, clasificacion, tipo, float(precio))
        except FileNotFoundError:
            print(f"No se encontró el archivo {filename}. Se creará uno nuevo al guardar productos.")

    def buscar_por_nombre(self, nombre):
        """
        Busca productos por nombre.

        Args:
            nombre (str): Nombre del producto a buscar.

        Returns:
            list: Lista de productos que coinciden con el nombre proporcionado.
        """
        resultados = [producto for producto in self.productos if nombre.lower() in producto.nombre.lower()]
        return resultados

    def buscar_por_clasificacion(self, clasificacion):
        """
        Busca productos por clasificación.

        Args:
            clasificacion (str): Clasificación del producto a buscar.

        Returns:
            list: Lista de productos que coinciden con la clasificación proporcionada.
        """
        resultados = [producto for producto in self.productos if producto.clasificacion.lower() == clasificacion.lower()]
        return resultados

    def buscar_por_tipo(self, tipo):
        """
        Busca productos por tipo.

        Args:
            tipo (str): Tipo del producto a buscar.

        Returns:
            list: Lista de productos que coinciden con el tipo proporcionado.
        """
        resultados = [producto for producto in self.productos if producto.tipo.lower() == tipo.lower()]
        return resultados

    def buscar_por_rango_de_precio(self, precio_min, precio_max):
        """
        Busca productos por rango de precio.

        Args:
            precio_min (float): Precio mínimo del rango.
            precio_max (float): Precio máximo del rango.

        Returns:
            list: Lista de productos que se encuentran dentro del rango de precios proporcionado.
        """
        resultados = [producto for producto in self.productos if precio_min <= producto.precio <= precio_max]
        return resultados

# Crear una instancia de GestionRestaurante y cargar los datos del JSON

class GestionVentaRestaurantes:
    """
        Inicializa la clase GestionVentaRestaurantes con una instancia de GestionRestaurante y una lista vacía de ventas.

        Args:
            gestion_restaurante (GestionRestaurante): Instancia de la clase GestionRestaurante.
    """
    def __init__(self, gestion_restaurante):
        self.gestion_restaurante = gestion_restaurante
        self.ventas = []

    def validar_cliente_vip(self, cedula):
        """
        Valida si un cliente es VIP.

        Args:
            cedula (str): Cédula del cliente.

        Returns:
            bool: True si el cliente es VIP, False en caso contrario.
        """
        # Implementar la lógica de validación del cliente VIP
        pass

    def calcular_costo_productos(self, cliente, productos):
        """
        Calcula el costo total de los productos comprados por un cliente, aplicando descuentos e IVA.

        Args:
            cliente (Cliente): Cliente que realiza la compra.
            productos (list): Lista de productos comprados.

        Returns:
            float: Costo total de los productos comprados.
        """
        total = sum(producto.precio for producto in productos)
        discount = 0.1 if self.validar_cliente_vip(cliente.cedula) else 0
        iva = 0.12
        costo = total * (1 - discount) * (1 + iva)
        return costo

    def registrar_venta_restaurante(self, cliente, productos):
        """
        Registra una venta en el restaurante.

        Args:
            cliente (Cliente): Cliente que realiza la compra.
            productos (list): Lista de productos comprados.

        Returns:
            dict: Diccionario con los detalles de la venta.
        """
        costo = self.calcular_costo_productos(cliente, productos)
        venta = {
            'cliente': cliente,
            'productos': productos,
            'costo': costo
        }
        self.ventas.append(venta)
        return venta

    def guardar_ventas(self, filename="ventas_restaurante.txt"):
        """
        Guarda las ventas en un archivo.

        Args:
            filename (str): Nombre del archivo donde se guardarán las ventas. Por defecto es "ventas_restaurante.txt".
        """
        with open(filename, 'w') as file:
            for venta in self.ventas:
                cliente = venta['cliente']
                productos = venta['productos']
                costo = venta['costo']
                file.write(f"{cliente.cedula},{cliente.nombre},{costo}")
                for producto in productos:
                    file.write(f",{producto.nombre},{producto.precio}")
                file.write("\n")

    def cargar_ventas_desde_archivo(self, filename="ventas_restaurante.txt"):
        """
        Carga las ventas desde un archivo.

        Args:
            filename (str): Nombre del archivo desde el cual se cargarán las ventas. Por defecto es "ventas_restaurante.txt".
        """
        try:
            with open(filename, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    cedula, nombre, costo = data[:3]
                    cliente = Cliente(cedula=cedula, nombre=nombre)
                    productos = []
                    for i in range(3, len(data), 2):
                        nombre_producto, precio = data[i], float(data[i+1])
                        producto = next((p for p in self.gestion_restaurante.productos if p.nombre == nombre_producto and p.precio == precio), None)
                        if producto:
                            productos.append(producto)
                    self.registrar_venta_restaurante(cliente, productos)
        except FileNotFoundError:
            print(f"No se encontró el archivo {filename}. Se creará uno nuevo al guardar ventas.")






