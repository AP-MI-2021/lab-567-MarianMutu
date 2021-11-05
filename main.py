from Command.comman_line_console import line_console
from Logic.crud import add_obiect
from Tests.run_all_tests import run_all_tests
from UserInterface.consola import run_console


def main():
    lst_obiecte = []
    undo_list = []
    redo_list = []
    lst_obiecte = add_obiect(lst_obiecte, "248", "Calculator", "electronice", 14.90, "bist", undo_list, redo_list)
    lst_obiecte = add_obiect(lst_obiecte, "244", "culegere", "de matematica", 14.99, "cluj", undo_list, redo_list)
    lst_obiecte = add_obiect(lst_obiecte, "247", "caiet", "de prezenta", 86.99, "iasi", undo_list, redo_list)
    lst_obiecte = add_obiect(lst_obiecte, "249", "Carte", "biblioteca", 4999.90, "bist", undo_list, redo_list)
    lst_obiecte = add_obiect(lst_obiecte, "245", "culegere", "de fizica", 82.99, "iasi", undo_list, redo_list)
    lst_obiecte = add_obiect(lst_obiecte, "257", "caiet", "de absente", 26.99, "bist", undo_list, redo_list)
    while True:
        menu = str(input("Introduceti tipul de meniu dorit (basic / command): "))
        if menu == "basic":
            run_console(lst_obiecte, undo_list, redo_list)
        elif menu == "command":
            line_console(lst_obiecte)
        elif menu == 'cancel':
            break
        else:
            print("Tip meniu invalid! Daca doriti sa va opriti introduceti 'cancel'.")


run_all_tests()
main()
