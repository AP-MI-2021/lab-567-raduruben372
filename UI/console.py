from Domain.obiect import to_string
from Logic.CRUD import add_obiect, delete_obiect, modify_obiect


def print_menu():
    print('''
1.  Adauga obiect
2.  Sterge obiect
3.  Modifica obiect
a.  Afiseaza toate obiectele
x.  Iesire''')


def ui_add_obiect(inventar):
    id = input("Dati id-ul: ")
    nume = input("Dati numele: ")
    descriere = input("Dati descrierea: ")
    pret_achizitie = float(input('Dati pretul: '))
    locatie = input("Dati locatia: ")
    return add_obiect(id, nume, descriere, pret_achizitie, locatie, inventar)


def ui_delete_obiect(inventar):
    id = input("Dati id-ul obiectului de sters: ")
    return delete_obiect(id, inventar)


def ui_modify_obiect(inventar):
    id = input("Dati id-ul obiectului de modificat: ")
    nume = input("Dati noul nume: ")
    descriere = input("Dati noua descriere: ")
    pret_achizitie = float(input('Dati noul pret: '))
    locatie = input('Dati noua locatie :')
    return modify_obiect(id, nume, descriere, pret_achizitie, locatie, inventar)


def show_all(inventar):
    for obiect in inventar:
        print(to_string(obiect))


def run_menu(inventar):
    while True:
        print_menu()
        optiune = input('Dati optiunea: ')

        if optiune == "1":
            inventar = ui_add_obiect(inventar)
        elif optiune == "2":
            inventar = ui_delete_obiect(inventar)
        elif optiune == '3':
            inventar = ui_modify_obiect(inventar)
        elif optiune == 'a':
            show_all(inventar)
        elif optiune == "x":
            break
        else:
            print('Optiune gresita! Reincercati: ')


