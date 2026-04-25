class HijoProdigo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.dinero = 100
        self.dignidad = 50
        self.hambre = 0
        
    def gastar_todo(self):
        self.dinero = 0
        self.dignidad -= 20
        self.hambre += 50
        print(f"\n¡Derroche total! {self.nombre} se quedó sin dinero.")
        print(f"Dignidad: {self.dignidad} | Hambre: {self.hambre}")

    def invertir_o_trabajar(self):
        self.dinero += 20
        self.dignidad += 5 
        self.hambre += 10
        print(f"\n{self.nombre} trabajó e invirtió con éxito.")
        print(f"Ganaste 20 monedas. (Dignidad +5, Hambre +10)")
# --- INICIO ---
nombre_jugador = input("Ingrese el nombre del jugador: ")
hijo = HijoProdigo(nombre_jugador)

print(f"\nBienvenido {hijo.nombre}. Recibes tu herencia de 100 monedas.")

while hijo.dinero > 0:
    print(f"\n--- ESTADO: Dinero {hijo.dinero} | Dignidad {hijo.dignidad} | Hambre {hijo.hambre} ---")
    print("1. Gastarlo todo en fiestas")
    print("2. Invertir / Trabajar")
    print("3. Ahorrar")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        hijo.gastar_todo()
    elif opcion == "2":
        hijo.invertir_o_trabajar()
    elif opcion == "3":
        print("Decidiste ahorrar.")
    
    # REQUISITO: El costo de vida que intenta frenar el bucle
    print("“Sigues viviendo lejos de casa…”")
    hijo.dinero -= 10 

print(f"\nEl dinero de {hijo.nombre} llegó a 0. Regresas con tu padre.")