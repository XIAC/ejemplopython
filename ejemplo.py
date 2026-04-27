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
        self.mostrarEstado("Usted tiene:")

    def gastar_en_fiestas(self):
        self.dinero -= 20
        self.dignidad -= 10
        self.hambre += 5
        self.mostrarEstado("ha gastado dinero en fiestas.")

    def invertir(self):
        self.dinero -= 30
        self.dignidad += 5
        self.hambre += 2
        self.mostrarEstado("ha invertido una parte de su dinero.")

    def ahorrar(self):
        self.dinero += 10
        self.dignidad += 2
        self.hambre -= 3
        self.mostrarEstado("ha ahorrado.")
    def mostrarEstado(self, descripcion):
        print(f"{self.nombre} {descripcion} Dinero: {self.dinero} | Dignidad: {self.dignidad} | Hambre: {self.hambre} | Arrepentimiendo: {self.arrepentimiento}")

nombre = input("Ingrese su nombre: ")
hijo = HijoProdigo(nombre)
opcion = input("Ingrese el número de la opción que desea elegir: 1 (Gastar en fiestas) | 2 (Invertir) | 3 (Ahorrar): ")
if opcion == "1":
    hijo.gastar_en_fiestas()
elif opcion == "2":
    hijo.invertir()
elif opcion == "3":
    hijo.ahorrar()
else:
    print("Opcion invalida")
