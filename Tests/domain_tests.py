from Domain.obiect import *


def obiect_test():
    obiect = create_obiect('128A93', 'stilou', 'rechizite', 2.99, 'Vivo')
    assert get_id(obiect) == '128A93'
    assert get_nume(obiect) == 'stilou'
    assert get_descriere(obiect) == 'rechizite'
    assert get_pret_achizitie(obiect) == 2.99
    assert get_locatie(obiect) == 'Vivo'

    set_id(obiect, '12345')
    set_nume(obiect, 'Penar')
    set_descriere(obiect, 'rechizite scolare')
    set_pret_achizitie(obiect, 15.89)
    set_locatie(obiect, 'Mall')

    assert get_id(obiect) == '12345'
    assert get_nume(obiect) == 'Penar'
    assert get_descriere(obiect) == 'rechizite scolare'
    assert get_pret_achizitie(obiect) == 15.89
    assert get_locatie(obiect) == 'Mall'
