from Domain.obiect import to_str
from Logic.crud import delete_obiect, add_obiect
from Logic.undo_redo import do_undo, do_redo


def show_menu():
    print()
    print("""
    § Adaugare: add [id] [nume] [descrierea] [pret_achizitie] [locatie]'
    § Afisare: showall
    § Stergere: delete [id]
    § Meniu: help
    § Undo:  undo
    § Redo: redo
    § Iesire: exit
    * Nota: mai multe comenzi adaugate pe acelasi rand necesita despartirea prin ";"!
    """)
    print()


def show_help():
    print(""" 
        § Mai multe comenzi vor fi despartite prin ";"
        § Itemii din cadrul comenzii trebuie despartiti prin "," si nu trebuie sa existe spatiu intre cuvinte.
        § Pentru add se vor intorduce 6 itemi despartiti prin ","
        § Pentru delete se vor intorduce 2 itemi despartiti prin "," """)


def run_add(lst_obiecte, id_introdus, nume_introdus, descriere_introdusa,
            pret_introdus, locatie_introdusa, undo_list, redo_list):
    """
    adaugarea unui obiect nou in lista
    :param lst_obiecte: lista de obiecte
    :param id_introdus: string
    :param nume_introdus: string
    :param descriere_introdusa: string
    :param pret_introdus: string si returneaza float
    :param locatie_introdusa: string
    :param undo_list: lista de undo
    :param redo_list: lista de redo
    :return: o lista de obiecte
    """
    try:
        nume = nume_introdus
        descriere = descriere_introdusa
        pret_achizitie = float(pret_introdus)
        locatie = locatie_introdusa
        if len(locatie) != 4:
            raise ValueError("Locatia trrebuie sa aibe exact 4 caractere!")
        return add_obiect(lst_obiecte, id_introdus, nume, descriere, pret_achizitie, locatie, undo_list, redo_list)
    except ValueError as ve:
        print("Eroare: {}".format(ve))

    undo_list.append(lst_obiecte)
    redo_list.clear()
    return lst_obiecte


def run_delete(id_introdus, lst_obiecte, undo_list, redo_list):
    """
    Sterge un obiect din lista.
    :param redo_list: lista de redo
    :param undo_list: lista de undo
    :param id_introdus: id-ul obiectului retinut dinttr-o lista.
    :param lst_obiecte: lista cu obiecte.
    :return: lista cu obiecte dupa stergere.
    """
    try:
        obiecte = delete_obiect(lst_obiecte, id_introdus, undo_list, redo_list)
        print("Obiect sters cu succes!")
        return obiecte
    except ValueError as ve:
        print("Eroare: ", ve)
    return lst_obiecte


def run_show_all(lst_obiecte):
    """
    Afiseaza toate obiectele.
    :param lst_obiecte: lista de obiecte.
    :return: -
    """
    for obiect in lst_obiecte:
        print(to_str(obiect))
    if len(lst_obiecte) == 0:
        print("Nu exista nici un element introdus!")


def run_undo(undo_list, redo_list, lst_obiecte):
    """
    Undo
    :param undo_list: lista de undo
    :param redo_list: lista de redo
    :param lst_obiecte: lista de obiecte
    :return: lista de undo sau lista de obiecte daca lista de undo e None
    """
    undo_result = do_undo(undo_list, redo_list, lst_obiecte)
    if undo_result is not None:
        return undo_result
    else:
        return lst_obiecte


def run_redo(undo_list, redo_list, lst_obiecte):
    """
    Redo
    :param undo_list: lista de undo
    :param redo_list: lista de redo
    :param lst_obiecte: lista de obiecte
    :return: lista de redo sau lista de obiecte daca lista de redo e None
    """
    redo_result = do_redo(undo_list, redo_list, lst_obiecte)
    if redo_result is not None:
        return redo_result
    else:
        return lst_obiecte


def handle_add_obiect(lst_obiecte, com, undo_list, redo_list):
    """
    validari pt adaugarea unui obiect
    :param lst_obiecte: lista de obiecte
    :param com: comanda introdusa
    :param undo_list: lista de undo
    :param redo_list: lista de redo
    :return: lista de obiecte
    """
    if len(com) == 6:
        lst_obiecte = run_add(lst_obiecte, com[1], com[2], com[3], com[4], com[5], undo_list, redo_list)
    else:
        raise ValueError("Campurile pentru obiect nu sunt completate corect,"
                         " introdu help pentru mai mulre detalii!")

    return lst_obiecte


def handle_delete_obiect(lst_obiecte, com, undo_list, redo_list):
    """
    validari delete obiect
    :param lst_obiecte: lista de obiecte
    :param com: coanda introdusa
    :param undo_list: lista de undo
    :param redo_list: lista de redo
    :return: lista de obiecte
    """
    if len(com) == 2:
        lst_obiecte = run_delete(com[1], lst_obiecte, undo_list, redo_list)
    else:
        raise ValueError("Campurile pentru stergerea unui obiect nu"
                         " sunt completate corect, introdu help pentru mai mulre detalii!")
    return lst_obiecte


def line_console(lst_obiecte, undo_list, redo_list):
    """
    interfata cu utilizatorul
    :param lst_obiecte: lista de obiecte
    :param undo_list: lista de undo
    :param redo_list: lista de redo
    :return:
    """
    try:
        while True:
            show_menu()
            toata_comanda = input("Introduceti o comanda: ")
            stop = False
            toata_comanda = toata_comanda.split(';')
            for i in range(len(toata_comanda)):
                com = toata_comanda[i].split(',')
                if com[0] == "add":
                    lst_obiecte = handle_add_obiect(lst_obiecte, com, undo_list, redo_list)
                elif com[0] == "help":
                    show_help()
                elif com[0] == "showall":
                    run_show_all(lst_obiecte), print()
                elif com[0] == "delete":
                    lst_obiecte = handle_delete_obiect(lst_obiecte, com, undo_list, redo_list)
                elif com[0] == 'undo':
                    lst_obiecte = run_undo(undo_list, redo_list, lst_obiecte)
                elif com[0] == 'redo':
                    lst_obiecte = run_redo(undo_list, redo_list, lst_obiecte)
                elif com[0] == "exit":
                    stop = True
                else:
                    print("Comanda invalida!")
            if stop is True:
                break
    except ValueError as ve:
        print("Eroare: ", ve)


#  add,1,nume,descriere,32,2000;showall;delete,1;showall
