from Domain.obiect import creeaza_obiect, get_locatie, get_descriere
from Logic.CRUD import add_obiect, get_by_id
from Logic.functionalitati import mutare, concatenare, pret_maxim_locatie


def test_mutare():
    inventar = []
    inventar = add_obiect("1", "Samsung S20", "Telefon", 2500, "C210", inventar)
    inventar = add_obiect("2", "Samsung S21", "Telefon", 1500, "C300", inventar)
    inventar = add_obiect("3", "Samsung S9", "Telefon", 500, "C300", inventar)

    inventar =mutare("C300", "C400", inventar)

    assert len(inventar) == 3
    assert get_locatie(get_by_id("1", inventar)) == "C210"
    assert get_locatie(get_by_id("2", inventar)) == "C400"
    assert get_locatie(get_by_id("3", inventar)) == "C400"


def test_concatenare():
    inventar = []
    inventar = add_obiect("1", "Samsung S10", "Telefon", 1200, "B121", inventar)
    inventar = add_obiect("2", "Samsung S20", "Telefon", 200, "B121", inventar)
    inventar = add_obiect("3", "Samsung S21", "Tel", 3200, "B121", inventar)

    inventar = concatenare("Scump", 1000, inventar)

    assert len(inventar) == 3
    assert get_descriere(get_by_id("1", inventar)) == "TelefonScump"
    assert get_descriere(get_by_id("2", inventar)) == "Telefon"
    assert get_descriere(get_by_id("3", inventar)) == "TelScump"


def test_pret_maxim_locatie():
    inventar = []
    inventar = add_obiect("1", "Samsung S10", "Telefon", 1200, "B121", inventar)
    inventar = add_obiect("2", "Samsung S20", "Telefon", 200, "B121", inventar)
    inventar = add_obiect("3", "Samsung S21", "Tel", 3800, "C121", inventar)
    inventar = add_obiect("3", "Samsung S21", "Tel", 3200, "C121", inventar)
    inventar = add_obiect("3", "Samsung S21", "Tel", 3200, "D421", inventar)

    rezultat = pret_maxim_locatie(inventar)
    assert rezultat["B121"] == 1200
    assert rezultat["C121"] == 3800
    assert rezultat["D421"] == 3200