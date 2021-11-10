def creeaza_obiect(id, nume, descriere, pret_achizitie, locatie):
    '''
    creeaza obiect
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret_achizitie: float
    :param locatie: string
    :return: o lista ce retine un obiect
    '''
    return{
        'id': id,
        'nume': nume,
        'descriere': descriere,
        'pret_achizitie': pret_achizitie,
        'locatie': locatie
    }

    #return[id, nume, descriere, pret_achizitie, locatie]


def get_id(obiect):
    '''
    Getter pentru id
    :param obiect: dictionar de tipul obiect
    :return: id obiect
    '''
    return obiect["id"]

    #return obiect[0]


def get_nume(obiect):
    '''
    Getter pentru nume
    :param obiect: dictionar de tipul obiect
    :return: nume obiect
    '''
    return obiect["nume"]

    #return obiect[1]


def get_descriere(obiect):
    '''
    Getter pentru descriere
    :param obiect: dictionar de tipul obiect
    :return: descriere obiect
    '''
    return obiect["descriere"]

    #return obiect[2]


def get_pret_achizitie(obiect):
    '''
    Getter pentru pre_achizitie
    :param obiect: dictionar de tipul obiect
    :return: pretul de achizitie a obiectului
    '''
    return obiect["pret_achizitie"]

    #return obiect[3]


def get_locatie(obiect):
    '''
    Getter pentru locatie
    :param obiect: dictionar de tipul obiect
    :return: locatia
    '''
    return obiect["locatie"]

    #return obiect[4]


def to_string(obiect):
    return "id: {}, nume: {}, descriere:{}, pret achizitie: {}, locatie: {} ".format(
        get_id(obiect),
        get_nume(obiect),
        get_descriere(obiect),
        get_pret_achizitie(obiect),
        get_locatie(obiect)
    )

