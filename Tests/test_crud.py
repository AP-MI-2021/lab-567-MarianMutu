from Logic.crud import *


def test_add_obiect():
    obiecte = []
    obiecte = add_obiect(obiecte, '128A93', 'stilou', 'rechizite', 2.99, 'Vivo')
    assert len(obiecte) == 1
    assert get_id(obiecte[0]) == '128A93'
    assert get_nume(obiecte[0]) == 'stilou'
    assert get_descriere(obiecte[0]) == 'rechizite'
    assert get_pret_achizitie(obiecte[0]) == 2.99
    assert get_locatie(obiecte[0]) == 'Vivo'


def test_edit_obiect():
    o1 = create_obiect('128A93', 'Calculator', 'electronice', 4999.90, 'secr')
    o2 = create_obiect('12W889', 'Carte', 'biblioteca', 14.89, 'CLuj')
    obiecte = [o1, o2]
    assert len(obiecte) == 2
    obiect = edit_obiect(obiecte, '128A93', 'Carte_new', 'biblioteca_new', 13.49, 'bibl')
    o1_new = read(obiect, '128A93')
    assert get_id(o1_new) == '128A93'
    assert get_nume(o1_new) == 'Carte_new'
    assert get_descriere(o1_new) == 'biblioteca_new'
    assert get_pret_achizitie(o1_new) == 13.49
    assert get_locatie(o1_new) == "bibl"


def test_delete_obiect():
    o1 = create_obiect('128A93', 'Calculator', 'electronice', 4999.90, 'secr')
    o2 = create_obiect('12W889', 'Carte', 'biblioteca', 14.89, 'CLuj')
    obiecte = [o1, o2]
    assert len(obiecte) == 2
    obiecte = delete_obiect(obiecte, '128A93')
    assert len(obiecte) == 1
    obiecte = delete_obiect(obiecte, '12W889')
    assert len(obiecte) == 0






