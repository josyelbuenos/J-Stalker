import time
import sys

import core.search_url as search_url
import core.logo as logo
import core.colors as colors
import core.mods as mods


def wordpress():

    def wp_menu():
        global ch
        mods.clear_screen()
        logo.dorkify_logo()

        print(f'''
    ESCOLHA UMA OPÇÃO:
    
        {colors.bcolors.OKBLUE}[!]{colors.bcolors.ENDC} Sites WP que estão usando o Wordfence WAF            [1]  
        {colors.bcolors.OKBLUE}[!]{colors.bcolors.ENDC} Buscar por arquivos de configuração do WP            [2]  
        {colors.bcolors.OKBLUE}[!]{colors.bcolors.ENDC} Encontrar arquivos de configuração MySQL, ABSPATH, WP [3] 
        {colors.bcolors.OKBLUE}[!]{colors.bcolors.ENDC} Procurar por arquivos database.sql de backup         [4]  
        {colors.bcolors.OKBLUE}[!]{colors.bcolors.ENDC} Informações de log de sites WP vulneráveis           [5]  
        {colors.bcolors.OKBLUE}[!]{colors.bcolors.ENDC} Log de debug em sites WP vulneráveis                 [6]  
        {colors.bcolors.OKBLUE}[!]{colors.bcolors.ENDC} Arquivos SQL dump de sites WP                        [7]  
        {colors.bcolors.OKBLUE}[!]{colors.bcolors.ENDC} Upload de Webshell. WordPress Levo-Slideshow         [8]  
        {colors.bcolors.OKBLUE}[!]{colors.bcolors.ENDC} Informações de WP para MAC OS X                      [9]  
        {colors.bcolors.OKBLUE}[!]{colors.bcolors.ENDC} Senha de banco de dados wp-config de sites WP vulneráveis [10]  
        {colors.bcolors.OKBLUE}[!]{colors.bcolors.ENDC} Encontrar arquivos wp-config.php vulneráveis         [11]  
        {colors.bcolors.OKBLUE}[!]{colors.bcolors.ENDC} Procurar por sites WP mal configurados               [12]  
        {colors.bcolors.OKBLUE}[!]{colors.bcolors.ENDC} Buscar por dados sensíveis, db em pastas públicas    [13]  
    
        ''')

        ch = int(input("    --> "))
        print('\n\n')

    wp_menu()

    if ch == 1:
        q = 'filetype:ini "wordfence"'
        print('\n Pesquisando...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 2:
        q = 'intext:DB_PASSWORD || intext:"MySQL hostname" ext:txt'
        print('\n Pesquisando...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 3:
        q = 'inurl:"-wp13.txt"'
        print('\n Pesquisando...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 4:
        q = 'inurl:"/wp-content/wpclone-temp/wpclone_backup/"'
        print('\n Pesquisando...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 5:
        q = 'inurl:log -intext:log ext:log inurl:wp-'
        print('\n Pesquisando...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 6:
        q = 'inurl:wp-content/debug.log'
        print('\n Pesquisando...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 7:
        q = 'filetype:sql intext:wp_users phpmyadmin'
        print('\n Pesquisando...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 8:
        q = 'inurl:"/wp-content/uploads/levoslideshow/"'
        print('\n Pesquisando...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 9:
        q = 'intitle:Index of /__MACOSX'
        print('\n Pesquisando...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 10:
        q = '''inurl:wp-config -intext:wp-config "'DB_PASSWORD'"'''
        print('\n Pesquisando...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 11:
        q = 'inurl:wp-admin/admin-ajax.php inurl:wp-config.php'
        print('\n Pesquisando...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 12:
        q = 'inurl:wp-admin/ intext:css/'
        print('\n Pesquisando...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 13:
        q = 'inurl:/wp-content/wpbackitup_backups'
        print('\n Pesquisando...\n')
        time.sleep(1)
        search_url.url_search(q)

    else:
        print('OPÇÃO INVÁLIDA  \n TENTE NOVAMENTE')
        sys.exit()
