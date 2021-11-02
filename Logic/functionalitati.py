from Domain.obiect import creeaza_obiect, get_locatie, get_id, get_nume, get_descriere, get_pret_achizitie


def mutare(locatie_veche, locatie_noua, inventar):
    '''
    Muta obiectele dintr-o anumita locatie in alta
    :param locatie_veche: locatie veche
    :param locatie_noua: locatie noua
    :param inventar: inventar cu obiecte
    :return: inventar modificat
    '''
    inventar_nou = []
    for obiect in inventar:
        if get_locatie(obiect) == locatie_veche:
            obiect_nou = creeaza_obiect(
                get_id(obiect),
                get_nume(obiect),
                get_descriere(obiect),
                get_pret_achizitie(obiect),
                locatie_noua
            )
            inventar_nou.append(obiect_nou)
        else:
            inventar_nou.append(obiect)
    return inventar_nou


def concatenare(cuvant, valoare, inventar):
    '''
    Concateneaza un string citit la toate obiectele cu pretul mai mare decat o valoare citita
    :param cuvant: cuvant concatenare
    :param valoare: valoare citita
    :param inventar: invetar cu obiecte
    :return: inventar nou in care descrierea obiectelor cu pretul mai mare decat valoarea citita este modificata
    '''

    inventar_nou = []
    for obiect in  inventar:
        if get_pret_achizitie(obiect) > valoare:
            obiect_nou = creeaza_obiect(
                get_id(obiect),
                get_nume(obiect),
                get_descriere(obiect) + cuvant,
                get_pret_achizitie(obiect),
                get_locatie(obiect)
            )
            inventar_nou.append(obiect_nou)
        else:
            inventar_nou.append(obiect)
    return inventar_nou