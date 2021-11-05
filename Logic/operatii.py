from Domain.obiect import *


def move_obiect_from_one_location_to_another(lst_obiecte, locatie_veche, locatie_noua, undo_list: list, redo_list: list):
    """
    muta toate obiectele din locatia "locatie_veche" in "locatie_noua"
    :param undo_list: lista de undo
    :param redo_list:  lista de redo
    :param lst_obiecte:  lista de obiecte
    :param locatie_veche: string
    :param locatie_noua: string
    :return: lista de obiecte modificata
    """
    for obiect in lst_obiecte:
        if get_locatie(obiect) == locatie_veche:
            set_locatie(obiect, locatie_noua)

    undo_list.append(lst_obiecte)
    redo_list.clear()
    return lst_obiecte


def add_string_by_price(lst_obiecte, val, string, undo_list: list, redo_list: list):
    """
    adauga la un obiect cu pretul mai mare decat "val" un string citit de la tastatura
    :param redo_list: lista de redo
    :param undo_list: lista de undo
    :param lst_obiecte: lista de obiecte
    :param val: valoarea cu care se compara
    :param string: string-ul citit de la tastatura
    :return: lista de obiecte modificata
    """
    for obiect in lst_obiecte:
        if get_pret_achizitie(obiect) > float(val):
            descriere_new = get_descriere(obiect) + string
            set_descriere(obiect, descriere_new)

    undo_list.append(lst_obiecte)
    redo_list.clear()
    return lst_obiecte


def biggest_price_for_each_location(lst_obiecte):
    """
    determina cel mai mare pret pentru fiecare loactie
    :param lst_obiecte: lista de obiecte
    :return: Dict
    """
    result = {}
    for obiect in lst_obiecte:
        if get_locatie(obiect) not in result:
            result[get_locatie(obiect)] = get_pret_achizitie(obiect)
        elif result[get_locatie(obiect)] < get_pret_achizitie(obiect):
            result[get_locatie(obiect)] = get_pret_achizitie(obiect)
    return result


def ordered_items_ascending_by_price(lst_obiecte):
    """
    ordoneaza obiectele in ordine crescatoare dupa pretul de achizitie
    :param lst_obiecte:
    :return: lista cu obiectele ordonate
    """
    return sorted(lst_obiecte, key=lambda obiect: get_pret_achizitie(obiect))
    # lambda este o functie anonima
    # pe care o folosim doar in aceasta operatie ne mai
    # fiind nevoie sa creeam o alta functie de tip procedura


def sum_of_prices_for_each_locations(lst_obiecte):
    """
    determina suma preturilor pentru fiecare locatie
    :param lst_obiecte:
    :return:
    """
    result = {}
    for obiect in lst_obiecte:
        if get_locatie(obiect) not in result:
            result[get_locatie(obiect)] = get_pret_achizitie(obiect)
        else:
            result[get_locatie(obiect)] += round(get_pret_achizitie(obiect))
    return result

