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
def gastar(dinero, dignidad):
    dinero -= 15
    dignidad -= 5
    print("Gastaste dinero...")
    return dinero, dignidad

def trabajar(dinero, hambre):
    dinero += 20
    hambre += 10
    print("Trabajaste para ganar dinero...")
    return dinero, hambre

nombre = input("Ingresa tu nombre: ")
hijo = HijoProdigo(nombre)

while hijo.dinero > 0:
    print("\nSigues viviendo lejos de casa...")
    print(f"Dinero: {hijo.dinero}, Dignidad: {hijo.dignidad}, Hambre: {hijo.hambre}")
    
    print("\n¿Qué deseas hacer?")
    print("1. Gastar")
    print("2. Trabajar")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        hijo.dinero, hijo.dignidad = gastar(hijo.dinero, hijo.dignidad)
    elif opcion == "2":
        hijo.dinero, hijo.hambre = trabajar(hijo.dinero, hijo.hambre)
    else:
        print("Opción inválida")

    if hijo.hambre > 50:
        print("Tienes demasiada hambre...")
        hijo.dinero -= 10

print("\nTe has quedado sin dinero... Fin del juego.")