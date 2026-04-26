"""Módulo de ejemplo: modela un `HijoProdigo` con acciones y un CLI.

Provee una clase con varias acciones (gastar, invertir, ahorrar),
algunas utilidades y un pequeño menú interactivo para probarlas.
"""

from typing import Optional


class HijoProdigo:
    """Representa a un hijo pródigo con atributos y acciones simples."""

    def __init__(self, nombre: str) -> None:
        self.nombre: str = nombre
        self.dinero: int = 100
        self.dignidad: int = 50
        self.hambre: int = 0
        self.arrepentimiento: int = 0

    def gastar_en_fiestas(self) -> None:
        """Gasta dinero en fiestas; reduce dignidad y aumenta hambre."""
        self.dinero -= 20
        self.dignidad -= 10
        self.hambre += 5
        print(f"{self.nombre} ha gastado dinero en fiestas. Dinero: {self.dinero}, Dignidad: {self.dignidad}, Hambre: {self.hambre}")

    def invertir(self) -> None:
        """Invierte parte del dinero; puede aumentar dignidad ligeramente."""
        self.dinero -= 30
        self.dignidad += 5
        self.hambre += 2
        print(f"{self.nombre} ha invertido una parte de su dinero. Dinero: {self.dinero}, Dignidad: {self.dignidad}, Hambre: {self.hambre}")

    def ahorrar(self) -> None:
        """Ahorra dinero y mejora un poco la dignidad; reduce hambre."""
        self.dinero += 10
        self.dignidad += 2
        self.hambre = max(0, self.hambre - 3)
        print(f"{self.nombre} ha ahorrado. Dinero: {self.dinero}, Dignidad: {self.dignidad}, Hambre: {self.hambre}")

    def alimentar(self, comida: int = 5) -> None:
        """Reduce el hambre a cambio de una pequeña cantidad de dinero."""
        coste = 5
        if self.dinero >= coste:
            self.dinero -= coste
            self.hambre = max(0, self.hambre - comida)
            print(f"{self.nombre} se ha alimentado. Hambre: {self.hambre}, Dinero: {self.dinero}")
        else:
            print(f"{self.nombre} no tiene suficiente dinero para comer.")

    def arrepentirse(self) -> None:
        """Aumenta el arrepentimiento y recupera algo de dignidad."""
        self.arrepentimiento += 10
        self.dignidad += 5
        print(f"{self.nombre} se ha arrepentido. Arrepentimiento: {self.arrepentimiento}, Dignidad: {self.dignidad}")

    def estado(self) -> str:
        """Devuelve una representación corta del estado actual."""
        return (
            f"{self.nombre} — Dinero: {self.dinero}, Dignidad: {self.dignidad}, "
            f"Hambre: {self.hambre}, Arrepentimiento: {self.arrepentimiento}"
        )


def main(name: Optional[str] = None) -> None:
    """Ejecuta un pequeño CLI para interactuar con un `HijoProdigo`."""
    if name is None:
        name = input("¿Cuál es tu nombre? ") or "AA"

    hijo = HijoProdigo(name)

    menu = (
        "\nSeleccione una acción:\n"
        "1. Gastar en fiestas\n"
        "2. Invertir\n"
        "3. Ahorrar\n"
        "4. Alimentar\n"
        "5. Arrepentirse\n"
        "6. Mostrar estado\n"
        "0. Salir\n"
    )

    while True:
        print(menu)
        opcion = input("Ingrese el número de la opción que desea elegir: ").strip()
        if opcion == "1":
            hijo.gastar_en_fiestas()
        elif opcion == "2":
            hijo.invertir()
        elif opcion == "3":
            hijo.ahorrar()
        elif opcion == "4":
            hijo.alimentar()
        elif opcion == "5":
            hijo.arrepentirse()
        elif opcion == "6":
            print(hijo.estado())
        elif opcion == "0":
            print("Saliendo. Hasta luego.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()