from Tests.domain_tests import obiect_test
from Tests.test_crud import *


def run_all_tests():
    test_add_obiect()
    obiect_test()
    test_edit_obiect()
    test_delete_obiect()
