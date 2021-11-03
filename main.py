from Command.comman_line_console import line_console
from Domain.obiect import create_obiect
from Tests.run_all_tests import run_all_tests
from UserInterface.consola import run_console


def main():
    lst_obiecte = []
    menu = str(input("Dati tipul de meniu dorit (basic / command): "))
    if menu == "basic":
        run_console(lst_obiecte)
    elif menu == "command":
        line_console(lst_obiecte)


run_all_tests()
main()
