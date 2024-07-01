class Equipo:
    """
    Clase para representar un equipo.

    Atributos:
    nombre_pais (str): Nombre del país.
    codigo_fifa (str): Código FIFA del país.
    grupo (str): Grupo en el que se encuentra el equipo.
    """

    def __init__(self, nombre, codigo_fifa, grupo):
        """
        Inicializa un equipo con los datos proporcionados.

        Args:
        nombre_pais (str): Nombre del país.
        codigo_fifa (str): Código FIFA del país.
        grupo (str): Grupo en el que se encuentra el equipo.
        """ 
        self.nombre = nombre
        self.codigo_fifa = codigo_fifa
        self.grupo = grupo
    
    def __repr__(self):
        return f'Equipo({self.nombre}, {self.codigo_fifa}, {self.grupo})'

