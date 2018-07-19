# -*- coding: iso-8859-1 -*
import os, csv, contextlib, subprocess, time, pyodbc
from shutil import copy2
from sys import exit
from settings import list_servers_config, database_list
from criar_ambiente_sistema import *
from criar_agente_virtual import *
from enviar_arquivos import *
from update_sql_nome2 import *

#print ('DEPLOY PROJETO BD \n \n  Script para criar as configurações do projeto no banco de dados. \n \n Escolha uma opção abaixo: \n ')
os.system ('cls')
separador = ('===' * 50)
print ('\n   TRESTTO \n ')
print (separador)
print ('\n   Escolha uma opção abaixo: \n ')
print (separador)
print ( " 1 - Criar tabelas no Banco de Dados \n 2 - Configurar Agente Virtual \n 3 - Criar Query Substatus \n 4 - Enviar PROMPTS \n 5 - Inserir nomes no banco de dados \n 6 - Capturar Log Chamada \n \n 9 - Fechar Script \n")
print (separador)
opcao = input ('Opcao = ')
opcao_list = ['1','2','3','4','5','6','9']
while opcao not in opcao_list:
    print ('Opcao invalida')
    time.sleep(1.5)
    os.system ('cls')
    print (' \n \n Escolha uma opção abaixo: \n ')
    print (separador)
    print ( " 1 - Criar tabelas no Banco de Dados \n 2 - Configurar Agente Virtual \n 3 - Criar Query Substatus \n 4 - Enviar PROMPTS \n 5 - Inserir nomes no banco de dados \n 6 - Capturar Log Chamada \n \n 9 - Fechar Script \n")
    print (separador)
    opcao = input ('Opcao = ')
else:
    if opcao == '1':
        criar_bd()
    elif opcao == '2':
        criar_agente()
    elif opcao == '3':
        #criar_substatus()
        print ('Essa opcao ainda esta em desenvolvimento \n')
        print ('Foi mal pelo vacilo!')
    elif opcao == '4':
        transfere_prompt()
    elif opcao == '5':
        update_sql_basenomeivr()
    elif opcao == '6':
        print ('Essa opcao ainda esta em desenvolvimento \n')
        print ('Foi mal pelo vacilo!')
    elif opcao == '9':
        print ("Obrigado por utilizar esse script!!")
        exit()
