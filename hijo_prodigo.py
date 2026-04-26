class HijoProdigo:
    def __init__(self, nombre, id=None):
        self.id = id
        self.nombre = nombre
        self.dinero = 100
        self.dignidad = 50
        self.hambre = 0

    def gastar_en_fiestas(self):
        self.dinero -= 20
        self.dignidad -= 10
        self.hambre += 5

    def invertir(self):
        self.dinero -= 30
        self.dignidad += 5
        self.hambre += 2

    def ahorrar(self):
        self.dinero += 10
        self.dignidad += 2
        self.hambre -= 3

    def estado(self):
        return f"Dinero: {self.dinero} | Dignidad: {self.dignidad} | Hambre: {self.hambre}"
