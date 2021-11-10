from Domain.obiect import to_string
from Logic.CRUD import add_obiect, delete_obiect, modify_obiect, get_by_id
from Logic.functionalitati import mutare, concatenare, pret_maxim_locatie, ordonare, suma_pret_locatie, undo, redo


def print_menu():
    print('''
1.  Adauga obiect
2.  Sterge obiect
3.  Modifica obiect
4.  Mutarea tuturor obiectelor dintr-o locație în alta.
5.  Concateneaza cuvantul citit la obiectele cu pretul mai mare decat valoarea citita
6.  Determina cel mai mare pret pentru fiecare locatie
7.  Ordoneaza obiectele crescator dupa pretul de achizitie
8.  Afiseaza sumele preturilor pentru fiecare locatie
u.  Undo
r.  Redo
a.  Afiseaza toate obiectele
x.  Iesire''')


def ui_add_obiect(inventar, undo_operations, redo_operations):
    try:
        id = input("Dati id-ul: ")
        if id == "":
            raise ValueError('Id-ul trebuie sa fie nenul')
        nume = input("Dati numele: ")
        if nume == "":
            raise ValueError('Numele trebuie sa fie nenul')
        descriere = input("Dati descrierea: ")
        if descriere == "":
            raise ValueError('Descrierea trebuie sa fie nenula')
        try:
            pret_achizitie = float(input('Dati pretul: '))
            if isinstance(pret_achizitie, int) is False and isinstance(pret_achizitie, float) is False:
                raise ValueError('Introduceti un numar!!')
        except Exception:
            raise ValueError(f"Introduceti un numar real!! Pretul nu este corect!")
        locatie = input("Dati locatia: ")
        if len(locatie) != 4:
            raise ValueError('Locatia trebuie sa aiba 4 caractere!')
        rezultat = add_obiect(id, nume, descriere, pret_achizitie, locatie, inventar, undo_operations, redo_operations)
        return rezultat
    except ValueError as ve:
        print('Eroare: ', ve)
        return inventar


def ui_delete_obiect(inventar, undo_operations, redo_operations):
    try:
         id = input("Dati id-ul obiectului de sters: ")
         rezultat = delete_obiect(id, inventar, undo_operations, redo_operations)
         #obiect_sters = get_by_id(id, inventar)
         return rezultat
    except ValueError as ve:
        print('Eroare: ', ve)
        return inventar


def ui_modify_obiect(inventar, undo_operations, redo_operations):
    try:
         id = input("Dati id-ul obiectului de modificat: ")
         if get_by_id(id, inventar) is None:
             raise ValueError("Nu exista un obiect cu id-ul dat!")
         nume = input("Dati noul nume: ")
         if nume == "":
             raise ValueError('Numele trebuie sa fie nenul!')
         descriere = input("Dati noua descriere: ")
         if descriere == "":
             raise ValueError('Descrierea trebuie sa fie nenula')
         pret_achizitie = float(input('Dati noul pret: '))
         locatie = input('Dati noua locatie :')
         if len(locatie) != 4:
             raise ValueError('Locatia trebuie sa aiba 4 caractere')
         rezultat =  modify_obiect(id, nume, descriere, pret_achizitie, locatie, inventar, undo_operations, redo_operations)
         #obiect_vechi = get_by_id(id, inventar)
         return rezultat
    except ValueError as ve:
        print('Eroare: ', ve)
        return inventar


def ui_mutare(inventar):
    try:
        locatie_veche = input("Dati locatia din care sa se mute obiectele: ")
        locatie_noua = input("Dati noua locatie: ")
        if locatie_noua == "" or locatie_veche == "":
            raise ValueError('Locatia trebuie sa fie nenula')
        return mutare(locatie_veche, locatie_noua, inventar)
    except ValueError as ve:
        print('Eroare: ', ve)
        return inventar


def ui_concatenare(inventar):
    try:
        cuvant = input('Dati cuvantul: ')
        if cuvant == "":
            raise ValueError('Cuvantul trebuie sa fie nenul')
        valoare = float(input('Dati o valoare: '))
        return concatenare(cuvant, valoare, inventar)
    except ValueError as ve:
        print("Eroare", ve)
        return inventar


def ui_pret_maxim_locatie(inventar):
    rezultat = pret_maxim_locatie(inventar)
    for locatie in rezultat:
        print(f"Locatia : {locatie} are pretul maxim {rezultat[locatie]}")


def ui_ordonare(inventar):
    show_all(ordonare(inventar))


def show_all(inventar):
    for obiect in inventar:
         print(to_string(obiect))


def ui_suma_pret_locatie(inventar):
    rezultat = suma_pret_locatie(inventar)
    for locatie in rezultat:
        print(f"Locatia {locatie} are suma preturilor {rezultat[locatie]}")


def run_menu(inventar):
    undo_operations = []
    redo_operations = []
    while True:
        print_menu()
        optiune = input('Dati optiunea: ')

        if optiune == "1":
            inventar = ui_add_obiect(inventar, undo_operations, redo_operations)
        elif optiune == "2":
            inventar = ui_delete_obiect(inventar, undo_operations, redo_operations)
        elif optiune == '3':
            inventar = ui_modify_obiect(inventar, undo_operations, redo_operations)
        elif optiune == "4":
            inventar = ui_mutare(inventar)
        elif optiune == "5":
            inventar = ui_concatenare(inventar)
        elif optiune == "6":
            ui_pret_maxim_locatie(inventar)
        elif optiune == "7":
            ui_ordonare(inventar)
        elif optiune == "8":
            ui_suma_pret_locatie(inventar)
        elif optiune.lower() == "u":
            if len(undo_operations) == 0:
                print('Nu se poate face undo!')
            inventar = undo(inventar, undo_operations, redo_operations)
        elif optiune.lower() == "r":
            if len(redo_operations) == 0:
                print('Nu se poate face redo!')
            inventar = redo(inventar, undo_operations, redo_operations)
        elif optiune == 'a':
            show_all(inventar)
        elif optiune == "x":
            break
        else:
            print('Optiune gresita! Reincercati: ')
