from personaje import HijoProdigo
from acciones import acciones


def mostrar_menu():
    print("\n--- ACCIONES ---")
    for clave, accion in acciones.items():
        print(f"{clave}. {accion['nombre']}")
    print("4. Salir")


def main():
    nombre = input("Ingrese el nombre del personaje : ")
    hijo = HijoProdigo(nombre)

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "4":
            print("Saliendo del juego...")
            break

        if opcion not in acciones:
            print("Opción inválida")
            continue

        accion = acciones[opcion]

        if not hijo.puede_realizar(accion["costo"]):
            print("No tienes suficiente dinero")
            continue

        hijo.aplicar_cambios(accion["cambios"])
        print(hijo.estado())


if __name__ == "__main__":
    main()