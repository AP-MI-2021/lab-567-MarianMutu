from copy import deepcopy
from Domain.obiect import *


def add_obiect(lst_obiecte, id, nume, descriere, pret_achizitie, locatie):
    """
    Adaugam in memorie, un obiect format din campurile: id, nume, descriere, pret_achizitie, locatie
    :param lst_obiecte: lista de obiecte
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret_achizitie: string
    :param locatie: string
    :return: 
    """
    error = []
    if len(id) == 0:
        error.append("ID-ul nu poate fi vid!")
    if len(nume) == 0:
        error.append("Numele obiectului nu poate fi vid!")
    if len(descriere) == 0:
        error.append("Descrierea obiectului nu poate fi vid!")
    if len(locatie) != 4:
        error.append("Locatia obiectului trebuie sa aibe exact 4 caractere!")
    if read(lst_obiecte, id) is not None:
        error.append(f"Exista deja un obiect cu id-ul {id}!")
    if len(error) != 0:
        raise ValueError(f'{error}')
    obiect = create_obiect(id, nume, descriere, pret_achizitie, locatie)
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


def edit_obiect(obiecte, id, nume_new, descriere_new, pret_achizitie_new, locatie_new):
    """
    modificarea obiectului dupa ID si aruncarea unei erori ValueError daca au fost introduse date gresite
    :param obiecte: lista de obiecte
    :param id: string
    :param nume_new: string
    :param descriere_new: string
    :param pret_achizitie_new: float
    :param locatie_new: string
    :return:
    """
    updated_list = deepcopy(obiecte)
    for obiect in updated_list:
        if get_id(obiect) == id:
            set_nume(obiect, nume_new)
            set_descriere(obiect, descriere_new)
            set_pret_achizitie(obiect, pret_achizitie_new)
            set_locatie(obiect, locatie_new)
    return updated_list


def delete_obiect(obiecte, id):
    """
    sterge obiectul din lista 'obiecte' care are id-ul ID
    :param obiecte: lista de obiecte
    :param id: string
    :return:
    """
    if read(obiecte, id) is None:
        raise ValueError(f'Nu xista un obiect cu ID-ul {id} pe care sa il stergem!')

    result_list = [obiect for obiect in obiecte if get_id(obiect) != id]
    return result_list
