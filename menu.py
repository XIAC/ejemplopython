import os
from prettytable import PrettyTable

_table = PrettyTable(["Opcion", "Accion"])
_table.add_row([0, "Gastar en fiestas"])
_table.add_row([1, "Invertir una parte"])
_table.add_row([2, "Ahorrar"])
_table.add_row([3, "Ver estado"])
_table.add_row([4, "Ver historial"])
_table.add_row([5, "Salir"])


def show_menu(jugador):
    os.system("clear")
    print('\033[1;32;40m' + f"\n  Jugador: {jugador.nombre}  |  {jugador.estado()}\n")
    print(_table.get_string(title='>>>   EL HIJO PRODIGO   <<<') + '\033[0m')
