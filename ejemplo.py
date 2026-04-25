import random

class HijoProdigo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.dinero = 100
        self.dignidad = 50
        self.hambre = 0
        self.arrepentimiento = 0

    def estado(self):
        print(f"\nEstado actual de {self.nombre}:")
        print(f"Dinero: {self.dinero}, Dignidad: {self.dignidad}, Hambre: {self.hambre}")

    def evento_aleatorio(self):
        evento = random.choice(["dinero", "robo", "ayuda"])
        
        if evento == "dinero":
            self.dinero += 15
            print("💰 Encontraste dinero en la calle (+15)")
        elif evento == "robo":
            self.dinero -= 10
            print("🚨 Te robaron (-10)")
        elif evento == "ayuda":
            self.dignidad += 5
            print("🙏 Alguien te ayudó (+5 dignidad)")

    def gastar_en_fiestas(self):
        self.dinero -= 20
        self.dignidad -= 10
        self.hambre += 5
        self.evento_aleatorio()

    def invertir(self):
        self.dinero -= 30
        self.dignidad += 5
        self.hambre += 2
        self.evento_aleatorio()

    def ahorrar(self):
        self.dinero += 10
        self.dignidad += 2
        self.hambre -= 3
        self.evento_aleatorio()

    def verificar_estado(self):
        if self.dinero <= 0:
            print("💀 Te quedaste sin dinero. Fin del juego.")
            return False
        if self.hambre >= 20:
            print("🍞 Moriste de hambre. Fin del juego.")
            return False
        return True


# MAIN
nombre = input("Ingresa tu nombre: ")
hijo = HijoProdigo(nombre)

while True:
    print("\n1. Fiestas\n2. Invertir\n3. Ahorrar\n4. Ver estado\n5. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        hijo.gastar_en_fiestas()
    elif opcion == "2":
        hijo.invertir()
    elif opcion == "3":
        hijo.ahorrar()
    elif opcion == "4":
        hijo.estado()
    elif opcion == "5":
        print("👋 Saliendo del juego...")
        break
    else:
        print("❌ Opción inválida")

    if not hijo.verificar_estado():
        break