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
        print(
            f"{self.nombre} ha gastado dinero en fiestas. Dinero: {self.dinero}, Dignidad: {self.dignidad}, Hambre: {self.hambre}")

    def invertir(self):
        self.dinero -= 30
        self.dignidad += 5
        self.hambre += 2
        print(
            f"{self.nombre} ha invertido una parte de su dinero. Dinero: {self.dinero}, Dignidad: {self.dignidad}, Hambre: {self.hambre}")

    def ahorrar(self):
        self.dinero += 10
        self.dignidad += 2
        self.hambre -= 3
        print(f"{self.nombre} ha ahorrado. Dinero: {self.dinero}, Dignidad: {self.dignidad}, Hambre: {self.hambre}")

    def trabajar(self):
        self.dinero += 25
        self.dignidad += 5
        self.hambre += 10
        print(
            f"{self.nombre} ha decidido trabajar. Dinero: {self.dinero}, Dignidad: {self.dignidad}, Hambre: {self.hambre}")


print("--- Simulador del Hijo Pródigo ---")
nombre = input("¿Cuál es tu nombre? ")
hijo = HijoProdigo(nombre)

print(f"\n¡Hola, {nombre}! Bienvenido al simulador.")
print("1. Gastar en fiestas")
print("2. Invertir una parte")
print("3. Ahorrar")
print("4. Trabajar")

opcion2 = input("Ingrese el número de la opción que desea elegir: ")

if opcion2 == "1":
    hijo.gastar_en_fiestas()
elif opcion2 == "2":
    hijo.invertir()
elif opcion2 == "3":
    hijo.ahorrar()
elif opcion2 == "4":
    hijo.trabajar()
else:
    print("Opción no válida.")
