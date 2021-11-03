from Domain.obiect import to_str
from Logic.crud import add_obiect, edit_obiect, delete_obiect
from Logic.operatii import move_obiect_from_one_location_to_another, add_string_by_price


def print_menu():
    print("""
    MENIU
    1. CRUD
    2. Operatii
    3. Undo
    x. Iesire 
    """)


def print_crud_menu():
    print("""
    MENIU CRUD
    1. Adaugare
    2. Modificare
    3. Stergere
    4. Afisare toate obiecte
    5. Inapoi
    """)


def print_operatii_menu():
    print("""
    MENIU OPERATII
    1. Mutarea tuturor obiectelor dintr-o locație în alta.
    2. Concatenarea unui string citit la toate descrierile obiectelor
    cu prețul mai mare decât o valoare citită.
    3. Determinarea celui mai mare preț pentru fiecare locație.
    4. Ordonarea obiectelor crescător după prețul de achiziție.
    5. Afișarea sumelor prețurilor pentru fiecare locație.
    a. Afisarea tuturor obiectelor
    6. Inapoi
    """)


def handle_add_obiect(lst_obiecte):
    """
    Adaugare obiect citit de la tastatura
    :param lst_obiecte: lista de obiecte
    :return:
    """
    try:
        id = input("Introduceti ID-ul obiectului: ")
        nume = input("Introduceti numele obiectului: ")
        descriere = input("Introduceti descrierea obiectului: ")
        pret_achizitie = float(input("Introduceti pretul de achizitie: "))
        locatie = input("Introduceti locatia: ")
        return add_obiect(lst_obiecte, id, nume, descriere, pret_achizitie, locatie)
    except ValueError as ve:
        print("Eroare: ", ve)
    return lst_obiecte


def handle_show_all(lst_obiecte):
    """
    Afisare lista de obiecte din memorie
    :param lst_obiecte: lista de obiecte
    :return:
    """
    for obiect in lst_obiecte:
        print(to_str(obiect))
    if len(lst_obiecte) == 0:
        print("Nu exista nici un element introdus!")


def handle_edit_obiect(lst_obiecte):
    """
    modifica un obiect introdus
    :param lst_obiecte: lista de obiecte
    :return:
    """
    try:
        id_introdus = input("Introduceti ID-ul obiectului pe care vreti sa-l modificati: ")
        nume_new = input("Introduceti noul nume al obiectului: ")
        descriere_new = input("Introduceti noua descriere a obiectului: ")
        pret_achizitie_new = input("Introduceti noul pret de achizitie: ")
        locatie_new = input("Introduceti noua locatie: ")
        return edit_obiect(lst_obiecte, id_introdus, nume_new, descriere_new, pret_achizitie_new, locatie_new)
    except ValueError as ve:
        print("Eroare: ", ve)
    return lst_obiecte


def handle_delete_obiect(lst_obiecte):
    """
    stergerea unui obiect dupa un id introdus de la tastatura
    :param lst_obiecte: lista de obiecte
    :return: lista de obiecte fara obiectul sters
    """
    try:
        id = input("Introduceti ID-ul obiectului pe care doriti sa-l stergeti:")
        obiecte = delete_obiect(lst_obiecte, id)
        print("Obiect sters cu succes!")
        return obiecte
    except ValueError as ve:
        print("Eroare: ", ve)
    return lst_obiecte


def run_crud_ui(lst_obiecte):
    """
    ruleaza interfata cu utilizatorul pentru meniul CRUD
    :param lst_obiecte: lista de obiecte
    :return: o lista de obiecte
    """
    while True:
        print_crud_menu()
        cmd = input("Introduceti o comanda: ")
        if cmd == '1':
            lst_obiecte = handle_add_obiect(lst_obiecte)
        elif cmd == '2':
            lst_obiecte = handle_edit_obiect(lst_obiecte)
        elif cmd == '3':
            lst_obiecte = handle_delete_obiect(lst_obiecte)
        elif cmd == '4':
            handle_show_all(lst_obiecte)
        elif cmd == '5':
            break
        else:
            print("Comanda invalida!")

    return lst_obiecte


def run_undo_ui(obiecte):
    pass


def run_operatii_ui(lst_obiecte):
    """
    rulare meniu operatii
    :param lst_obiecte: lista de obiecte
    :return:
    """
    def handle_move_obiect_from_locatie(lst_obiecte):
        """
        muta un obiect dintr-o locatie in alta
        :param lst_obiecte:
        :return:
        """
        locatie_veche = input("Introduceti o locatie din care doriti sa mutati obiecte: ")
        locatie_noua = input("Introduceti noua locatie: ")
        if len(locatie_noua) == len(locatie_veche) == 4:
            lst_obiecte = move_obiect_from_one_location_to_another(lst_obiecte, locatie_veche, locatie_noua)
            print("Obiect mutat cu succes!")
            return lst_obiecte
        else:
            print("Nu ati introdus locatii valide!")

    def handle_add_string_from_price(lst_obiecte):
        """
        adauga la locatia unui obiect un string citit de la tastatura daca
        pretul este mai mare decat o valoare citita de la tastatura
        :param lst_obiecte:
        :return:
        """
        try:
            val = float(input("Introduceti o valoare dupa care doriti sa comparatati pretul obiectelor: "))
            string = input("Introduceti un string pe care doriti sa-l adaugati la descrierea obiectelor: ")
            return add_string_by_price(lst_obiecte, val, string)
        except ValueError as ve:
            print("Eroare: ", ve)

    while True:
        print_operatii_menu()
        cmd = input("Introduceti o comanda: ")
        if cmd == '1':
            lst_obiecte = handle_move_obiect_from_locatie(lst_obiecte)
        elif cmd == '2':
            lst_obiecte = handle_add_string_from_price(lst_obiecte)
        elif cmd == '3':
            pass
        elif cmd == '4':
            pass
        elif cmd == '5':
            pass
        elif cmd == 'a':
            handle_show_all(lst_obiecte)
        elif cmd == '6':
            break
        else:
            print("Comanda invalida!")
    return lst_obiecte


def run_console(lst_obiecte):
    """
    ruleaza meniul principal
    :param lst_obiecte: lista de obiecte
    :return:
    """
    while True:
        print_menu()
        cmd = input("Introduceti o comanda: ")
        if cmd == '1':
            lst_obiecte = run_crud_ui(lst_obiecte)
        elif cmd == '2':
            lst_obiecte = run_operatii_ui(lst_obiecte)
        elif cmd == '3':
            run_undo_ui(lst_obiecte)
        elif cmd == 'x':
            print("La revedere!")
            break
        else:
            print("Comanda invalida!")
