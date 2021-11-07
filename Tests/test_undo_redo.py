from Domain.obiect import get_descriere, get_locatie
from Logic.crud import add_obiect
from Logic.operatii import move_obiect_from_one_location_to_another, add_string_by_price
from Logic.undo_redo import do_undo, do_redo


def test_undo_redo():
    lst_obiecte = []
    undo_list = []
    redo_list = []
    lst_obiecte = add_obiect(lst_obiecte, "128", "Calculator", "electronice", 4999.90, "bist", undo_list, redo_list)
    lst_obiecte = add_obiect(lst_obiecte, "129", "Carte", "biblioteca", 14.89, "dejj", undo_list, redo_list)
    lst_obiecte = add_obiect(lst_obiecte, "124", "culegere", "de matematica", 14.99, "cluj", undo_list, redo_list)
    lst_obiecte = do_undo(undo_list, redo_list, lst_obiecte)
    assert len(lst_obiecte) == 2
    lst_obiecte = do_redo(undo_list, redo_list, lst_obiecte)
    assert len(lst_obiecte) == 3
    lst_obiecte = add_obiect(lst_obiecte, "154", "culegere", "de fizica", 12.99, "iasi", undo_list, redo_list)
    assert len(lst_obiecte) == 4
    lst_obiecte = do_undo(undo_list, redo_list, lst_obiecte)
    assert len(lst_obiecte) == 3
    lst_obiecte = do_undo(undo_list, redo_list, lst_obiecte)
    lst_obiecte = do_undo(undo_list, redo_list, lst_obiecte)
    lst_obiecte = do_undo(undo_list, redo_list, lst_obiecte)
    assert len(lst_obiecte) == 0
    lst_obiecte = do_redo(undo_list, redo_list, lst_obiecte)
    lst_obiecte = do_redo(undo_list, redo_list, lst_obiecte)
    lst_obiecte = do_redo(undo_list, redo_list, lst_obiecte)
    assert len(lst_obiecte) == 3
    lst_obiecte = move_obiect_from_one_location_to_another(lst_obiecte, 'bist', 'cluj', undo_list, redo_list)
    assert get_locatie(lst_obiecte[0]) == 'cluj'
    lst_obiecte = do_undo(undo_list, redo_list, lst_obiecte)
    assert get_locatie(lst_obiecte[0]) == 'bist'
    lst_obiecte = do_redo(undo_list, redo_list, lst_obiecte)
    assert get_locatie(lst_obiecte[0]) == 'cluj'
    lst_obiecte = add_string_by_price(lst_obiecte, 70, " - test", undo_list, redo_list)
    assert get_descriere(lst_obiecte[0]) == "electronice - test"
    lst_obiecte = do_undo(undo_list, redo_list, lst_obiecte)
    assert get_descriere(lst_obiecte[0]) == "electronice"
    lst_obiecte = do_redo(undo_list, redo_list, lst_obiecte)
    assert get_descriere(lst_obiecte[0]) == "electronice - test"
