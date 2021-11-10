from Domain.obiect import get_locatie, get_descriere, get_id, to_string
from Logic.CRUD import add_obiect, get_by_id, delete_obiect
from Logic.functionalitati import mutare, concatenare, pret_maxim_locatie, suma_pret_locatie, ordonare


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
    inventar = add_obiect("4", "Samsung S21", "Tel", 3200, "C121", inventar)
    inventar = add_obiect("5", "Samsung S21", "Tel", 3200, "D421", inventar)

    rezultat = pret_maxim_locatie(inventar)
    assert rezultat["B121"] == 1200
    assert rezultat["C121"] == 3800
    assert rezultat["D421"] == 3200


def test_ordonare():
    inventar = []
    inventar = add_obiect("1", "Samsung S10", "Telefon", 1200, "B121", inventar)
    inventar = add_obiect("2", "Samsung S20", "Telefon", 200, "B121", inventar)
    inventar = add_obiect("3", "Samsung S21", "Tel", 3800, "C121", inventar)

    rezultat = ordonare(inventar)

    assert get_id(rezultat[0]) == "2"
    assert get_id(rezultat[1]) == "1"
    assert get_id(rezultat[2]) == "3"


def test_suma_pret_locatie():
    inventar =[]
    inventar = add_obiect("1", "Samsung S10", "Telefon", 1200.0, "B121", inventar)
    inventar = add_obiect("2", "Samsung S20", "Telefon", 200.0, "B121", inventar)
    inventar = add_obiect("3", "Samsung S21", "Tel", 3800.0, "C121", inventar)
    inventar = add_obiect("4", "Samsung S21", "Tel", 3200.0, "C121", inventar)
    inventar = add_obiect("5", "Samsung S21", "Tel", 3200.0, "D421", inventar)

    rezultat = suma_pret_locatie(inventar)

    assert len(rezultat) == 3
    assert rezultat["C121"] == 7000.0
    assert rezultat["B121"] == 1400.0
    assert rezultat["D421"] == 3200.0

