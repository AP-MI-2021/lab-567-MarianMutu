from copy import deepcopy
from Domain.obiect import *


def add_obiect(lst_obiecte, id_introdus, nume, descriere, pret_achizitie, locatie, undo_list: list, redo_list: list):
    """
    Adaugam in memorie, un obiect format din campurile: id, nume, descriere, pret_achizitie, locatie
    :param lst_obiecte: lista de obiecte
    :param id_introdus: string
    :param nume: string
    :param descriere: string
    :param pret_achizitie: string
    :param locatie: string
    :param undo_list: lista de undo
    :param redo_list: lista de redo
    :return: 
    """
    error = []
    if float(pret_achizitie) < 0:
        error.append("Pretul nu poate fi un numar negativ")
    if len(id_introdus) == 0:
        error.append("ID-ul nu poate fi vid!")
    if len(nume) == 0:
        error.append("Numele obiectului nu poate fi vid!")
    if len(descriere) == 0:
        error.append("Descrierea obiectului nu poate fi vid!")
    if len(locatie) != 4:
        error.append("Locatia obiectului trebuie sa aibe exact 4 caractere!")
    if read(lst_obiecte, id_introdus) is not None:
        error.append(f"Exista deja un obiect cu id-ul {id_introdus}!")
    if len(error) != 0:
        raise ValueError(f'{error}')

    undo_list.append(lst_obiecte)
    redo_list.clear()
    obiect = create_obiect(id_introdus, nume, descriere, pret_achizitie, locatie)
    return lst_obiecte + [obiect]


def read(lst_obiecte, id_obiect):
    """
    Citeste o prajitura din "baza de date".
    :param lst_obiecte: lista de obiecte
    :param id_obiect: id-ul obiectului dorit.
    :return:
        - obiectul cu id-ul id_obiect, daca exista
        - lista cu toate obiectele, daca id_obiect = None
        - None, daca nu exista un obiect cu id_obiect
    """

    if not id_obiect:
        return lst_obiecte

    obiect_cu_id = None
    for obiect in lst_obiecte:
        if get_id(obiect) == id_obiect:
            obiect_cu_id = obiect

    if obiect_cu_id:
        return obiect_cu_id
    return None


def edit_obiect(lst_obiecte, id_introdus, nume_new, descriere_new, pret_achizitie_new, locatie_new,
                undo_list: list, redo_list: list):
    """
    modificarea obiectului dupa ID si aruncarea unei erori ValueError daca au fost introduse date gresite
    :param redo_list: lista de redo
    :param undo_list: lista de undo
    :param lst_obiecte: lista de obiecte
    :param id_introdus: string
    :param nume_new: string
    :param descriere_new: string
    :param pret_achizitie_new: float
    :param locatie_new: string
    :return:
    """
    try:
        error = []
        if float(pret_achizitie_new) < 0:
            error.append("Noul pret nu poate fi un numar negativ")
        if len(nume_new) == 0:
            error.append("Noul nume al obiectului nu poate fi vid!")
        if len(descriere_new) == 0:
            error.append("Noua descriere a obiectului nu poate fi vid!")
        if len(locatie_new) != 4:
            error.append("Noua locatie a obiectului trebuie sa aibe exact 4 caractere!")
        if len(error) != 0:
            raise ValueError(f'{error}')
        pret_achizitie_new = float(pret_achizitie_new)
    except ValueError as error:
        print(error)

    updated_list = deepcopy(lst_obiecte)
    for obiect in updated_list:
        if get_id(obiect) == id_introdus:
            set_nume(obiect, nume_new)
            set_descriere(obiect, descriere_new)
            set_pret_achizitie(obiect, pret_achizitie_new)
            set_locatie(obiect, locatie_new)
    undo_list.append(lst_obiecte)
    redo_list.clear()
    return updated_list


def delete_obiect(lst_obiecte, id_introdus, undo_list: list, redo_list: list):
    """
    sterge obiectul din lista 'obiecte' care are id-ul ID
    :param undo_list: lista de undo
    :param redo_list: lista de redo
    :param lst_obiecte: lista de obiecte
    :param id_introdus: string
    :return:
    """
    if read(lst_obiecte, id_introdus) is None:
        raise ValueError(f'Nu xista un obiect cu ID-ul {id_introdus} pe care sa il stergem!')

    result_list = [obiect for obiect in lst_obiecte if get_id(obiect) != id_introdus]

    undo_list.append(lst_obiecte)
    redo_list.clear()
    return result_list
