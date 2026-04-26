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

    def mostrar_estado(self):
        print(f"\nEstado de {self.nombre}:")
        print(f"Dinero: {self.dinero}")
        print(f"Dignidad: {self.dignidad}")
        print(f"Hambre: {self.hambre}")
        print(f"Arrepentimiento: {self.arrepentimiento}")

    def gastar_en_fiestas(self):
        self.dinero -= 20
        self.dignidad -= 10
        self.hambre += 5
        print(f"{self.nombre} gastó dinero en fiestas.")

    def invertir(self):
        self.dinero -= 30
        self.dignidad += 5
        self.hambre += 2
        print(f"{self.nombre} invirtió su dinero.")

    def ahorrar(self):
        self.dinero += 10
        self.dignidad += 2
        self.hambre -= 3
        print(f"{self.nombre} ahorró dinero.")


# Crear personaje
nombre = input("Ingrese el nombre del hijo pródigo: ")
hijo = HijoProdigo(nombre)

# Menú
while True:
    print("\n--- MENÚ ---")
    print("1. Gastar en fiestas")
    print("2. Invertir")
    print("3. Ahorrar")
    print("4. Ver estado")
    print("5. Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        hijo.gastar_en_fiestas()
    elif opcion == "2":
        hijo.invertir()
    elif opcion == "3":
        hijo.ahorrar()
    elif opcion == "4":
        hijo.mostrar_estado()
    elif opcion == "5":
        print("Fin del juego.")
        break
    else:
        print("Opción inválida.")

    hijo.mostrar_estado()