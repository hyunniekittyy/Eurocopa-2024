class Partido:
    """
    Clase para representar un partido.

    Atributos:
    equipo_local (Equipo): Equipo local.
    equipo_visitante (Equipo): Equipo visitante.
    fecha_hora (datetime): Fecha y hora del partido.
    estadio (Estadio): Estadio donde se juega el partido.
    """
    
    def __init__(self, equipo_local, equipo_visitante, fecha_hora, estadio):
        """
        Inicializa un partido con los datos proporcionados.

        Args:
        equipo_local (Equipo): Equipo local.
        equipo_visitante (Equipo): Equipo visitante.
        fecha_hora (datetime): Fecha y hora del partido.
        estadio (Estadio): Estadio donde se juega el partido.
        """
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.fecha_hora = fecha_hora
        self.estadio = estadio
        self.asientos_ocupados = set()
    

    def __repr__(self):
        return f'Partido({self.equipo_local}, {self.equipo_visitante}, {self.fecha_hora}, {self.estadio})'

    def asientos_disponibles(self):
        # Supongamos que el estadio tiene 100 asientos numerados del 1 al 100
        todos_asientos = set(range(1, 101))
        return todos_asientos - self.asientos_ocupados