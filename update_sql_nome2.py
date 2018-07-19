# -*- coding: iso-8859-1 -*
import os, csv, wave, contextlib, subprocess, time, pyodbc
from shutil import copy2
from pydub import AudioSegment
from settings import list_servers_config, database_list

def update_sql_basenomeivr():
      os.system ('cls')
      src = input ("Insira o caminho onde estao os nomes: \n \n")
      #src = origem
      novonome = 0
      nomeexiste = 0
      lista_nomes_inseridos = []

      #print ('O local de origem das gravaoces é:' + origem )
      #print ('\n')


      #src = 'C:/Users/augusto.nascimento/Documents/locutores/pt_BR-lb/nome'
      print ('Lista de Servidores: \n')
      print (' --- 200.201.128.218:2020\n --- 200.201.128.218:1044\n --- 200.206.41.210:21744\n --- 200.206.41.210:22744\n --- 200.170.220.147:10130\n --- 10.100.31.70\n --- 200.201.128.218:1818\n --- 189.112.36.196:3510\n  ')
      database_dst = input ('Digite o ip do servidor BD de destino \n')
      print ('O servidor de destino é: ' + database_dst)
      print ('\n')


      database = database_list[database_dst]

      #database = database_list['189.112.36.196:3510']

      cn = pyodbc.connect(driver='{SQL Server Native Client 11.0}', server=database['server'], uid=database['uid'], pwd=database['pwd'])

      i = []
      for f in os.listdir(src):
          l = f.split("_")
          i = "('{nome}', '{locutor}')".format(nome=l[0], locutor=l[1][:2])
          sqlv = "Nome = '{nome}' and Locutor ='{locutor}'".format(nome=l[0], locutor=l[1][:2])
          sqlconsulta = """SELECT * from ovx.[dbo].[BaseNomeIVR] where {condicao}""".format(condicao=sqlv)
          sql = """INSERT INTO ovx.[dbo].[BaseNomeIVR] ([Nome],[Locutor]) VALUES {valor}""".format(valor=i)
          #sql = select * from ovx.[dbo].[BaseNomeIVR] where Nome =
          #print ('O comando sql para consulta se o nome ja esta na base eh: \n' + sqlconsulta)
          #time.sleep(4)
          resultpesquisa = cn.execute(sqlconsulta).fetchone()
          if resultpesquisa:
              #print ('\n Retorno: ' + str(resultpesquisa))
              #print ('\n')
              print ('O nome ja esta na base de dados \n')
              nomeexiste += 1

          else:
              print ('O nome sera inserido na base de dados \n')
              #print ('o comando sql que sera executado eh \n \n' + sql)
              cn.execute(sql)
              lista_nomes_inseridos.append(sql)
              novonome += 1


          #time.sleep(3)



      cn.commit()

      print ('\n Novos nomes inseridos eh --- ' + str(novonome))
      print ('\n Nomes inseridos: ' ,lista_nomes_inseridos)
      print ('\n Quantidade de nomes nao inseridos pois ja havia na base eh --- ' + str(nomeexiste))

      print ('\n Nao ha novos nomes a serem inseridos \n')
      print ('Obrigado e ate breve \n')
      #menu()
