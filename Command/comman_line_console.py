from Domain.obiect import to_str
from Logic.crud import delete_obiect, add_obiect


def show_menu():
    print('Adaugare: add [id] [nume] [descrierea] [pret_achizitie] [locatie]')
    print('Afisare: showall')
    print('Stergere: delete [id]')
    print()
    print('Meniu: help')
    print('Iesire: exit')
    print('*Nota: mai multe comenzi adaugate pe acelasi rand necesita despartirea prin ";"!')


def run_add(lst_obiecte, id_introdus, nume_introdus, descriere_introdusa, pret_introdus, locatie_introdusa):
    try:
        id = id_introdus
        nume = nume_introdus
        descriere = descriere_introdusa
        pret_achizitie = float(pret_introdus)
        locatie = locatie_introdusa
        if len(locatie) != 4:
            raise ValueError("Locatia trrebuie sa aibe exact 4 caractere!")
        return add_obiect(lst_obiecte, id, nume, descriere, pret_achizitie, locatie)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
    return lst_obiecte


def run_delete(id_introdus, lst_obiecte):
    '''
    Sterge un obiect din lista.
    :param id_introdus: id-ul obiectului retinut dinttr-o lista.
    :param lst_obiecte: lista cu obiecte.
    :return: lista cu obiecte dupa stergere.
    '''
    try:
        id = id_introdus
        return delete_obiect(lst_obiecte, id)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lst_obiecte


def run_show_all(lst_obiecte):
    '''
    Afiseaza toate obiectele.
    :param lst_obiecte: lista de obiecte.
    :return: -
    '''
    for obiect in lst_obiecte:
        print(to_str(obiect))
    if len(lst_obiecte) == 0:
        print("Nu exista nici un element introdus!")


def line_console(lst_obiecte):
    while True:
        show_menu()
        toata_comanda = input("Introduceti lista de obiecte. Acestea trebuie despartite prin ;. "
                              "Itemii din cadrul comenzii trebuie despartiti prin virgula"
                              " si nu trebuie sa existe spatiu intre cuvinte ")
        comanda = toata_comanda.split(";")
        for comanda in comanda:
            com = comanda.split(",")
            if com[0] == "add":
                try:
                    lst_obiecte = run_add(lst_obiecte, com[1], com[2], com[3], com[4], com[5])
                except ValueError as ve:
                    print("Eroare: ", ve)
            elif com[0] == "delete":
                lst_obiecte = run_delete(str(com[1]), lst_obiecte)
            elif com[0] == "help":
                show_menu()
            elif com[0] == "showall":
                run_show_all(lst_obiecte)
            elif com[0] == "exit":
                break
            else:
                print("Comanda invalida!")
