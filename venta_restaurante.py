class VentaRestaurante:
    def __init__(self, cliente, productos):
        self.cliente = cliente
        self.productos = productos

    def __repr__(self):
        return f'VentaRestaurante({self.cliente}, {self.productos})'
