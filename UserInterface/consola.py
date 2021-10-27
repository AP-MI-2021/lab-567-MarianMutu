from Domain.obiect import to_str
from Logic.crud import add_obiect, edit_obiect, delete_obiect


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
    6. Inapoi
    """)


def run_crud_ui(obiecte):
    """

    :param obiecte: lista de obiecte
    :return:
    """

    def handle_add_obiect(obiecte):
        """
        Adaugare obiect citit de la tastatura
        :param obiecte: lista de obiecte
        :return:
        """
        id = input("Introduceti ID-ul obiectului: ")
        nume = input("Introduceti numele obiectului: ")
        descriere = input("Introduceti descrierea obiectului: ")
        pret_achizitie = input("Introduceti pretul de achizitie: ")
        locatie = input("Introduceti locatia: ")
        try:

            obiecte = add_obiect(obiecte, id, nume, descriere, pret_achizitie, locatie)
            print("Obiect adaugat cu succes!")
            return obiecte
        except ValueError as ve:
            print("!!!Au aparut erori")
            print(ve)

    def handle_show_all(obiecte):
        """
        Afisare lista de obiecte din memorie
        :param obiecte: lista de obiecte
        :return:
        """
        for obiect in obiecte:
            print(to_str(obiect))

    def handle_edit_obiect(obiecte):
        """
        modifica un obiect introdus
        :param obiecte: lista de obiecte
        :return:
        """
        id = input("Introduceti ID-ul obiectului pe care vreti sa-l modificati: ")
        nume_new = input("Introduceti noul nume al obiectului: ")
        descriere_new = input("Introduceti noua descriere a obiectului: ")
        pret_achizitie_new = input("Introduceti noul pret de achizitie: ")
        locatie_new = input("Introduceti noua locatie: ")
        try:
            obiecte = edit_obiect(obiecte, id, nume_new, descriere_new, pret_achizitie_new, locatie_new)
            print("Obiect modificat cu succes!")
            return obiecte
        except ValueError as ve:
            print("!!!Au aparut erori")
            print(ve)

    def handle_delete_obiect(obiecte):
        id_introdus = input("introduceti ID-ul obiectului pe care doriti sa-l stergeti: ")
        print("Obiect sters cu succes")
        return delete_obiect(obiecte, id_introdus)

    while True:
        print_crud_menu()
        cmd = input("Introduceti o comanda: ")
        if cmd == '1':
            obiecte = handle_add_obiect(obiecte)
        elif cmd == '2':
            obiecte = handle_edit_obiect(obiecte)
        elif cmd == '3':
            obiecte = handle_delete_obiect(obiecte)
        elif cmd == '4':
            handle_show_all(obiecte)
        elif cmd == '5':
            break
        else:
            print("Comanda invalida!")


def run_undo_ui(obiecte):
    pass


def run_operatii_ui(obiecte):
    """
    rulare meniu operatii
    :param obiecte: lista de obiecte
    :return:
    """
    while True:
        print_operatii_menu()
        cmd = input("Introduceti o comanda: ")
        if cmd == '1':
            pass
        elif cmd == '2':
            pass
        elif cmd == '3':
            pass
        elif cmd == '4':
            pass
        elif cmd == '5':
            pass
        elif cmd == '6':
            break
        else:
            print("Comanda invalida!")


def run_console(obiecte):
    """

    :param obiecte: lista de obiecte
    :return:
    """
    while True:
        print_menu()
        cmd = input("Introduceti o comanda: ")
        if cmd == '1':
            run_crud_ui(obiecte)
        elif cmd == '2':
            run_operatii_ui(obiecte)
        elif cmd == '3':
            run_undo_ui(obiecte)
        elif cmd == 'x':
            print("La revedere!")
            break
        else:
            print("Comanda invalida!")
