#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import core.colors as colors
from foxcolor import *

def url_search(q):
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    query = q.replace(' ', '+')
    URL = f"https://www.google.com/search?q={query}"
    headers = {"user-agent": USER_AGENT}
    
    # Enviar a requisição
    res = requests.get(URL, headers=headers)

    # Verificar o status da resposta
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, "html.parser")
        links = []
        titles = []
        
        # Atualizar a lógica de scraping para novos padrões
        for result in soup.select("div.tF2Cxc"):
            # Encontrar o link
            link_tag = result.select_one("a")
            # Encontrar o título
            title_tag = result.select_one("h3")
            
            if link_tag and title_tag:
                links.append(link_tag["href"])
                titles.append(title_tag.text)

        # Combinar os links e títulos e exibir os resultados
        if links and titles:
            dorks = dict(zip(links, titles))
            for link, title in dorks.items():
                print(f'{colors.bcolors.LOGGING}[*]{colors.bcolors.ENDC}  {link}  -  {colors.bcolors.HEADER}{title}{colors.bcolors.ENDC}')
        else:
            print(f'{Cores.vermelho}[404]{colors.bcolors.BOLD} Vixe, não foram econtrado nenhum resultado :({colors.bcolors.ENDC}')
    else:
        print(f'{colors.bcolors.FAIL}Falha ao se conectar com o Google. Código de erro: {res.status_code}{colors.bcolors.ENDC}')
