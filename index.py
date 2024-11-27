#!/usr/bin/python
# -*- coding: utf-8 -*-

#Sistema de investigação digital 1.0

import sys
import argparse

import core.search_url as search_url
import core.logo as logo
import core.colors as colors
import core.mods as mods
import Modules.wordpress as wp
import Modules.information as info
import Modules.userpass as up
import Modules.cameras as cam
import Modules.ftp as ftp

def menu_principal():
    while True:
        mods.clear_screen()
        logo.dorkify_logo()
        print(f'''
ESCOLHA UMA OPÇÃO:

    {colors.bcolors.OKBLUE}[1]{colors.bcolors.ENDC} Pesquisa no Google
    {colors.bcolors.OKBLUE}[2]{colors.bcolors.ENDC} Pesquisa em URLs
    {colors.bcolors.OKBLUE}[3]{colors.bcolors.ENDC} Pesquisar Livros
    {colors.bcolors.OKBLUE}[4]{colors.bcolors.ENDC} Baixar Músicas
    {colors.bcolors.OKBLUE}[5]{colors.bcolors.ENDC} Obter Informações
    {colors.bcolors.OKBLUE}[6]{colors.bcolors.ENDC} Pesquisar Mapas
    {colors.bcolors.OKBLUE}[7]{colors.bcolors.ENDC} Ver Previsão do Tempo
    {colors.bcolors.OKBLUE}[8]{colors.bcolors.ENDC} Pesquisar Títulos de Sites
    {colors.bcolors.OKBLUE}[09]{colors.bcolors.ENDC} Pesquisar URLs de Sites
    {colors.bcolors.OKBLUE}[10]{colors.bcolors.ENDC} Pesquisar Sites Específicos
    {colors.bcolors.OKBLUE}[11]{colors.bcolors.ENDC} Pesquisar Estoques/Ações
    {colors.bcolors.OKBLUE}[12]{colors.bcolors.ENDC} Vulnerabilidades em WordPress
    {colors.bcolors.OKBLUE}[13]{colors.bcolors.ENDC} Procurar Usuários e Senhas Vulneráveis
    {colors.bcolors.OKBLUE}[14]{colors.bcolors.ENDC} Procurar Câmeras CCTV Vulneráveis
    {colors.bcolors.OKBLUE}[15]{colors.bcolors.ENDC} Procurar Servidores FTP Abertos
    {colors.bcolors.OKBLUE}[0 ou 00]{colors.bcolors.ENDC} Sair
    ''')
        try:
            opcao = input("    --> ")
            if opcao in ['0', '00']:
                print(f"\n{colors.bcolors.OKGREEN}Saindo... Até logo!{colors.bcolors.ENDC}")
                sys.exit()
            opcao = int(opcao)
            print('\n\n')
            executar_opcao(opcao)
            input(f"{colors.bcolors.OKBLUE}Pressione Enter para continuar...{colors.bcolors.ENDC}")
        except ValueError:
            print(f"{colors.bcolors.FAIL}Opção inválida! Por favor, insira um número válido.{colors.bcolors.ENDC}")
            input(f"{colors.bcolors.OKBLUE}Pressione Enter para tentar novamente...{colors.bcolors.ENDC}")

def executar_opcao(opcao):
    if opcao == 1:  # Pesquisa no Google
        q = input('Digite sua pesquisa: ')
        print('\nRealizando pesquisa no Google...\n')
        search_url.url_search(q)

    elif opcao == 2:  # Pesquisa em URLs
        s = input('Digite os termos para buscar nas URLs dos sites: ')
        q = str('inurl:' + s)
        print('\nPesquisando URLs...\n')
        search_url.url_search(q)

    elif opcao == 3:  # Livros
        s = input('Digite o nome do livro/autor: ')
        q = str('book:' + s)
        print('\nPesquisando livros...\n')
        search_url.url_search(q)

    elif opcao == 4:  # Músicas
        s = input('Digite o nome da música/artista: ')
        q = str('?intitle:index.of?mp3 ' + s)
        print('\nPesquisando músicas...\n')
        search_url.url_search(q)

    elif opcao == 5:  # Informação
        info.information()

    elif opcao == 6:  # Mapas
        s = input('Digite o nome da cidade: ')
        q = str('maps ' + s)
        print('\nPesquisando mapas...\n')
        search_url.url_search(q)

    elif opcao == 7:  # Tempo
        s = input('Digite o nome da cidade: ')
        q = str('weather ' + s)
        print('\nPesquisando previsão do tempo...\n')
        search_url.url_search(q)

    elif opcao == 8:  # Pesquisa no título de sites
        s = input('Digite os termos para buscar no título dos sites: ')
        q = str('intitle:' + s)
        print('\nPesquisando títulos...\n')
        search_url.url_search(q)

    elif opcao == 9:  # Pesquisa em URLs de sites
        s = input('Digite os termos para buscar nas URLs dos sites: ')
        q = str('inurl:' + s)
        print('\nPesquisando URLs...\n')
        search_url.url_search(q)

    elif opcao == 10:  # Pesquisa em sites específicos
        s = input('Digite o site para pesquisar: ')
        q = str('site:' + s)
        print('\nPesquisando no site...\n')
        search_url.url_search(q)

    elif opcao == 11:  # Estoques/Ações
        s = input('Digite o nome ou ticker da empresa: ')
        q = str('stocks:' + s)
        print('\nPesquisando estoques...\n')
        search_url.url_search(q)

    elif opcao == 12:  # WordPress
        print(notice)
        yn = input('Você concorda com os termos? (S/N): ')
        if yn.lower() == 's':
            wp.wordpress()
        else:
            print('Você deve concordar com os termos.')

    elif opcao == 13:  # Usuários e Senhas
        print(notice)
        yn = input('Você concorda com os termos? (S/N): ')
        if yn.lower() == 's':
            up.userpass()
        else:
            print('Você deve concordar com os termos.')

    elif opcao == 14:  # Câmeras CCTV
        print(notice)
        yn = input('Você concorda com os termos? (S/N): ')
        if yn.lower() == 's':
            cam.cameras()
        else:
            print('Você deve concordar com os termos.')

    elif opcao == 15:  # FTP
        print(notice)
        yn = input('Você concorda com os termos? (S/N): ')
        if yn.lower() == 's':
            ftp.ftp()
        else:
            print('Você deve concordar com os termos.')

    else:
        print('Opção inválida!')


# Mensagem de aviso
notice = f'''
    {colors.bcolors.OKBLUE}Por favor, leia atentamente as informações abaixo antes de usar esta ferramenta.{colors.bcolors.ENDC}
    Esta ferramenta é apenas para fins educacionais e testes de segurança.
    O uso indevido pode ser ilegal e rastreável. Certifique-se de estar ciente disso.
'''


# Programa principal
if __name__ == "__main__":
    menu_principal()
