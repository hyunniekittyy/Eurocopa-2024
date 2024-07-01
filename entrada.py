class Entrada:
    """
    Clase para representar una entrada.

    Atributos:
    cliente (Cliente): Cliente que compra la entrada.
    partido (Partido): Partido para el que se compra la entrada.
    tipo (str): Tipo de entrada (General o VIP).
    asiento (str): Asiento seleccionado.
    costo (float): Costo de la entrada.
    """
    
    def __init__(self, cliente, partido, tipo, asiento, costo):
        """
        Inicializa una entrada con los datos proporcionados.

        Args:
        cliente (Cliente): Cliente que compra la entrada.
        partido (Partido): Partido para el que se compra la entrada.
        tipo (str): Tipo de entrada.
        asiento (str): Asiento seleccionado.
        costo (float): Costo de la entrada.
        """
        self.cliente = cliente
        self.partido = partido
        self.tipo = tipo
        self.asiento = asiento
        self.costo = costo

    def __repr__(self):
        return f'Entrada({self.cliente}, {self.partido}, {self.tipo}, {self.asiento})'
