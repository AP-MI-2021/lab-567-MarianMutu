from Tests.domain_tests import obiect_test
from Tests.test_crud import *
from Tests.test_operatii import test_move_obiect_from_one_location_to_another, \
    test_add_string_from_price


def run_all_tests():
    test_add_obiect()
    obiect_test()
    test_edit_obiect()
    test_delete_obiect()
    test_move_obiect_from_one_location_to_another()
    test_add_string_from_price()