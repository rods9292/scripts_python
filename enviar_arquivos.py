# -*- coding: iso-8859-1 -*
#suas fu��es aqui
from fabric.api import *
import tempfile, os, re, difflib,time
from fabric.contrib.files import exists, append, contains

def transfere_prompt():
    origem = input ('Qual o diretorio de origem dos prompts? \n Exemplo: \n /home/transferencia/  \n /opt/optimus/locutores/pt_BR-gs/nome \n /opt/optimus/locutores/pt_BR-gs/581_prompts_v3 \n')
    destino = input ('Qual o diretorio de destino dos prompts? \n Exemplo: \n /opt/optimus/locutores/pt_BR-gs/nome \n /opt/optimus/locutores/pt_BR-gs/581_prompts_v3 \n')
    send_prompt(origem,destino)

def send_prompt(path_origem,path_destino):
    print ('Origem: '+path_origem)
    print ('Destino: '+path_destino)
    if os.path.isdir(path_origem):
        print ('Origem: '+path_origem)
        print ('Destino: '+path_destino)
        #run('rm -rf {path}'.format(path=path))
        if not exists(path_destino):
            run('mkdir -p {path}'.format(path=path_destino))
        for file in os.listdir(path_origem):
            put(os.path.join(path_origem,file), os.path.join(path_destino,file))
