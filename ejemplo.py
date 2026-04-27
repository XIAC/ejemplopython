# nombre = input("¿Cuál es tu nombre? ")
# print("¡Hola, " + nombre + "! Bienvenido al mundo de la programación en Python.")
# print(f"Bienvenido al mundo de la programación en Python, {nombre}!")
# dinero = 100
# dignidad = 50
# hambre = 0
# print("El jugador ha recibido su herencia.")

# print("Que desea hacer el jugador?")
# print("1. Gastar dinero en fiestas")
# print("2. Invertir una parte")
# print("3. Ahorrar")

# opcion = input("Ingrese el número de la opción que desea elegir: ")
# if opcion == "1":
#     dinero -= 20
#     dignidad -= 10
#     hambre += 5
#     print("El jugador ha gastado dinero en fiestas. Dinero:", dinero, "Dignidad:", dignidad, "Hambre:", hambre)
# elif opcion == "2":
#     dinero -= 30
#     dignidad += 5
#     hambre += 2
#     print("El jugador ha invertido una parte de su dinero. Dinero:", dinero, "Dignidad:", dignidad, "Hambre:", hambre)
# elif opcion == "3":
#     dinero += 10
#     dignidad += 2
#     hambre -= 3
#     print("El jugador ha ahorrado. Dinero:", dinero, "Dignidad:", dignidad, "Hambre:", hambre)
# else:
#     print("Opción no válida.")

class HijoProdigo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.dinero = 100
        self.dignidad = 50
        self.hambre = 0
        self.arrepentimiento = 0

    def gastar_en_fiestas(self):
        self.remove_cash(20)
        self.remove_status(10)
        self.add_hungry(5)

        print(
            f"{self.nombre} ha gastado dinero en fiestas. Dinero: {self.dinero}, Dignidad: {self.dignidad}, Hambre: {self.hambre}")

    def invertir(self):
        self.remove_cash(30)
        self.add_status(5)
        self.add_hungry(2)

        print(
            f"{self.nombre} ha invertido una parte de su dinero. Dinero: {self.dinero}, Dignidad: {self.dignidad}, Hambre: {self.hambre}")

    def ahorrar(self):
        self.add_cash(10)
        self.add_status(2)
        self.remove_hungry(3)

        print(f"{self.nombre} ha ahorrado. Dinero: {self.dinero}, Dignidad: {self.dignidad}, Hambre: {self.hambre}")

    def add_cash(self, amount):
        self.dinero += amount

    def remove_cash(self, amount):
        if self.dinero < amount:
            print(f"El monto {amount} es mayor a la cantidad de dinero disponible {self.dinero}, estas endeudado")

        self.dinero -= amount

    def add_hungry(self, amount):
        self.hambre += amount

    def remove_hungry(self, amount):
        self.hambre -= amount

    def add_status(self, amount):
        self.dignidad += amount

    def remove_status(self, amount):
        self.dignidad -= amount


opcion2 = input("Ingrese el número de la opción que desea elegir: ")
if opcion2 == "1":
    hijo = HijoProdigo("AA")
    hijo.gastar_en_fiestas()
