from Tests.test_CRUD import test_get_by_id, test_add_obiect, test_delete_obiect, test_modify_obiect
from Tests.test_domain import test_obiect
from Tests.test_functionalitati import test_mutare, test_concatenare, test_pret_maxim_locatie, test_suma_pret_locatie, \
    test_ordonare
from Tests.test_undo_redo import test_undo_redo


def run_all_test():
    test_obiect()
    test_get_by_id()
    test_add_obiect()
    test_delete_obiect()
    test_modify_obiect()
    test_mutare()
    test_concatenare()
    test_pret_maxim_locatie()
    test_suma_pret_locatie()
    test_ordonare()
    test_undo_redo()