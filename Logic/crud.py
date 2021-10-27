from copy import deepcopy
from Domain.obiect import *
from Logic.validator import validator


def add_obiect(obiecte, id, nume, descriere, pret_achizitie, locatie):
    """
    Adaugam in memorie, un obiect format din campurile: id, nume, descriere, pret_achizitie, locatie
    :param obiecte: lista de obiecte
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret_achizitie: string
    :param locatie: string
    :return: 
    """

    id, nume, descriere, pret_achizitie, locatie = validator(id, nume, descriere, pret_achizitie, locatie)
    obiect = create_obiect(id, nume, descriere, pret_achizitie, locatie)
    return obiecte + [obiect]


def find_obiect(obiecte, id):
    """
    cauta un obiect dupa id
    :param obiecte:
    :param id:
    :return:
    """
    for obiect in obiecte:
        if get_id(obiect) == id:
            return obiect
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
    id, nume_new, descriere_new, pret_achizitie_new, locatie_new = \
        validator(id, nume_new, descriere_new, pret_achizitie_new, locatie_new)
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
    result_list = [obiect for obiect in obiecte if get_id(obiect) != id]
    return result_list
