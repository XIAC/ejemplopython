import random

class HijoProdigo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.dinero = 100
        self.dignidad = 50
        self.hambre = 0
        self.arrepentimiento = 0
        self.vivo = True

    def mostrar_estado(self):
        print(f"\n--- Estado de {self.nombre} ---")
        print(f"Dinero: {self.dinero}")
        print(f"Dignidad: {self.dignidad}")
        print(f"Hambre: {self.hambre}")
        print(f"Arrepentimiento: {self.arrepentimiento}")

    def ajustar_valores(self):
        if self.dinero < 0:
            self.dinero = 0
        if self.hambre < 0:
            self.hambre = 0
        if self.dignidad < 0:
            self.dignidad = 0

    def verificar_estado(self):
        if self.hambre >= 100:
            print("\n💀 Has perdido: moriste de hambre.")
            self.vivo = False
        elif self.dignidad <= 0:
            print("\n💀 Has perdido: perdiste toda tu dignidad.")
            self.vivo = False
        elif self.arrepentimiento >= 100:
            print("\n✨ Te has arrepentido completamente y decides volver a casa.")
            self.vivo = False

    def gastar_en_fiestas(self):
        print("\n🎉 Te vas de fiesta...")
        self.dinero -= 20
        self.dignidad -= 10
        self.hambre += 5
        self.arrepentimiento += 15

    def invertir(self):
        print("\n📈 Decides invertir tu dinero...")
        resultado = random.choice(["ganancia", "perdida"])

        if resultado == "ganancia":
            print("💰 ¡Tu inversión fue exitosa!")
            self.dinero += 40
            self.dignidad += 10
        else:
            print("📉 La inversión falló...")
            self.dinero -= 30
            self.dignidad -= 5

        self.hambre += 3
        self.arrepentimiento += 5

    def ahorrar(self):
        print("\n🏦 Decides ahorrar...")
        self.dinero += 10
        self.dignidad += 5
        self.hambre += 2
        self.arrepentimiento -= 2

    def evento_aleatorio(self):
        evento = random.choice(["robo", "regalo", "nada"])

        if evento == "robo":
            print("\n⚠️ ¡Te robaron dinero!")
            self.dinero -= 15
        elif evento == "regalo":
            print("\n🎁 Recibes un regalo inesperado.")
            self.dinero += 20


# PROGRAMA PRINCIPAL

nombre = input("¿Cuál es tu nombre? ")
hijo = HijoProdigo(nombre)

print(f"\nBienvenido {nombre}, has recibido tu herencia...")

while hijo.vivo:
    hijo.mostrar_estado()

    print("\n¿Qué deseas hacer?")
    print("1. Gastar en fiestas")
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
        print("\n👋 Has decidido abandonar el juego.")
        break
    else:
        print("❌ Opción no válida")
        continue

    hijo.evento_aleatorio()
    hijo.ajustar_valores()
    hijo.verificar_estado()

print("\n--- Fin del juego ---")