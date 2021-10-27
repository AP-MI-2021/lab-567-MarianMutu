def validator(id, nume, descriere, pret_achizitie, locatie):
    """
    validarea datelor introduse
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret_achizitie: string se returneaza float
    :param locatie: string
    :return:
    """
    errors = []
    if id == '':
        errors.append("ID-ul nu poate fi vid!")
    if nume == '':
        errors.append("Numele nu poate fi vid!")
    if descriere == '':
        errors.append("Descrierea nu poate fi vid!")
    if len(locatie) != 4:
        errors.append("Locatia trebuie sa contina exact 4 caractere!")
    try:
        pret_achizitie = float(pret_achizitie)
        if pret_achizitie < 0:
            errors.append("Pretul nu poate fi negativ!")
    except ValueError:
        errors.append("Pretul trebuie sa fie numar real!")

    if len(errors) != 0:
        raise ValueError(errors)
    return id, nume, descriere, pret_achizitie, locatie
