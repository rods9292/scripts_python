# -*- coding: iso-8859-1 -*
import os, csv, wave, contextlib, subprocess, time, pyodbc
from shutil import copy2
from pydub import AudioSegment
from settings import list_servers_config, database_list
from datetime import datetime, date
from valida_dados import *

def criar_bd():
    os.system ('cls')
    DIAS = ('Segunda','Terça','Quarta','Quinta','Sexta','Sabado','Domingo')
    hoje = date.today()
    dia_atual = DIAS[hoje.weekday()]

    print ('============> SCRIPT PARA CRIAÇÃO DAS TABELAS NECESSARIAS PARA O PROJETO <============ \n'.center(100))
    print ('============> TABELA CAMPANHA <============ \n'.center(100))
    #now = datetime.now()
#print (now.hour,':',now.minute)
#now_hora = now.hour
#now_dia = now.day
#print (now.day)
#if now_hora  <= int('12'):
#    print ('Antes do meio dia')
#else:
#    print ('depois do meio dia')

    num_projeto = input ("Qual o numero do projeto: \n ")
    projeto_valido = valida_projeto(num_projeto)
    while projeto_valido != '1':
        num_projeto = input ("Qual o numero do projeto com 3 caracteres: \n")
        projeto_valido = valida_projeto(num_projeto)
        if projeto_valido == '1':
            break
    else:
        print ('Numero do projeto correto')

    nome_cliente = input ("Qual o nome do cliente: \n ")
    nome_projeto = input ("Qual o nome do projeto: \n ")
    layout_mailing = input("Qual o layout do mailing para esse projeto: \n  --- VIRTUS = 7  \n  --- VIRTUS_NEXT = 9 \n  --- SYSTEM_INTERACT = 1 \n ")
    layout_valido = valida_mailing(layout_mailing)
    while layout_valido != '1':
        layout_mailing = input ("Qual o Layout do mailing: \n  --- VIRTUS = 7  \n--- VIRTUS_NEXT = 9 \n--- SYSTEM_INTERACT = 1 \n")
        layout_valido = valida_mailing(layout_mailing)
        #print (horario_valido)
        if layout_valido == '1':
            break
    else:
        print ('Layout correto')

#  ======= VALIDA HORARIO SEMANA ===============

    hora_inicio_s = input("Qual o horario de inicio durante a semana: \n")
    horario_valido_i = valida_horario(hora_inicio_s)
    while horario_valido_i != '1':
        hora_inicio_s = input ("Digite o horario de inicio durante a semana igual o exemplo: 08:00 \n")
        horario_valido_i = valida_horario(hora_inicio_s)
        #print (horario_valido)
        if horario_valido_i == '1':
            print ('Horario valido')
            break
        elif horario_valido_i == '2':
            confirma = input ('O horario inserido esta vazio, para permanecer assim digite 1 caso queira inserir um novo horario digite 2: \n')
            if confirma == '1':
                print ('Horario em branco')
                break
            elif confirma =='2':
                hora_inicio_s = input ("Digite o horario de inicio durante a semana igual o exemplo: 08:00 \n")
                horario_valido_i = valida_horario(hora_inicio_s)
        else:
            print ('Horario correto')


    hora_termino_s = input("Qual o horario de termino durante a semana: \n")
    horario_valido_t = valida_horario(hora_termino_s)
    while horario_valido_t != '1':
        hora_termino_s = input ("Digite o horario de inicio durante a semana igual o exemplo: 18:00 \n")
        horario_valido_t = valida_horario(hora_termino_s)
        #print (horario_valido)
        if horario_valido_t == '1':
            print ('Horario valido')
            break
        elif horario_valido_t == '2':
            confirma = input ('O horario inserido esta vazio, para permanecer assim digite 1 caso queira inserir um novo horario digite 2: \n')
            if confirma == '1':
                print ('Horario em branco')
                break
            elif confirma =='2':
                hora_termino_s = input ("Digite o horario de inicio durante a semana igual o exemplo: 18:00 \n")
                horario_valido_t = valida_horario(hora_termino_s)
    else:
        print ('Horario correto')

#  ======= VALIDA HORARIO FINAL SEMANA ===============
    hora_inicio_fs = input("Qual o horario de inicio no final de semana: \n")
    horario_valido_fsi = valida_horario(hora_inicio_fs)
    while horario_valido_fsi != '1':
        hora_inicio_fs = input ("Digite o horario de inicio durante o final de semana igual o exemplo: 08:00 \n")
        horario_valido_fsi = valida_horario(hora_inicio_fs)
        #print (horario_valido)
        if horario_valido_fsi == '1':
            print ('Horario valido')
            break
        elif horario_valido_fsi == '2':
            confirma = input ('O horario inserido esta vazio, para permanecer assim digite 1, para inserir um novo horario digite 2: \n')
            if confirma == '1':
                print ('Horario em branco')
                break
            elif confirma =='2':
                hora_inicio_fs = input ("Digite o horario de inicio durante a semana igual o exemplo: 08:00 \n")
                horario_valido_fsi = valida_horario(hora_inicio_fs)
            else:
                print ('Horario correto')


    hora_termino_fs = input("Qual o horario de termino no final de semana: \n")
    horario_valido_fst = valida_horario(hora_termino_fs)
    while horario_valido_fst != '1':
        hora_termino_fs = input ("Digite o horario de inicio termino no final de semana igual o exemplo: 18:00 \n")
        horario_valido_fst = valida_horario(hora_termino_fs)
        #print (horario_valido)
        if horario_valido_fst == '1':
            print ('Horario valido')
            break
        elif horario_valido_fst == '2':
            confirma = input ('O horario inserido esta vazio, para permanecer assim digite 1 caso queira inserir um novo horario digite 2: \n')
            if confirma == '1':
                print ('Horario em branco')
                break
            elif confirma =='2':
                hora_termino_fs = input ("Digite o horario de termino no final de semana igual o exemplo: 18:00 \n")
                horario_valido_fst = valida_horario(hora_termino_fs)
    else:
        print ('Horario correto')

# =================

    scriptivr = input("Qual o nome do script IVR: \n")
    while scriptivr[4:7] != num_projeto:
        print ('O numero do projeto inserido na variavel eh diferente do projeto inserido no comeco do script !!'  + scriptivr[4:7])
        scriptivr = input("Qual o nome do script IVR: \n")
        if scriptivr[4:7] == num_projeto:
            print ('Script IVR correto!')
            break
    else:
        print ('Script Ivr Correto: ' + scriptivr)

    scriptamd = input("Qual o nome do script AMD: \n")

    ip_servidor = input ('Digite o ip do servidor que o projeto sera configurado: \n')
    callerid = input ('Qual o callerid do projeto:  \n')
    tipo_campanha = input ('Qual o tipo de campanha desse projeto: (L) Localizador  (C) Cobrança (CL) Cenas Lamentaveis  \n')
    locutor = input ('Qual o Locutor utilizado no projeto: \n')
    qtd_agentes = input ('Quantos agentes serão utilizados no projeto: \n \n')

    print ('========> TABELA DADOS CLIENTE <============ \n')
    produto = input ("Qual o produto que será vocalizado: \n \n")
    codigo_cliente = input ("Qual o codigo do cliente na base de dados do fornecedor: \n \n")
    cpf = input ("Qual o CPF: (Caso não tenha CPF deixe o campo em branco) \n \n")
    if cpf == '':
        cpf = '12345678911'

    print ('========> TABELA OPERADORA CAMPANHA <============ \n')
    operadora = input ("Qual o nome da operadora que sera utilizada no projeto: \n \n")

#print ('========> TABELA SCRIPT SERVIDOR <============ \n')
#servidor = input ("Qual o nome do servidor que o Agente Virtual será implementado \n \n")


    os.system ('cls')
    print ('========> RESUMO DAS INFORMAÇÕES <============ \n')
    print ('========> TABELA CAMPANHA <============ \n \n')
    print ('Numero do projeto: ' + num_projeto)
    print ('\n')
    print ('Cliente: ' + nome_cliente)
    print ('\n')
    print ('Projeto: ' + nome_projeto)
    print ('\n')
    print ('Layout do Mailing: ' + layout_mailing)
    print ('\n')
    print ('Horario de funcionamento da campanha durante a semana: ' + hora_inicio_s + ' as ' +hora_termino_s)
    print ('\n')
    print ('Horario de funcionamento da campanha durante o final de semana: ' + hora_inicio_fs + ' as ' + hora_termino_fs)
    print ('\n')
    print ('Scripts IVR:' + scriptivr +'\n Script AMD ' + scriptamd)
    print ('\n')
    print ('Servidor utilizado no projeto: ' + ip_servidor)
    print ('\n')
    print ('CallerID: ' + callerid)
    print ('\n')
    print ('Tipo Campanha: ' + tipo_campanha)
    print ('\n')
    print ('Locutor utilizado no Projeto: ' + locutor)
    print ('\n')
    print ('Quantidade de Agentes: ' + qtd_agentes)
    print ('\n')
    print ('========> TABELA DADOS CLIENTE <============ \n \n')
    print ('PRODUTO: ' + produto)
    print ('\n')
    print ('Codigo do cliente: ' + codigo_cliente)
    print ('\n')
    print ('CPF: ' + cpf)
    print ('\n')
    print ('Layout Mailing: ' + layout_mailing)
    print ('\n')
    print ('========> TABELA OPERADORA CAMPANHA <============ \n \n')
    print ('Operadora de telefonia: ' + operadora)
    print ('\n')
    #print ('========> TABELA SCRIPT SERVIDOR <============ \n')
    #print ('O Servidor e: ' + servidor)
    #print ('\n')

    time.sleep(5)

    #src = 'C:/Users/augusto.nascimento/Documents/locutores/pt_BR-lb/nome'
    print ('Lista de Servidores: \n')
    print (' --- 200.201.128.218:2020\n --- 200.201.128.218:1044\n --- 200.206.41.210:21744\n --- 200.206.41.210:22744\n --- 200.170.220.147:10130\n --- 10.100.31.70\n --- 200.201.128.218:1818\n --- 189.112.36.196:3510\n  ')
    #database_dst = input ('Digite o ip do servidor BD de destino \n')
    database_dst = "200.201.128.218:2020"
    print ('O servidor BD de destino e: ' + database_dst)
    print ('\n')


    database = database_list[database_dst]

#database = database_list['189.112.36.196:3510']

    cn = pyodbc.connect(driver='{SQL Server Native Client 11.0}', server=database['server'], uid=database['uid'], pwd=database['pwd'])


    #i = "('{nome}', '{locutor}')".format(nome=l[0], locutor=l[1][:2])
#i = ""+num_projeto+","+nome_projeto+","+layout_mailing+","+nome_cliente+","+hora_inicio_s+","+hora_termino_s+","+hora_inicio_fs+","+hora_termino_fs+","'OVX'","+scriptivr+","+scriptamd+","+servidor+","+callerid+","+tipo_campanha+","+locutor+","+qtd_agentes+""
    dcampanha = ""+num_projeto+",'"+nome_projeto+"',"+layout_mailing+",'"+nome_cliente+"','"+hora_inicio_s+"','"+hora_termino_s+"','"+hora_inicio_fs+"','"+hora_termino_fs+"','OVX','"+scriptivr+"','"+scriptamd+"','"+ip_servidor+"','"+callerid+"','"+tipo_campanha+"','"+locutor+"',"+qtd_agentes+",1"
    dcliente = ""+num_projeto+",'"+produto+"',"+codigo_cliente+","+cpf
    ocampanha = ""+num_projeto+",'"+operadora+"'"
    renitencia = ""+num_projeto
    script_servidor = ""+num_projeto

    sql_dados_campanha = """EXEC [OPTIMUS].[DBO].[sp_IVR_DEPLOY_DADOS_CAMPANHA_V1] {valor1}""".format(valor1=dcampanha)
    sql_dados_cliente = """EXEC [OPTIMUS].[DBO].[sp_IVR_DEPLOY_DADOS_CLIENTE_V1] {valor2}""".format(valor2=dcliente)
    sql_operadora_campanha = """EXEC [OPTIMUS].[DBO].[sp_IVR_DEPLOY_OPERADORA_CAMPANHA_V1] {valor3}""".format(valor3=ocampanha)
    sql_renitencia = """EXEC [OPTIMUS].[DBO].[sp_IVR_DEPLOY_RENITENCIA_DISCADOR_V1] {valor4}""".format(valor4=renitencia)
    sql_script_servidor = """EXEC [OPTIMUS].[DBO].[sp_IVR_DEPLOY_SCRIPT_SERVIDOR_V1] {valor5}""".format(valor5=script_servidor)


    print ('O comando SQl que sera executado para inserir os dados na tabela campanha eh: ' +sql_dados_campanha)
    print ('O comando SQl que sera executado para criar a tabela dados cliente eh: ' +sql_dados_cliente)
    print ('O comando SQl que sera executado para inserir na tabela operadora campanha eh: ' +sql_operadora_campanha)
    print ('O comando SQl que sera executado para inserir na tabela renitencia eh: ' +sql_renitencia)
    print ('O comando SQl que sera executado para inserir na tabela script servidor eh: ' +sql_script_servidor)
    print ('\n \n \n')
    time.sleep(7)

    arq = open("INSERTS_DEPLOY.txt",'a+')
    arq.writelines("\n")
    arq.write("Comandos executados: \n")
    arq.writelines(num_projeto)
    arq.writelines("\n")
    arq.writelines(sql_dados_campanha)
    arq.writelines("\n")
    arq.writelines(sql_dados_cliente)
    arq.writelines("\n")
    arq.writelines(sql_operadora_campanha)
    arq.writelines("\n")
    arq.writelines(sql_renitencia)
    arq.writelines("\n")
    arq.writelines(sql_script_servidor)
    arq.close()

    print ('===========> POR FAVOR AGUARDE AS TABELAS ESTAO SENDO CRIADAS <============== \n')
    print ('===========> Caso as tabelas ja existam, os valores serao atualizados para as dados informados acima!! <============== \n')
    print ('===========> ISSO PODE DEMORAR ALGUNS MINUTOS <============== \n')
    now = datetime.now()
    now_hora = now.hour
    if now_hora  <= int('12'):
        print ('Sugiro Tomar um Cafe, daqui a pouco eh a hora do almoco!!\n')
    else:
        print ('Se ja almocou, sugiro tomar outro cafe, para nao dormir enquanto os comandos sao executados!!\n')


    print ('=============================================================================================================================')
    print ('Inserindo informacoes na tabela Campanha \n')
    cn.execute(sql_dados_campanha)
    time.sleep(4)
    print ('Criando tabela Dados_Cliente \n')
    cn.execute(sql_dados_cliente)
    time.sleep(4)
    print ('Inserindo informacoes na tabela Operadora Campanha \n')
    cn.execute(sql_operadora_campanha)
    time.sleep(3)
    print ('Inserindo informacoes na tabela Renitencia \n')
    cn.execute(sql_renitencia)
    time.sleep(3)
    cn.commit()
    time.sleep(3)
    print ('Inserindo informacoes na tabela Script Servidor \n')
    cn.execute(sql_script_servidor)
    time.sleep(3)
    cn.commit()


    print ('===========> SCRIPT FINALIZADO - AS TABELAS FORAM CRIADAS/ATUALIZADAS <============== \n \n')
    print ('===========> OS COMANDOS SQLs EXECUTADOS FORAM GRAVADOS NO ARQUIVO "INSERTS_DEPLOY.txt" no diretorio onde o script esta salvo! <=============\n \n')
    print ('===========> OBRIGADO POR UTILIZAR ESSE SCRIPT <============== \n')
    print ('===========> RETORNANDO PARA O MENU PRINCIPAL !! <============== \n')

    tabelas_criadas = '1'
    return tabelas_criadas
    time.sleep(20)
