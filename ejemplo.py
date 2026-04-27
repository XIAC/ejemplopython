class HijoProdigo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.dinero = 100
        self.dignidad = 50
        self.hambre = 0
        self.arrepentimiento = 0

    def gastar_en_fiestas(self):
        self.dinero -= 20
        self.dignidad -= 10
        self.hambre += 5
        print(f"{self.nombre} ha gastado dinero en fiestas. Dinero: {self.dinero}, Dignidad: {self.dignidad}, Hambre: {self.hambre}")

    def invertir(self):
        self.dinero -= 30
        self.dignidad += 5
        self.hambre += 2
        print(f"{self.nombre} ha invertido una parte de su dinero. Dinero: {self.dinero}, Dignidad: {self.dignidad}, Hambre: {self.hambre}")

    def ahorrar(self):
        self.dinero += 10
        self.dignidad += 2
        self.hambre -= 3
        print(f"{self.nombre} ha ahorrado. Dinero: {self.dinero}, Dignidad: {self.dignidad}, Hambre: {self.hambre}")
    def trabajar(self):
        self.dinero += 15
        self.hambre += 10

    def reflexionar(self):
        if self.hambre > 40:
            self.arrepentimiento += 10

    def estado(self):
    print(f"Nom:{self.nombre} Din:{self.dinero} Dig:{self.dignidad} Ham:{self.hambre} Arr:{self.arrepentimiento}")
nombre = input("Nombre: ")
hijo = HijoProdigo(nombre)

print("El jugador ha recibido su herencia")
opcion = input("1.Fiestas 2.Invertir 3.Ahorrar: ")

if opcion == "1": hijo.gastar_en_fiestas()
elif opcion == "2": hijo.invertir()
elif opcion == "3": hijo.ahorrar()

hijo.estado()

while hijo.dinero > 0:
    print("Lejos de casa...")
    hijo.dinero -= 10; hijo.hambre += 5; hijo.reflexionar()

    if hijo.dinero <= 0: break

    if input("1.Trabajar 2.Nada: ") == "1": hijo.trabajar()

    hijo.estado()

print("Sin dinero"); hijo.estado()