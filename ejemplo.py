# Historia del Hijo Pródigo en Python
# Uso de variables, condicionales, funciones, bucles y POO

# ==========================
# Clase (Programación Orientada a Objetos)
# ==========================
class HijoProdigo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.dinero = 100
        self.dignidad = 50
        self.hambre = 0

    # Mostrar estado actual del jugador
    def mostrar_estado(self):
        print("\n--- Estado actual ---")
        print(f"Jugador: {self.nombre}")
        print(f"Dinero: {self.dinero}")
        print(f"Dignidad: {self.dignidad}")
        print(f"Hambre: {self.hambre}")
        print("----------------------\n")

    # Opción 1: Gastar dinero en fiestas
    def fiestas(self):
        print("\nHas gastado todo en fiestas...")
        self.dinero -= 80
        self.dignidad -= 20
        self.hambre += 30

    # Opción 2: Invertir una parte
    def invertir(self):
        print("\nHas invertido una parte de tu herencia...")
        self.dinero += 50
        self.dignidad += 10
        self.hambre += 5

    # Opción 3: Ahorrar
    def ahorrar(self):
        print("\nHas decidido ahorrar tu dinero...")
        self.dinero += 10
        self.dignidad += 5
        self.hambre += 2

    # Regresar al padre
    def regresar_a_casa(self):
        print("\nArrepentido, decides volver a casa.")
        print("Tu padre te recibe con amor y organiza una gran fiesta.")
        self.dignidad = 100
        self.hambre = 0

# ==========================
# Función principal
# ==========================
def main():
    # Pedir nombre del jugador
    nombre = input("¿Cuál es tu nombre? ")

    # Crear objeto
    jugador = HijoProdigo(nombre)

    # Mensaje inicial
    print(f"\nHola {nombre}, bienvenido a la historia del Hijo Pródigo.")
    print("Has recibido tu herencia.")

    # Bucle principal
    while True:
        jugador.mostrar_estado()

        # Menú de opciones
        print("¿Qué deseas hacer?")
        print("1. Gastarlo todo en fiestas")
        print("2. Invertir una parte")
        print("3. Ahorrar")
        print("4. Regresar a casa")
        print("5. Salir")

        opcion = input("Ingrese el número de la opción: ")

        # Condicionales
        if opcion == "1":
            jugador.fiestas()
        elif opcion == "2":
            jugador.invertir()
        elif opcion == "3":
            jugador.ahorrar()
        elif opcion == "4":
            jugador.regresar_a_casa()
            jugador.mostrar_estado()
            print("Fin de la historia. Has sido perdonado.")
            break
        elif opcion == "5":
            print("Gracias por jugar.")
            break
        else:
            print("Opción no válida.")

        # Verificar si se quedó sin dinero
        if jugador.dinero <= 0:
            print("\nTe has quedado sin dinero.")
            print("Terminas cuidando cerdos y pasando hambre.")
            jugador.hambre += 50
            jugador.mostrar_estado()

            decision = input("¿Deseas regresar a casa? (si/no): ").lower()

            if decision == "si":
                jugador.regresar_a_casa()
                jugador.mostrar_estado()
                print("Fin de la historia. Tu padre te ha perdonado.")
                break

# Ejecutar programa
main()