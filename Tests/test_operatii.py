from Domain.obiect import create_obiect, get_locatie, get_descriere
from Logic.operatii import move_obiect_from_one_location_to_another, \
    add_string_by_price


def test_move_obiect_from_one_location_to_another():
    o1 = create_obiect("128A93", "Calculator", "electronice", 4999.90, "bist")
    o2 = create_obiect("12W889", "Carte", "biblioteca", 14.89, "dejj")
    o3 = create_obiect("123594", "culegere", "de matematica", 14.99, "cluj")
    lst_obiecte = [o1, o2, o3]
    lst_obiecte = move_obiect_from_one_location_to_another(lst_obiecte, "cluj", "bist")
    assert get_locatie(o1) == "bist"
    assert get_locatie(o2) == "dejj"
    assert get_locatie(o3) == "bist"
    lst_obiecte = move_obiect_from_one_location_to_another(lst_obiecte, "bist", "memo")
    assert get_locatie(o1) == "memo"
    assert get_locatie(o2) == "dejj"
    assert get_locatie(o3) == "memo"


def test_add_string_from_price():
    o1 = create_obiect("128", "Calculator", "electronice", 4999.90, "bist")
    o2 = create_obiect("129", "Carte", "biblioteca", 14.89, "dejj")
    o3 = create_obiect("124", "culegere", "de matematica", 14.99, "cluj")
    lst_obiecte = [o1, o2, o3]
    lst_obiecte = add_string_by_price(lst_obiecte, 67.89, " - altex")
    assert get_descriere(o1) == "electronice - altex"
    assert get_descriere(o2) == "biblioteca"
    assert get_descriere(o3) == "de matematica"
    lst_obiecte = add_string_by_price(lst_obiecte, 5.50, " - consumabile")
    assert get_descriere(o1) == "electronice - altex - consumabile"
    assert get_descriere(o2) == "biblioteca - consumabile"
    assert get_descriere(o3) == "de matematica - consumabile"
    lst_obiecte = add_string_by_price(lst_obiecte, 55500, " - consumabile")
    assert get_descriere(o1) == "electronice - altex - consumabile"
    assert get_descriere(o2) == "biblioteca - consumabile"
    assert get_descriere(o3) == "de matematica - consumabile"


