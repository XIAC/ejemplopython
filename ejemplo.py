class HijoProdigo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.dinero = 100
        self.dignidad = 50
        self.hambre = 0

    def mostrar_estado(self):
        """Muestra las estadísticas actuales del jugador."""
        print(f"\n---  ESTADO DE {self.nombre.upper()} ---")
        print(f" Dinero: {self.dinero}")
        print(f" Dignidad: {self.dignidad}")
        print(f" Hambre: {self.hambre}")
        print("-" * 30)

    def gastar_en_fiestas(self):
        self.dinero -= 20
        self.dignidad -= 10
        self.hambre += 5
        print(f"\n {self.nombre} se fue de fiesta. ¡La noche estuvo loca!")

    def invertir(self):
        self.dinero -= 30
        self.dignidad += 5
        self.hambre += 2
        print(f"\n {self.nombre} invirtió en criptomonedas. ¡Mentalidad de tiburón!")

    def ahorrar(self):
        self.dinero += 10
        self.dignidad += 2
        self.hambre -= 3
        print(f"\n {self.nombre} guardó dinero bajo el colchón.")

# --- Lógica de ejecución ---
if __name__ == "__main__":
    user_name = input("Ingrese un nombre de jugador")
    hijo = HijoProdigo(user_name)

    while True:
        hijo.mostrar_estado()
        print("¿Qué desea hacer el jugador?")
        print("1. Gastar dinero en fiestas")
        print("2. Invertir una parte")
        print("3. Ahorrar")
        print("4. Salir del programa")

        opcion = input("\nSeleccione una opción (1-4): ")

        if opcion == "1":
            hijo.gastar_en_fiestas()
        elif opcion == "2":
            hijo.invertir()
        elif opcion == "3":
            hijo.ahorrar()
        elif opcion == "4":
            print("¡Cerrando el simulador!, gracias por jugar.")
            break
        else:
            print("Opción no válida, intente de nuevo.")