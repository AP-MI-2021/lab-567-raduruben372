from Logic.CRUD import add_obiect, get_by_id
from Logic.functionalitati import undo, redo


def test_undo_redo():
    inventar =[]
    undo_operations = []
    redo_operations = []

    # add 1
    inventar = add_obiect("1", "Samsung S10", "Telefon", 1200.0, "B121", inventar, undo_operations, redo_operations)
    assert len(inventar) == 1

    # add 2
    inventar = add_obiect("2", "Samsung S20", "Telefon", 2200.0, "B121", inventar, undo_operations, redo_operations)
    assert len(inventar) == 2

    # add 3
    inventar = add_obiect("3", "Samsung S9", "Telefon", 200.0, "B121", inventar, undo_operations, redo_operations)
    assert len(inventar) == 3

    # undo 1
    inventar = undo(inventar, undo_operations, redo_operations)
    assert len(inventar) == 2
    assert get_by_id("1", inventar) is not None
    assert get_by_id("2", inventar) is not None
    assert get_by_id("3", inventar) is None

    # undo 2
    inventar = undo(inventar, undo_operations, redo_operations)
    assert len(inventar) == 1
    assert get_by_id("1", inventar) is not None
    assert get_by_id("2", inventar) is None
    assert get_by_id("3", inventar) is None

    # undo 3
    inventar = undo(inventar, undo_operations, redo_operations)
    assert len(inventar) == 0

    # undo 4
    inventar = undo(inventar, undo_operations, redo_operations)
    assert len(inventar) == 0

    # add 3
    inventar = add_obiect("1", "Samsung S10", "Telefon", 1200.0, "B121", inventar, undo_operations, redo_operations)
    assert len(inventar) == 1

    inventar = add_obiect("2", "Samsung S20", "Telefon", 2200.0, "B121", inventar, undo_operations, redo_operations)
    assert len(inventar) == 2

    inventar = add_obiect("3", "Samsung S9", "Telefon", 200.0, "B121", inventar, undo_operations, redo_operations)
    assert len(inventar) == 3

    # redo
    inventar = redo(inventar, undo_operations, redo_operations)
    assert len(inventar) == 3
    assert get_by_id("1", inventar) is not None
    assert get_by_id("2", inventar) is not None
    assert get_by_id("3", inventar) is not None

    # undo x2
    inventar = undo(inventar, undo_operations, redo_operations)
    inventar = undo(inventar, undo_operations, redo_operations)
    assert len(inventar) == 1
    assert get_by_id("1", inventar) is not None
    assert get_by_id("2", inventar) is None
    assert get_by_id("3", inventar) is None

    # redo 1
    inventar = redo(inventar, undo_operations, redo_operations)
    assert len(inventar) == 2
    assert get_by_id("1", inventar) is not None
    assert get_by_id("2", inventar) is not None
    assert get_by_id("3", inventar) is None

    # redo 2
    inventar = redo(inventar, undo_operations, redo_operations)
    assert len(inventar) == 3
    assert get_by_id("1", inventar) is not None
    assert get_by_id("2", inventar) is not None
    assert get_by_id("3", inventar) is not None

    # undo x2
    inventar = undo(inventar, undo_operations, redo_operations)
    inventar = undo(inventar, undo_operations, redo_operations)
    assert len(inventar) == 1
    assert get_by_id("1", inventar) is not None
    assert get_by_id("2", inventar) is None
    assert get_by_id("3", inventar) is None

    # add
    inventar = add_obiect("4", "Samsung S8", "Telefon", 1200.0, "B121", inventar, undo_operations, redo_operations)
    assert len(inventar) == 2
    assert get_by_id("1", inventar) is not None
    assert get_by_id("2", inventar) is None
    assert get_by_id("3", inventar) is None
    assert get_by_id("4", inventar) is not None

    # redo
    inventar = redo(inventar, undo_operations, redo_operations)
    assert len(inventar) == 2
    assert get_by_id("1", inventar) is not None
    assert get_by_id("2", inventar) is None
    assert get_by_id("3", inventar) is None
    assert get_by_id("4", inventar) is not None

    # undo 1
    inventar = undo(inventar, undo_operations, redo_operations)
    assert len(inventar) == 1
    assert get_by_id("1", inventar) is not None
    assert get_by_id("2", inventar) is None
    assert get_by_id("3", inventar) is None
    assert get_by_id("4", inventar) is None

    # undo 2
    inventar = undo(inventar, undo_operations, redo_operations)
    assert len(inventar) == 0

    # redo x2
    inventar = redo(inventar, undo_operations, redo_operations)
    inventar = redo(inventar, undo_operations, redo_operations)
    assert len(inventar) == 2
    assert get_by_id("1", inventar) is not None
    assert get_by_id("2", inventar) is None
    assert get_by_id("3", inventar) is None
    assert get_by_id("4", inventar) is not None

    # redo
    inventar = redo(inventar, undo_operations, redo_operations)
    assert len(inventar) == 2
    assert get_by_id("1", inventar) is not None
    assert get_by_id("2", inventar) is None
    assert get_by_id("3", inventar) is None
    assert get_by_id("4", inventar) is not None
