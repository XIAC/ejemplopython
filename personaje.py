class HijoProdigo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.dinero = 100
        self.dignidad = 50
        self.hambre = 0
        self.arrepentimiento = 0

    def aplicar_cambios(self, cambios):
        for atributo, valor in cambios.items():
            setattr(self, atributo, getattr(self, atributo) + valor)

        self._limitar_valores()

    def _limitar_valores(self):
        self.dinero = max(self.dinero, 0)
        self.hambre = max(self.hambre, 0)
        self.dignidad = max(min(self.dignidad, 100), 0)

    def puede_realizar(self, costo):
        return self.dinero >= costo

    def estado(self):
        return (
            f"\n{self.nombre}\n"
            f"Dinero : {self.dinero}\n"
            f"Dignidad: {self.dignidad}\n"
            f"Hambre: {self.hambre}\n"
        )