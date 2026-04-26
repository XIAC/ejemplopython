from hijo_prodigo import HijoProdigo
from menu import show_menu
from handlers import gastar_en_fiestas, invertir, ahorrar, ver_estado, ver_historial
from database import init_db, crear_jugador

init_db()

nombre = input("¿Cuál es tu nombre?: ")
jugador_id = crear_jugador(nombre)
jugador = HijoProdigo(nombre, id=jugador_id)

OPCIONES = {
    "0": gastar_en_fiestas,
    "1": invertir,
    "2": ahorrar,
    "3": ver_estado,
    "4": ver_historial,
}

while True:
    show_menu(jugador)
    opcion = input("Ingrese su opcion: ")

    if opcion == "5":
        print("¡Hasta luego!")
        break
    elif opcion in OPCIONES:
        OPCIONES[opcion](jugador)
    else:
        input("Opcion no valida. Presiona Enter para continuar ")
