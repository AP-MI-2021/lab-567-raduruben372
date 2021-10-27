from Domain.obiect import get_id, get_nume, get_descriere, get_locatie, get_pret_achizitie
from Logic.CRUD import add_obiect, get_by_id, delete_obiect, modify_obiect


def test_get_by_id():
    inventar = []
    inventar = add_obiect("1", "Samsung S20", "Telefon", 2500, "C2", inventar)
    inventar = add_obiect("2", "Samsung S21", "Telefon", 1500, "C3", inventar)
    inventar = add_obiect("3", "Samsung S9", "Telefon", 500, "C4", inventar)

    obiect = get_by_id("1", inventar)
    assert get_id(obiect) == "1"
    assert get_nume(obiect) == "Samsung S20"
    assert get_descriere(obiect) == "Telefon"
    assert get_pret_achizitie(obiect) == 2500
    assert get_locatie(obiect) == "C2"

    obiect = get_by_id("2", inventar)
    assert get_id(obiect) == "2"
    assert get_nume(obiect) == "Samsung S21"
    assert get_descriere(obiect) == "Telefon"
    assert get_pret_achizitie(obiect) == 1500
    assert get_locatie(obiect) == "C3"

    obiect = get_by_id("3", inventar)
    assert get_id(obiect) == "3"
    assert get_nume(obiect) == "Samsung S9"
    assert get_descriere(obiect) == "Telefon"
    assert get_pret_achizitie(obiect) == 500
    assert get_locatie(obiect) == "C4"

    assert get_by_id("4", inventar) is None
    assert get_by_id("5", inventar) is None


def test_add_obiect():
    inventar = []
    inventar = add_obiect("1", "Samsung S20", "Telefon", 2500, "C2", inventar)

    assert len(inventar) == 1
    assert get_id(get_by_id("1", inventar)) == "1"
    assert get_nume(get_by_id("1", inventar)) == "Samsung S20"
    assert get_descriere(get_by_id("1", inventar)) == "Telefon"
    assert get_pret_achizitie(get_by_id("1", inventar)) == 2500
    assert get_locatie(get_by_id("1", inventar)) == "C2"


def test_delete_obiect():
    inventar = []
    inventar = add_obiect("1", "Samsung S20", "Telefon", 2500, "C2", inventar)
    inventar = add_obiect("2", "Iphone 13", "Telefon", 6500, "C2", inventar)

    inventar = delete_obiect("1", inventar)

    assert len(inventar) == 1
    assert get_by_id("1", inventar) is None
    assert get_by_id("2", inventar) is not None

    inventar = delete_obiect("3", inventar)

    assert len(inventar) == 1
    assert get_by_id("2", inventar) is not None


def test_modify_obiect():
    inventar = []
    inventar = add_obiect("1", "Samsung S20", "Telefon", 2500, "C2", inventar)
    inventar = add_obiect("2", "Iphone 13", "Telefon", 6500, "C2", inventar)

    inventar = modify_obiect("1", "Samsung S10", "Telefon", 1400, "C3", inventar)

    new_obiect = get_by_id("1", inventar)
    assert get_id(new_obiect) == "1"
    assert get_nume(new_obiect) == "Samsung S10"
    assert get_descriere(new_obiect) == "Telefon"
    assert get_pret_achizitie(new_obiect) == 1400
    assert get_locatie(new_obiect) == "C3"

    base_obiect = get_by_id("2", inventar)
    assert get_id(base_obiect) == "2"
    assert get_nume(base_obiect) == "Iphone 13"
    assert get_descriere(base_obiect) == "Telefon"
    assert get_pret_achizitie(base_obiect) == 6500
    assert get_locatie(base_obiect) == "C2"

    inventar = []
    inventar = add_obiect("1", "Samsung S20", "Telefon", 2500, "C2", inventar)

    inventar = modify_obiect("3", "Samsung S9", "Telefon", 1500, "C6", inventar)
    base_obiect = get_by_id("1", inventar)
    assert get_id(base_obiect) == "1"
    assert get_nume(base_obiect) == "Samsung S20"
    assert get_descriere(base_obiect) == "Telefon"
    assert get_pret_achizitie(base_obiect) == 2500
    assert get_locatie(base_obiect) == "C2"
