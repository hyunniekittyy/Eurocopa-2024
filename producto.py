class Producto:
    """
    Clase para representar un producto del restaurante.

    Atributos:
    nombre (str): Nombre del producto.
    clasificacion (str): Clasificación del producto (alimento o bebida).
    precio (float): Precio del producto con IVA incluido.
    alcoholica (bool, optional): Indica si la bebida es alcohólica.
    empaque (bool, optional): Indica si el alimento es de empaque.
    """
    
    def __init__(self, nombre, clasificacion, precio, detalle= None): #Revisa esto aquí
        """
        Inicializa un producto con los datos proporcionados.

        Args:
        nombre (str): Nombre del producto.
        clasificacion (str): Clasificación del producto.
        precio (float): Precio del producto.
        alcoholica (bool, optional): Indica si la bebida es alcohólica.
        empaque (bool, optional): Indica si el alimento es de empaque.
        """
        self.nombre = nombre
        self.clasificacion = clasificacion
        self.precio = precio
        self.detalle = detalle

    def __repr__(self):
        return f'Producto({self.nombre}, {self.clasificacion}, {self.precio}, {self.detalle})'
