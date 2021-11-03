from Domain.obiect import *


def move_obiect_from_one_location_to_another(lst_obiecte, locatie_veche, locatie_noua):
    """
    muta toate obiectele din locatia "locatie_veche" in "locatie_noua"
    :param lst_obiecte:  lista de obiecte
    :param locatie_veche: string
    :param locatie_noua: string
    :return:
    """
    for obiect in lst_obiecte:
        if get_locatie(obiect) == locatie_veche:
            set_locatie(obiect, locatie_noua)
    return lst_obiecte


def add_string_by_price(lst_obiecte, val, string):
    """
    adauga la un obiect cu pretul mai mare decat "val" un string citit de la tastatura
    :param lst_obiecte: lista de obiecte
    :param val: valoarea cu care se compara
    :param string: string-ul citit de la tastatura
    :return:
    """
    for obiect in lst_obiecte:
        if get_pret_achizitie(obiect) > val:
            descriere_new = get_descriere(obiect) + string
            set_descriere(obiect, descriere_new)
    return lst_obiecte

