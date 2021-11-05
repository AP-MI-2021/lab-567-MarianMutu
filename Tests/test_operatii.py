from Logic.operatii import *


def test_move_obiect_from_one_location_to_another():
    undo_list = []
    redo_list = []
    o1 = create_obiect("128A93", "Calculator", "electronice", 4999.90, "bist")
    o2 = create_obiect("12W889", "Carte", "biblioteca", 14.89, "dejj")
    o3 = create_obiect("123594", "culegere", "de matematica", 14.99, "cluj")
    lst_obiecte = [o1, o2, o3]
    lst_obiecte = move_obiect_from_one_location_to_another(lst_obiecte, "cluj", "bist", undo_list, redo_list)
    assert get_locatie(o1) == "bist"
    assert get_locatie(o2) == "dejj"
    assert get_locatie(o3) == "bist"
    lst_obiecte = move_obiect_from_one_location_to_another(lst_obiecte, "bist", "memo", undo_list, redo_list)
    assert get_locatie(o1) == "memo"
    assert get_locatie(o2) == "dejj"
    assert get_locatie(o3) == "memo"


def test_add_string_from_price():
    undo_list = []
    redo_list = []
    o1 = create_obiect("128", "Calculator", "electronice", 4999.90, "bist")
    o2 = create_obiect("129", "Carte", "biblioteca", 14.89, "dejj")
    o3 = create_obiect("124", "culegere", "de matematica", 14.99, "cluj")
    lst_obiecte = [o1, o2, o3]
    lst_obiecte = add_string_by_price(lst_obiecte, 67.89, " - altex", undo_list, redo_list)
    assert get_descriere(o1) == "electronice - altex"
    assert get_descriere(o2) == "biblioteca"
    assert get_descriere(o3) == "de matematica"
    lst_obiecte = add_string_by_price(lst_obiecte, 5.50, " - consumabile", undo_list, redo_list)
    assert get_descriere(o1) == "electronice - altex - consumabile"
    assert get_descriere(o2) == "biblioteca - consumabile"
    assert get_descriere(o3) == "de matematica - consumabile"
    lst_obiecte = add_string_by_price(lst_obiecte, 55500, " - consumabile", undo_list, redo_list)
    assert get_descriere(o1) == "electronice - altex - consumabile"
    assert get_descriere(o2) == "biblioteca - consumabile"
    assert get_descriere(o3) == "de matematica - consumabile"


def test_biggest_price_for_each_location():
    o1 = create_obiect("128", "Calculator", "electronice", 14.90, "bist")
    o2 = create_obiect("129", "Carte", "biblioteca", 4999.90, "bist")
    o3 = create_obiect("137", "caiet", "de absente", 26.99, "bist")
    o4 = create_obiect("124", "culegere", "de matematica", 14.99, "cluj")
    o5 = create_obiect("127", "caiet", "de prezenta", 86.99, "iasi")
    o6 = create_obiect("125", "culegere", "de fizica", 82.99, "iasi")
    lst_obiecte = [o1, o2, o3, o4, o5, o6]
    assert biggest_price_for_each_location(lst_obiecte) == {'bist': 4999.90, 'cluj': 14.99, 'iasi': 86.99}


def test_ordered_items_ascending_by_price():
    o1 = create_obiect("138", "Calculator", "electronice", 14.90, "bist")
    o2 = create_obiect("139", "Carte", "biblioteca", 4999.90, "bist")
    o3 = create_obiect("137", "caiet", "de absente", 26.99, "bist")
    o4 = create_obiect("134", "culegere", "de matematica", 14.99, "cluj")
    o5 = create_obiect("137", "caiet", "de prezenta", 86.99, "iasi")
    o6 = create_obiect("135", "culegere", "de fizica", 82.99, "iasi")
    lst_obiecte = [o1, o2, o3, o4, o5, o6]
    sorted_list = ordered_items_ascending_by_price(lst_obiecte)
    assert sorted_list[0] == o1
    assert sorted_list[1] == o4
    assert sorted_list[2] == o3
    assert sorted_list[3] == o6
    assert sorted_list[4] == o5
    assert sorted_list[5] == o2


def test_sum_of_prices_for_each_locations():
    o1 = create_obiect("148", "Calculator", "electronice", 14.90, "bist")
    o2 = create_obiect("144", "culegere", "de matematica", 14.99, "cluj")
    o3 = create_obiect("147", "caiet", "de prezenta", 86.99, "iasi")
    o4 = create_obiect("149", "Carte", "biblioteca", 4999.90, "bist")
    o5 = create_obiect("145", "culegere", "de fizica", 82.99, "iasi")
    o6 = create_obiect("147", "caiet", "de absente", 36.99, "bist")
    lst_obiecte = [o1, o2, o3, o4, o5, o6]
    assert sum_of_prices_for_each_locations(lst_obiecte) == {'bist': 5051.9, 'cluj': 14.99, 'iasi': 169.99}
