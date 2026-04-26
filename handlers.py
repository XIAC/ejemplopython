from prettytable import PrettyTable
from database import registrar_accion, obtener_historial


def gastar_en_fiestas(jugador):
    jugador.gastar_en_fiestas()
    registrar_accion(jugador.id, "Gastar en fiestas", jugador)
    print(f"\n{jugador.nombre} ha gastado dinero en fiestas.")
    print(jugador.estado())
    input("\nPresiona Enter para continuar ")


def invertir(jugador):
    jugador.invertir()
    registrar_accion(jugador.id, "Invertir", jugador)
    print(f"\n{jugador.nombre} ha invertido una parte de su dinero.")
    print(jugador.estado())
    input("\nPresiona Enter para continuar ")


def ahorrar(jugador):
    jugador.ahorrar()
    registrar_accion(jugador.id, "Ahorrar", jugador)
    print(f"\n{jugador.nombre} ha ahorrado.")
    print(jugador.estado())
    input("\nPresiona Enter para continuar ")


def ver_estado(jugador):
    print(f"\nEstado actual de {jugador.nombre}:")
    print(jugador.estado())
    input("\nPresiona Enter para continuar ")


def ver_historial(jugador):
    filas = obtener_historial(jugador.id)
    if not filas:
        input("\nAun no hay acciones registradas. Presiona Enter para continuar ")
        return

    tabla = PrettyTable(["#", "Accion", "Dinero", "Dignidad", "Hambre", "Fecha"])
    for i, fila in enumerate(filas, 1):
        tabla.add_row([i, fila["accion"], fila["dinero"], fila["dignidad"],
                       fila["hambre"], fila["fecha"]])

    print(f"\nHistorial de {jugador.nombre}:")
    print(tabla)
    input("\nPresiona Enter para continuar ")
