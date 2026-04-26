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

    def gastar_en_fiestas(self):
        self.dinero -= 20
        self.dignidad -= 10
        self.hambre += 5
        print(f"{self.nombre} ha gastado dinero en fiestas. Dinero: {self.dinero}, Dignidad: {self.dignidad}, Hambre: {self.hambre}")

    def invertir(self):
        self.dinero -= 30
        self.dignidad += 5
        self.hambre += 2
        print(f"{self.nombre} ha invertido una parte de su dinero. Dinero: {self.dinero}, Dignidad: {self.dignidad}, Hambre: {self.hambre}")

    def ahorrar(self):
        self.dinero += 10
        self.dignidad += 2
        self.hambre -= 3
        print(f"{self.nombre} ha ahorrado. Dinero: {self.dinero}, Dignidad: {self.dignidad}, Hambre: {self.hambre}")
        
opcion2 = input("Ingrese el número de la opción que desea elegir: ")
if opcion2 == "1":    
    hijo = HijoProdigo("JOSE")
    hijo.gastar_en_fiestas()

######  Mi clase y funcion 

class Padre:
    def __init__(self, nombre):
        self.nombre = nombre
        self.paciencia = 100

    def aconsejar(self, hijo):
        hijo.dignidad += 10
        hijo.arrepentimiento += 5
        self.paciencia -= 10
        print(f"{self.nombre} aconseja a {hijo.nombre}. Dignidad del hijo: {hijo.dignidad}, Arrepentimiento: {hijo.arrepentimiento}")

def mostrar_estado(hijo):
    print(f"Estado de {hijo.nombre}: Dinero={hijo.dinero}, Dignidad={hijo.dignidad}, Hambre={hijo.hambre}, Arrepentimiento={hijo.arrepentimiento}")

opcion2 = input("Ingrese el número de la opción que desea elegir: ")

if opcion2 == "1":    
    hijo = HijoProdigo("JOSE")
    hijo.gastar_en_fiestas()
    mostrar_estado(hijo)

elif opcion2 == "2":
    hijo = HijoProdigo("JOSE")
    padre = Padre("PEDRO")
    padre.aconsejar(hijo)
    mostrar_estado(hijo)
