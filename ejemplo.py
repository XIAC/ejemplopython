class HijoProdigo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.dinero = 100
        self.dignidad = 50
        self.hambre = 0
        self.arrepentimiento = 0

    def mostrar_estado(self):
        print("\n--- ESTADO ACTUAL ---")
        print(f"Nombre: {self.nombre}")
        print(f"Dinero: {self.dinero}")
        print(f"Dignidad: {self.dignidad}")
        print(f"Hambre: {self.hambre}")
        print("----------------------\n")

    def gastar_en_fiestas(self):
        self.dinero -= 20
        self.dignidad -= 10
        self.hambre += 5
        print(f"{self.nombre} ha gastado dinero en fiestas.")

    def invertir(self):
        self.dinero -= 30
        self.dignidad += 5
        self.hambre += 2
        print(f"{self.nombre} ha invertido su dinero.")

    def ahorrar(self):
        self.dinero += 10
        self.dignidad += 2
        self.hambre -= 3
        print(f"{self.nombre} ha ahorrado dinero.")

    def verificar_estado(self):
        if self.dinero <= 0:
            print("Te has quedado sin dinero 💸")
        if self.dignidad <= 0:
            print("Has perdido toda tu dignidad 😞")
        if self.hambre >= 20:
            print("Tienes mucha hambre 🍞")


# Programa principal
nombre = input("¿Cuál es tu nombre? ")
hijo = HijoProdigo(nombre)

while True:
    hijo.mostrar_estado()
    
    print("¿Qué deseas hacer?")
    print("1. Gastar dinero en fiestas")
    print("2. Invertir")
    print("3. Ahorrar")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        hijo.gastar_en_fiestas()
    elif opcion == "2":
        hijo.invertir()
    elif opcion == "3":
        hijo.ahorrar()
    elif opcion == "4":
        print("Gracias por jugar 👋")
        break
    else:
        print("Opción no válida.")

    hijo.verificar_estado()