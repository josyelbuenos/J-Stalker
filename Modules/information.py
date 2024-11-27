import sys

import core.search_url as search_url
import core.logo as logo
import core.colors as colors
import core.mods as mods

def information():
    def information_menu():
        global ch5
        mods.clear_screen()
        logo.dorkify_logo()
        print(f'''
    ESCOLHA UMA OPÇÃO:
    
        {colors.bcolors.OKBLUE}[+]{colors.bcolors.ENDC} Definição    [1]
        {colors.bcolors.OKBLUE}[+]{colors.bcolors.ENDC} Informações  [2]
        {colors.bcolors.OKBLUE}[+]{colors.bcolors.ENDC} Ações        [3]
        {colors.bcolors.OKBLUE}[+]{colors.bcolors.ENDC} Mapas        [4]
        {colors.bcolors.OKBLUE}[+]{colors.bcolors.ENDC} Clima        [5]
    
        ''')

        ch5 = int(input("    --> "))
        print('\n\n')

    information_menu()

    if ch5 == 1:
        s = input('BUSCAR DEFINIÇÃO: ')
        q = str('define:' + s)
        print('\nPesquisando... \n')
        search_url.url_search(q)

    elif ch5 == 2:
        s = input('BUSCAR: ')
        q = str('info:' + s)
        print('\nColetando informações... \n')
        search_url.url_search(q)

    elif ch5 == 3:
        s = input('BUSCAR EMPRESA COM CÓDIGO DE AÇÕES: ')
        q = str('stocks:' + s)
        print('\nPesquisando ações... \n')
        search_url.url_search(q)

    elif ch5 == 4:
        s = input('BUSCAR CIDADE: ')
        q = str('maps:' + s)
        print('\nLocalizando mapas... \n')
        search_url.url_search(q)

    elif ch5 == 5:
        s = input('INSERIR NOME DA CIDADE: ')
        q = str('weather:' + s)
        print('\nVerificando clima... \n')
        search_url.url_search(q)

    else:
        print('OPÇÃO INVÁLIDA  \n TENTE NOVAMENTE')
        sys.exit()