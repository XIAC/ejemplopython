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
    
import random

class HijoProdigo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.dinero = 100
        self.dignidad = 50
        self.hambre = 0
        self.arrepentimiento = 0
        self.volver = False

    def mostrar_estado(self):
        print(f"\n💰 Dinero: {self.dinero} | 🧍 Dignidad: {self.dignidad} | 🍞 Hambre: {self.hambre} | 😔 Arrepentimiento: {self.arrepentimiento}")

    def aplicar_consecuencias(self, dinero, hambre, dignidad, arrepentimiento):
        self.dinero = max(0, self.dinero - dinero)
        self.hambre += hambre
        self.dignidad -= dignidad
        self.arrepentimiento += arrepentimiento

        # 🔥 CONDICIÓN AUTOMÁTICA DE REGRESO
        if self.dinero <= 0 or self.dignidad <= 10 or self.hambre >= 50:
            self.volver = True

    def evento(self, lista_eventos, consecuencias):
        print("\n" + random.choice(lista_eventos))
        self.aplicar_consecuencias(*consecuencias)
        self.mostrar_estado()


# ===== INICIO =====
print("=== EL HIJO PRÓDIGO (JUEGO) ===")
nombre = input("Nombre del hijo pródigo: ")
hijo = HijoProdigo(nombre)

print(f"\n{hijo.nombre} recibe su herencia con {hijo.dinero} monedas...")

# ===== EVENTOS =====

fiesta = [
    "Vas a un banquete... y terminas pagando hasta la mesa.",
    "Contratas músicos... pero el único que baila eres tú.",
    "Compras vino... terminas pagando todo sin beber nada."
]

amigos = [
    "Tus amigos dicen 'somos hermanos'... hasta que se acaba tu dinero.",
    "Compras túnicas... y luego nadie te recuerda.",
    "Prestaste dinero... y cuando les cobras te dicen que Dios te lo pague."
]

trabajo = [
    "Cuidas cerdos... pero ellos parecen tus jefes.",
    "Te pagan con pan duro y bendiciones.",
    "Llegas tarde... y el trabajo desaparece."
]

ahorro = [
    "Guardas tu dinero tan bien... que ni tú sabes dónde está.",
    "Escondes monedas... pero alguien usa el escondite.",
    "Intentas no gastar... pero el pan te gana."
]

reflexion = [
    "Te pones a pensar... pero tu estómago interrumpe.",
    "Recuerdas tu casa... y te da más hambre.",
    "Miras al horizonte dramáticamente..."
]

# ===== JUEGO PRINCIPAL =====

while not hijo.volver:
    print("\n¿Qué deseas hacer?")
    print("1. Ir de fiesta")
    print("2. Gastar con amigos")
    print("3. Trabajar")
    print("4. Ahorrar")
    print("5. Reflexionar")

    opcion = input("Elige: ")

    if opcion == "1":
        hijo.evento(fiesta, (30, 15, 10, 15))

    elif opcion == "2":
        hijo.evento(amigos, (25, 10, 10, 10))

    elif opcion == "3":
        hijo.evento(trabajo, (10, 5, 5, 5))

    elif opcion == "4":
        hijo.evento(ahorro, (5, 5, 2, 3))

    elif opcion == "5":
        hijo.evento(reflexion, (0, 2, 1, 10))

    else:
        print("Opción inválida.")

# ===== REGRESO AUTOMÁTICO =====

print("\n--- HAS TOCADO FONDO ---")
print(f"{hijo.nombre} se queda sin fuerzas, sin recursos o sin dignidad...")
print("Entonces piensa:")
print("'En la casa de mi padre hasta los jornaleros tienen pan...'")
print("Se arrepiente y decide volver.")

# ===== HERMANO =====

print("\n--- HERMANO MAYOR ---")
print("¿Qué dices como hermano?")
print("1. 'Yo trabajé siempre y nunca me celebraste'")
print("2. 'Él gastó todo y ahora lo recibes'")
print("3. 'No es justo que vuelva así'")

op = input("Elige: ")

if op == "1":
    respuesta = "Hijo, tú siempre has estado conmigo, y todo lo mío es tuyo."
elif op == "2":
    respuesta = "Hijo, no celebramos su error, celebramos que ha vuelto."
elif op == "3":
    respuesta = "Hijo, estaba perdido y ahora ha sido hallado."
else:
    respuesta = "Hijo, debemos alegrarnos porque tu hermano ha vuelto."

print("\nPadre:")
print(f'"{respuesta}"')

print("\nEl hermano reflexiona...")
print("Todos entran a casa y celebran.")

print("\n🎉 FIN 🎉")