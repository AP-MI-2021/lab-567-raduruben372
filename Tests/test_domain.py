from Domain.obiect import creeaza_obiect, get_id, get_nume, get_descriere, get_pret_achizitie, get_locatie


def test_obiect():
    obiect = creeaza_obiect("1", "Samsung S20", "Telefon", 2500, "C2")
    assert get_id(obiect) == "1"
    assert get_nume(obiect) == "Samsung S20"
    assert get_descriere(obiect) == "Telefon"
    assert get_pret_achizitie(obiect) == 2500
    assert get_locatie(obiect) == "C2"

