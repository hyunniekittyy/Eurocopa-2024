
from equipo import Equipo
from estadio import Estadio
from partido import Partido

class GestionPartidosEstadios:
    """
        Inicializa la clase GestionPartidosEstadios con listas vacías para equipos, estadios y partidos.
    """
    def __init__(self):
        self.equipos = []
        self.estadios = []
        self.partidos = []

    def cargar_datos_iniciales(self):
        """
        Carga los datos iniciales de equipos, estadios y partidos desde fuentes externas.
        """
        self.cargar_equipos()
        self.cargar_estadios()
        self.cargar_partidos()

    def cargar_equipos(self):
        """
        Carga los datos de los equipos desde una URL y los almacena en la lista de equipos.
        """
        url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json"
        response = requests.get(url)
        equipos_data = response.json()
        for equipo in equipos_data:
            self.equipos.append(Equipo(equipo["nombre"], equipo["codigo_fifa"], equipo["grupo"]))

    def cargar_estadios(self):
        """
        Carga los datos de los estadios desde una URL y los almacena en la lista de estadios.
        """
        url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json"
        response = requests.get(url)
        estadios_data = response.json()
        for estadio in estadios_data:
            self.estadios.append(Estadio(estadio["nombre"], estadio["ubicacion"]))

    def cargar_partidos(self):
        """
        Carga los datos de los partidos desde una URL y los almacena en la lista de partidos.
        """
        url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json"
        response = requests.get(url)
        partidos_data = response.json()
        for partido in partidos_data:
            equipo_local = self.buscar_equipo_por_codigo(partido["equipo_local"])
            equipo_visitante = self.buscar_equipo_por_codigo(partido["equipo_visitante"])
            estadio = self.buscar_estadio_por_nombre(partido["estadio"])
            fecha_hora = partido["fecha_hora"]
            self.partidos.append(Partido(equipo_local, equipo_visitante, fecha_hora, estadio))
            

def buscar_equipo_por_codigo(self, codigo_fifa):
        """
        Busca un equipo por su código FIFA.

        Args:
        - codigo_fifa (str): El código FIFA del equipo.

        Returns:
        - Equipo: El equipo correspondiente al código FIFA proporcionado.
        - None: Si no se encuentra ningún equipo con el código proporcionado.
        """
        for equipo in self.equipos:
            if equipo.codigo_fifa == codigo_fifa:
                return equipo
        return None

def buscar_estadio_por_nombre(self, nombre):
        """
        Busca un estadio por su nombre.

        Args:
        - nombre (str): El nombre del estadio.

        Returns:
        - Estadio: El estadio correspondiente al nombre proporcionado.
        - None: Si no se encuentra ningún estadio con el nombre proporcionado.
        """
        for estadio in self.estadios:
            if estadio.nombre == nombre:
                return estadio
        return None

def buscar_partidos_por_pais(self, nombre_pais):
        """
        Busca partidos por el nombre del país.

        Args:
        - nombre_pais (str): El nombre del país del equipo local o visitante.

        Returns:
        - list: Lista de partidos en los que participa el equipo del país proporcionado.
        """
        partidos = []
        for partido in self.partidos:
            if partido.equipo_local.nombre == nombre_pais or partido.equipo_visitante.nombre == nombre_pais:
                partidos.append(partido)
        return partidos

def buscar_partidos_por_estadio(self, nombre_estadio):
        """
        Busca partidos por el nombre del estadio.

        Args:
        - nombre_estadio (str): El nombre del estadio.

        Returns:
        - list: Lista de partidos que se juegan en el estadio proporcionado.
        """
        partidos = []
        for partido in self.partidos:
            if partido.estadio.nombre == nombre_estadio:
                partidos.append(partido)
        return partidos

def buscar_partidos_por_fecha(self, fecha):
        """
        Busca partidos por la fecha.

        Args:
        - fecha (str): La fecha en formato 'AAAA-MM-DD'.

        Returns:
        - list: Lista de partidos que se juegan en la fecha proporcionada.
        """
        partidos = []
        for partido in self.partidos:
            if partido.fecha_hora.startswith(fecha):
                partidos.append(partido)
        return partidos