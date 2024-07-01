class Estadio:
    """
    Clase para representar un estadio.

    Atributos:
    nombre (str): Nombre del estadio.
    ubicacion (str): Ubicación del estadio."""
    
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.asientos = [['💺' for _ in range(15)] for _ in range(10)]
        self.asientos_ocupados = set()
    """
        Inicializa un estadio con los datos proporcionados.

        Args:
        nombre (str): Nombre del estadio.
        ubicacion (str): Ubicación del estadio.
        """

    def __repr__(self):
        return f'Estadio({self.nombre}, {self.ubicacion})'

#Mapa de asientos:

    def mostrar_mapa(self):
        """
        Muestra el mapa del estadio con los asientos disponibles y ocupados.
        """
        print("Mapa del Estadio:")
        print("Campo")
        print("---------------------------------------------")
        print("  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O")
        print("---------------------------------------------")
        for i in range(10):
            print(f"{i+1} " + " ".join(self.asientos[i]))
        print("---------------------------------------------")

    def seleccionar_asiento(self, fila, columna):
        """
        Intenta seleccionar un asiento específico en el estadio.

        Args:
        - fila (int): Número de fila del asiento (1-10).
        - columna (str): Letra de la columna del asiento (A-O).

        Returns:
        - tuple: (bool, str). 
          - bool: True si el asiento se seleccionó correctamente, False si no.
          - str: Mensaje indicando el resultado de la operación.
        """
        if fila < 1 or fila > 10 or columna not in "ABCDEFGHIJKLMNO":
            return False, "Fila o columna inválida."

        indice_fila = fila - 1
        indice_columna = ord(columna) - ord('A')

        if self.asientos[indice_fila][indice_columna] == '💺':
            self.asientos[indice_fila][indice_columna] = 'X'
            self.asientos_ocupados.add((fila, columna))
            return True, f"Asiento {fila}{columna} seleccionado correctamente."
        else:
            return False, f"Lo siento, el asiento {fila}{columna} está ocupado. Por favor, seleccione otro."

    def asiento_esta_ocupado(self, fila, columna):
        """
        Verifica si un asiento específico está ocupado.

        Args:
        - fila (int): Número de fila del asiento (1-10).
        - columna (str): Letra de la columna del asiento (A-O).

        Returns:
        - bool: True si el asiento está ocupado, False si no.
        """
        return (fila, columna) in self.asientos_ocupados

estadio = Estadio()
estadio.seleccionar_asiento(3, 'H')
estadio.seleccionar_asiento(1, 'A')

estadio.mostrar_mapa()
