import sys
import time

import core.search_url as search_url
import core.logo as logo
import core.colors as colors
import core.mods as mods


def ftp():
    def ftp_menu():
        global ch
        mods.clear_screen()
        logo.dorkify_logo()

        print(f'''
    ESCOLHA UMA OPÇÃO:

        {colors.bcolors.OKBLUE}[+]{colors.bcolors.ENDC} Detectar sites FTP vulneráveis                [1]  
        {colors.bcolors.OKBLUE}[+]{colors.bcolors.ENDC} Encontrar possíveis arquivos de log em FTP    [2]  
        {colors.bcolors.OKBLUE}[+]{colors.bcolors.ENDC} Encontrar servidores FTP abertos              [3]  
        {colors.bcolors.OKBLUE}[+]{colors.bcolors.ENDC} Encontrar pastas administrativas em FTP       [4]  

        ''')

        ch = int(input("    --> "))
        print('\n\n')

    ftp_menu()

    if ch == 1:
        q = 'inurl:ftp://ftp'
        print('\n Pesquisando...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 2:
        q = '"index of" /ftp/logs'
        print('\n Pesquisando...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 3:
        q = 'intitle:"index of" inurl:ftp'
        print('\n Pesquisando...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 4:
        q = 'intitle:"index of" inurl:ftp intext:admin'
        print('\n Pesquisando...\n')
        time.sleep(1)
        search_url.url_search(q)

    else:
        print('OPÇÃO INVÁLIDA  \n TENTE NOVAMENTE')
        sys.exit()
