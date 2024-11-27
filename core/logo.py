#!/usr/bin/python
# -*- coding: utf-8 -*-
import core.colors as colors
import core.mods as mods
from foxcolor import *
import time


def dorkify_logo():
    mods.clear_screen()
    print(f''' {colors.bcolors.WARNING}
    ╦   ╔═╗╔╦╗╔═╗╦  ╦╔═╔═╗╦═╗
    ║───╚═╗ ║ ╠═╣║  ╠╩╗║╣ ╠╦╝
   ╚╝   ╚═╝ ╩ ╩ ╩╩═╝╩ ╩╚═╝╩╚═
            {Cores.vermelho}v1.0{Cores.incolor}''')

    print(f'''    {Cores.verde}╔╦════════• •✠•❀•✠ • •════════╦╗{Cores.incolor}'''); {time.sleep(0.5)}
    print(Cores.vermelho + "    AUTOR:" + Cores.amarelo + "Josyel Buenos"); {time.sleep(0.5)}
    print(Cores.vermelho + "    Instagram:" + Cores.amarelo + "instagram.com/josyelbuenos");time.sleep(0.5)
    print(Cores.vermelho + "    SITE:" + Cores.amarelo + "www.josyel-buenos.vercel.app");time.sleep(0.5)
    print(Cores.vermelho + "    GITHUB:" + Cores.amarelo + "github.com/josyelbuenos" + Cores.incolor)
    print(f'''    {Cores.verde}╚╩════════• •✠•❀•✠ • •════════╩╝''' + Cores.incolor)
    print(f'''{colors.bcolors.NOTICE}Esta ferramenta é apenas para fins educacionais e o criador não é responsável por nenhuma
ação realizada pelos usuários!{colors.bcolors.ENDC}''')


