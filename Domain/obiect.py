def create_obiect(id, nume, descriere, pret_achizitie, locatie):
    """

    :param id: string
    :param nume: string
    :param descriere: string
    :param pret_achizitie: float
    :param locatie: string (exact 4 caractere)
    :return: List  #Dict
    :return: un obiect
    """
    #  return {
    #  "id": id,
    #   "nume": nume,
    #  "descriere": descriere,
    #  "pret_achizitie": pret_achizitie,
    #  "locatie": locatie,
#  }
    return [id, nume, descriere, pret_achizitie, locatie]


def get_id(obiect):
    """
    
    :param obiect: list #  Dict
    :return: id - string
    """
    #  return obiect["id"]
    return obiect[0]


def get_nume(obiect):
    """

    :param obiect:  list #  Dict
    :return: nume - string
    """
    #  return obiect["nume"]
    return obiect[1]


def get_descriere(obiect):
    """

    :param obiect:  list #  Dict
    :return: descriere - string
    """
    #  return obiect["descriere"]
    return obiect[2]


def get_pret_achizitie(obiect):
    """

    :param obiect:  list #  Dict
    :return: pret achizitie - float
    """
    #  return obiect["pret_achizitie"]
    return obiect[3]


def get_locatie(obiect):
    """

    :param obiect:  list #  Dict
    :return: locatie - string
    """
    #  return obiect["locatie"]
    return obiect[4]


def set_id(obiect, id):
    """
    Setarea id la obiect
    :param obiect:  list #  Dict
    :param id: string
    :return:
    """
    #  obiect["id"] = id
    obiect[0] = id


def set_nume(obiect, nume):
    """
    Setarea nume la obiect
    :param obiect: list #  Dict
    :param nume: string
    :return:
    """
    #  obiect["nume"] = nume
    obiect[1] = nume


def set_descriere(obiect, descriere):
    """
    Setarea descriere la obiect
    :param obiect:  list #  Dict
    :param descriere: string
    :return:
    """
    #  obiect["descriere"] = descriere
    obiect[2] = descriere


def set_pret_achizitie(obiect, pret_achizitie):
    """
    Setarea pret_achizitie la obiect
    :param obiect:  list #  Dict
    :param pret_achizitie: float
    :return:
    """
    #  obiect["pret_achizitie"] = pret_achizitie
    obiect[3] = pret_achizitie


def set_locatie(obiect, locatie):
    """
    Setarea locatie la obiect
    :param obiect:  list #  Dict
    :param locatie: string
    :return:
    """
    #  obiect["locatie"] = locatie
    obiect[4] = locatie


def to_str(obiect):
    return f'ID = {get_id(obiect)},  nume = {get_nume(obiect)},  descriere = {get_descriere(obiect)}, ' \
           f'pret_achizitie = {get_pret_achizitie(obiect)},  locatie = {get_locatie(obiect)}'
