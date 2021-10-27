from Tests.test_CRUD import test_add_obiect, test_delete_obiect, test_modify_obiect, test_get_by_id
from Tests.test_domain import test_obiect


def run_all_test():
    test_obiect()
    test_get_by_id()
    test_add_obiect()
    test_delete_obiect()
    test_modify_obiect()