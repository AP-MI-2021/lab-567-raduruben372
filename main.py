from Tests.test_all import run_all_test
from UI.command_line_console import run_cmd_menu
from UI.console import run_menu


def main():
    run_all_test()
    inventar = []
    while True:
        print('''
1.  Meniu vechi
2.  Meniu tip cmd
x.  Exit
        ''')
        optiune = input('Dati optiunea: ')
        if optiune == "1":
            run_menu(inventar)
        elif optiune == "2":
            run_cmd_menu(inventar)
        elif optiune == "x":
            break
        else:
            print('Optiune gresita ! Reincercati!')

main()