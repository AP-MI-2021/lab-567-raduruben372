from Domain.obiect import creeaza_obiect, get_id


def add_obiect(id, nume, descriere, pret_achizitie, locatie, inventar):
    '''
    adauga un obiect in inventar
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret_achizitie: float
    :param locatie: string
    :param inventar: lista obiecte
    :return: adauga un obiect in dictionar
    '''
    if get_by_id(id, inventar) is not None:
        raise ValueError("Id-ul exista deja")
    obiect = creeaza_obiect(id, nume, descriere, pret_achizitie, locatie)
    return inventar + [obiect]


def get_by_id(id, inventar):
    '''
    gaseste un obiect cu id-ul dat in inventar
    :param id: id obiect
    :param inventar: lista obiecte
    :return: obiectul cu id-ul dat din lista sau None daca acesta nu exista
    '''

    for obiect in inventar:
        if get_id(obiect) == id:
            return obiect
    return None


def delete_obiect(id, inventar):
    '''
    sterge un obiect cu id-ul dat din inventar
    :param id: id obiect
    :param inventar: lista cu obiecte
    :return: o lista de obiecte fara obiectul cu id-ul dat
    '''
    if get_by_id(id, inventar) is None:
        raise ValueError('Nu exista un obiect cu id-ul dat!')
    return[obiect for obiect in inventar if get_id(obiect) != id]


def modify_obiect(id, nume, descriere, pret_achizitie, locatie, inventar):
    '''
    modifica obiectul cu id-ul dat
    :param id: id obiect
    :param nume: nume obiect
    :param descriere: descriere obiect
    :param pret_achizitie: pret obiect
    :param locatie: locatie obiect
    :param inventar: inventar de obiecte
    :return:
    '''
    inventar_nou = []
    for obiect in inventar:
        if get_id(obiect) == id:
            obiect_nou = creeaza_obiect(id, nume, descriere, pret_achizitie, locatie)
            inventar_nou.append(obiect_nou)
        else:
            inventar_nou.append(obiect)
    return inventar_nou
