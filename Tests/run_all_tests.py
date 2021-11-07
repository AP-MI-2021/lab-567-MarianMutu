from Tests.domain_tests import obiect_test
from Tests.test_crud import *
from Tests.test_operatii import *
from Tests.test_undo_redo import test_undo_redo


def run_all_tests():
    test_add_obiect()
    obiect_test()
    test_edit_obiect()
    test_delete_obiect()
    test_move_obiect_from_one_location_to_another()
    test_add_string_from_price()
    test_biggest_price_for_each_location()
    test_ordered_items_ascending_by_price()
    test_sum_of_prices_for_each_locations()
    test_undo_redo()