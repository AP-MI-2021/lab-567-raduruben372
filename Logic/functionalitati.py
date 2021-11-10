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


def pret_maxim_locatie(inventar):
    '''
    Determina cel mai mare pret pentru fiecare locatie
    :param inventar: inventar cu obiecte
    :return: rezultat cu preturi
    '''
    rezultat = {}
    for obiect in inventar:
        pret = get_pret_achizitie(obiect)
        locatie = get_locatie(obiect)
        if locatie in rezultat:
            if pret > rezultat[locatie]:
                rezultat[locatie] = pret
        else:
            rezultat[locatie] = pret
    return rezultat


def ordonare(inventar):
    '''
    Ordoneaza obiectele crescator dupa pretul de achizitie
    :param inventar: inventar cu obiecte
    :return: inventar nou ordonat
    '''
    return sorted(inventar, key=lambda obiect: float(get_pret_achizitie(obiect)))


def suma_pret_locatie(inventar):
    '''
    Afiseaza sumele preturilor pentru fiecare locatie
    :param inventar: inventar cu obiecte
    :return: rezultat cu sume
    '''
    rezultat = {}
    for obiect in inventar:
        locatie = get_locatie(obiect)
        pret = float(get_pret_achizitie(obiect))
        if locatie in rezultat:
            rezultat[locatie] += pret
        else:
            rezultat[locatie] = pret
    return rezultat


def undo(inventar, undo_operations, redo_operations):
    if len(undo_operations) > 0:
        redo_operations.append(inventar)
        return undo_operations.pop()
    return inventar


def redo(inventar, undo_operations, redo_operations):
    if len(redo_operations) > 0:
        undo_operations.append(inventar)
        return redo_operations.pop()
    return inventar