from Domain.obiect import to_string
from Logic.CRUD import delete_obiect, add_obiect, get_by_id, modify_obiect


def show_all(inventar):
    for obiect in inventar:
        print(to_string(obiect))


def print_help():
    print('''
comenzile sunt separate prin ";" si prin spatiu (). ex:(add 1 Samsung Telefon 1200 C121 ; modify 1 Iphone Telefon 2200 C101)
add id nume descriere pret locatie - adauga un obiect in inventar. ex:(add 1 Samsung Telefon 1200 C121)
modify id nume descriere pret locatie - modifica un obiect din inventar. ex:(modify 1 Iphone Telefon 2200 C101)
delete id - sterge un obiect din inventar. ex:(delete 1)
showall - afiseaza toate obiectele
exit - iesire
    ''')


def ui_add(param, inventar):
    try:
        id = param[0]
        if id == "":
            raise ValueError('Id-ul trebuie sa fie nenul')
        nume = param[1]
        if nume == "":
            raise ValueError('Numele trebuie sa fie nenul')
        descriere = param[2]
        if descriere == "":
            raise ValueError('Descrierea trebuie sa fie nenula')
        pret_achizitie = float(param[3])
        if isinstance(pret_achizitie, int) is False and isinstance(pret_achizitie, float) is False:
            raise ValueError('Introduceti un numar!!')
        locatie = param[4]
        if len(locatie) != 4:
            raise ValueError('Locatia trebuie sa aiba 4 caractere!')
        return add_obiect(id, nume, descriere, pret_achizitie, locatie, inventar)
    except ValueError as ve:
        print('Eroare: ', ve)
        return inventar


def ui_delete(param, inventar):
    try:
         id = param[0]
         return delete_obiect(id, inventar)
    except ValueError as ve:
        print('Eroare: ', ve)
        return inventar


def ui_modify(param, inventar):
    try:
        id = param[0]
        if get_by_id(id, inventar) is None:
            raise ValueError("Nu exista un obiect cu id-ul dat!")
        nume = param[1]
        if nume == "":
            raise ValueError('Numele trebuie sa fie nenul!')
        descriere = param[2]
        if descriere == "":
            raise ValueError('Descrierea trebuie sa fie nenula')
        pret_achizitie = float(param[3])
        locatie = param[4]
        if len(locatie) != 4:
            raise ValueError('Locatia trebuie sa aiba 4 caractere')
        return modify_obiect(id, nume, descriere, pret_achizitie, locatie, inventar)
    except ValueError as ve:
        print('Eroare: ', ve)
        return inventar


def run_cmd_menu(inventar):
    while True:
        optiuni = input()
        comenzi = optiuni.split(";")
        try:
            for comanda in comenzi:
                comanda = comanda.split()
                if comanda[0] == 'add':
                    inventar = ui_add(comanda[1:], inventar)
                elif comanda[0] == "delete":
                    inventar = ui_delete(comanda[1:], inventar)
                elif comanda[0] == "modify":
                    inventar = ui_modify(comanda[1:], inventar)
                elif comanda[0] == "showall":
                    show_all(inventar)
                elif comanda[0] == "help":
                    print_help()
                elif comanda[0] == "exit":
                    return inventar
                else:
                    print('Optiune gresita! Tasteaza help pentru ajutor')
        except Exception as ex:
            print("Eroare: {}".format(ex))