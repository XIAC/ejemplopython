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

    def gastar_todo(self):
        self.dinero = 0
        self.dignidad -= 20
        self.hambre += 50
        print("Has gastado todo en fiestas...")

    def invertir(self):
        self.dinero -= 30
        self.dinero += 20  # ganancia
        self.dignidad += 5
        self.hambre += 2
        print("Has invertido una parte de tu dinero.")

    def ahorrar(self):
        self.dinero += 10
        self.dignidad += 2
        self.hambre -= 3
        print("Has decidido ahorrar.")

    def trabajar(self):
        self.dinero += 25
        self.dignidad += 10
        self.hambre += 10
        print("Has trabajado duro para ganar dinero.")

    def reflexionar(self):
        if self.hambre > 40:
            self.arrepentimiento += 20
            print("El hambre te hace reflexionar sobre tus decisiones...")
        else:
            print("Aún no sientes necesidad de reflexionar.")

    def mostrar_estado(self):
        print("\n--- Estado del jugador ---")
        print("Nombre:", self.nombre)
        print("Dinero:", self.dinero)
        print("Dignidad:", self.dignidad)
        print("Hambre:", self.hambre)
        print("Arrepentimiento:", self.arrepentimiento)


# Programa principal
nombre = input("¿Cuál es tu nombre? ")
jugador = HijoProdigo(nombre)

print(f"\n¡Hola, {jugador.nombre}! Has recibido tu herencia.\n")

print("¿Qué deseas hacer?")
print("1. Gastar todo en fiestas")
print("2. Invertir")
print("3. Ahorrar")
print("4. Trabajar")
print("5. Reflexionar")

opcion = input("Elige una opción: ")

if opcion == "1":
    jugador.gastar_todo()
elif opcion == "2":
    jugador.invertir()
elif opcion == "3":
    jugador.ahorrar()
elif opcion == "4":
    jugador.trabajar()
elif opcion == "5":
    jugador.reflexionar()
else:
    print("Opción no válida.")

jugador.mostrar_estado()