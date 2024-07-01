from cliente import Cliente
from entrada import Entrada
import random

def generar_codigo_boleto(self):
    """
    Genera un código aleatorio de boleto compuesto por 10 caracteres alfanuméricos.

    Returns:
    - str: Código generado para el boleto.
    """
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10))

class GestionVentaEntradas:
    """
        Inicializa la gestión de venta de entradas.
    """
    def __init__(self):
        self.clientes = []
        self.entradas = []

    def agregar_cliente(self, nombre, cedula, edad):
        """
        Crea y agrega un nuevo cliente a la lista de clientes.

        Args:
        - nombre (str): Nombre del cliente.
        - cedula (str): Número de cédula del cliente.
        - edad (int): Edad del cliente.

        Returns:
        - Cliente: Objeto Cliente creado y agregado.
        """
        cliente = Cliente(nombre, cedula, edad)
        self.clientes.append(cliente)
        return cliente

    def calcular_costo_entrada(self, cliente, tipo):
        """
        Calcula el costo de una entrada basado en el tipo y condiciones del cliente.

        Args:
        - cliente (Cliente): Cliente para el cual calcular el costo de la entrada.
        - tipo (str): Tipo de entrada ("general" o "preferencial").

        Returns:
        - dict: Diccionario con los costos calculados.
          - "subtotal" (float): Costo base de la entrada.
          - "iva" (float): Valor del IVA aplicado.
          - "total" (float): Costo total a pagar.
        """
        base_cost = 35 if tipo.lower() == "general" else 75
        if self.es_cedula_vampiro(cliente.cedula):
            base_cost *= 0.5
        iva = base_cost * 0.16
        total_cost = base_cost + iva
        return {
            "subtotal": base_cost,
            "iva": iva,
            "total": total_cost
        }

    def es_cedula_vampiro(self, cedula):
        """
        Verifica si el número de cédula pertenece a un "cliente vampiro".

        Args:
        - cedula (str): Número de cédula a verificar.

        Returns:
        - bool: True si la cédula pertenece a un "cliente vampiro", False si no.
        """
        return False  # Implementar lógica para verificar si la cédula es un número vampiro

    def comprar_entrada(self, cliente, partido, tipo, asiento):
        """
        Procesa la compra de una entrada para un cliente dado.

        Args:
        - cliente (Cliente): Cliente que está comprando la entrada.
        - partido (Partido): Partido al cual se asistirá.
        - tipo (str): Tipo de entrada ("general" o "preferencial").
        - asiento (tuple): Tupla (fila, columna) del asiento seleccionado.

        Returns:
        - Entrada: Objeto Entrada creado y registrado.
        """
        costo = self.calcular_costo_entrada(cliente, tipo)
        entrada = Entrada(cliente, partido, tipo, asiento, costo)
        self.entradas.append(entrada)
        partido.ocupar_asiento(asiento)
        return entrada

#Parte para la gestión y asistencia de partidos:
    
class GestionAsistenciaPartidos:
    """
        Inicializa la gestión de asistencia a partidos.

        Args:
        - gestion_venta_entradas (GestionVentaEntradas): Instancia de GestionVentaEntradas para gestionar las entradas.
    """
    def __init__(self, gestion_venta_entradas):
        self.gestion_venta_entradas = gestion_venta_entradas

    def validar_boleto(self, codigo_boleto):
        """
        Valida un boleto utilizando su código.

        Args:
        - codigo_boleto (str): Código del boleto a validar.

        Returns:
        - bool: True si el boleto se validó con éxito y se registró la asistencia, False si no.
        """
        for entrada in self.gestion_venta_entradas.entradas:
            if entrada.codigo_boleto == codigo_boleto:
                if entrada.asistencia:
                    return False  # Boleto ya utilizado
                entrada.asistencia = True
                entrada.partido.registrar_asistencia()
                return True
        return False  # Boleto no encontrado

    def registrar_asistencia(self, codigo_boleto):
        """
        Registra la asistencia de un boleto válido utilizando su código.

        Args:
        - codigo_boleto (str): Código del boleto a registrar.

        Prints:
        - Mensaje indicando el resultado de la operación.
        """
        if self.validar_boleto(codigo_boleto):
            print("Asistencia registrada con éxito.")
        else:
            print("Boleto no válido o ya utilizado.")



   


