class Cliente:
    """
    Clase para representar un cliente.

    Atributos:
    nombre (str): Nombre del cliente.
    cedula (str): Cédula del cliente.
    edad (int): Edad del cliente.
    """
    
    def __init__(self, nombre, cedula, edad):
        """
        Inicializa un cliente con los datos proporcionados.

        Args:
        nombre (str): Nombre del cliente.
        cedula (str): Cédula del cliente.
        edad (int): Edad del cliente.
        """
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
    
    
    def __repr__(self):
        return f'Cliente({self.nombre}, {self.cedula}, {self.edad})'
