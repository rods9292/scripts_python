# -*- coding: iso-8859-1 -*
import os, csv, contextlib, subprocess, time, pyodbc
from shutil import copy2
from sys import exit
from valida_dados import *

def criar_agente():
    os.system ('cls')


    separador = ('===' * 50)
    print (separador)

    print (separador)
    num_projeto = input ('Qual o numero do projeto? \n')
    projeto_valido = valida_projeto(num_projeto)
    while projeto_valido != '1':
        num_projeto = input ("Qual o numero do projeto com 3 caracteres: \n")
        projeto_valido = valida_projeto(num_projeto)
        if projeto_valido == '1':
            break
    else:
        print ('Numero do projeto correto \n')

    print (separador)
    versao_script = input ('Qual a versao do Agente Virtual? \n')
    script_valido = valida_versao_projeto(versao_script)
    while script_valido != '1':
        versao_script = input ("Qual a versao do Agente Virtual, utilize apenas numeros: \n")
        script_valido = valida_versao_projeto(versao_script)
        if script_valido == '1':
            break
    else:
        print ('Versao do Agente Virtual esta correta! \n')

    print (separador)
    descricao_projeto = input ('Digite a descricao do projeto \n Exemplo: URA SISCOM BANCO GM 584 === Spec V1 \n')

    print (separador)
    hash_dadoscliente = input('Qual a Proc GET_DATA_CLIENT? \n')
    hash_dadoscliente = hash_dadoscliente.upper()

    print (separador)
    diretorio_gramatica = input ('Qual o diretorio de gramatica padrao do Projeto?  Insira somente o nome, sem o "/" no comeco e no fim!! \n')
    diretorio_gramatica = diretorio_gramatica.upper()

    print (separador)
    locutor = input ('Qual o Locutor do projeto: \n')
    locutor = locutor.lower()
    locutor_valido = valida_locutor(locutor)
    while locutor_valido != '1':
        print ('Locutor inserido nao eh valido!! \n')
        locutor = input ('Qual o Locutor do projeto: \n')
        locutor = locutor.lower()
        locutor_valido = valida_locutor(locutor)
        if locutor_valido == '1':
            print ('Locutor Valido \n')
            break
    else:
        print ('Locutor valido!!')

    print (separador)
    nova_fase = input ('Deseja criar uma fase personalizada? Digite "Sim" ou "Nao"\n')
    nova_fase = nova_fase.upper()
    if nova_fase == 'SIM':
         fase = gera_fase(num_projeto)
    else:
        fase = ''


    print (separador)
    saudacao = input ('Qual o Template da Fase Saudacao: \n ST1 - ST2 - ST3 \n')
    saudacao = saudacao.lower()
    saudacao_valido = valida_template_fase_saudacao(saudacao)
    while saudacao_valido != '1':
        print ('Valor inserido nao eh valido!! \n')
        saudacao = input ("Qual o Template da Fase Saudacao: \n ST1 - ST2 - ST3 \n")
        saudacao_valido = valida_template_fase_saudacao(saudacao)
        if saudacao_valido == '1':
            print ('Template Correto \n ')
            break
    else:
        print ('Versao do template Correto! \n')

    print (separador)
    confirmar_cliente = input ('Qual o Template da Fase Confirmar Cliente: \n ST1 - ST2 - ST3 \n')
    confirmar_cliente = confirmar_cliente.lower()
    confirmar_cliente_valido = valida_template_fase_confirma(confirmar_cliente)
    while confirmar_cliente_valido != '1':
        confirmar_cliente = input ("Qual o Template da Fase Confirmar Cliente: \n ST1 - ST2 - ST3 \n")
        confirmar_cliente = confirmar_cliente.lower()
        confirmar_cliente_valido = valida_template_fase_confirma(confirmar_cliente)
        if confirmar_cliente_valido == '1':
            print ('Template Correto \n ')
            break
        else:
            print ('Versao do template Correto! \n')

    print (separador)
    qtd_encerrar = input ('Quantas fases de encerramento contem o projeto?  Caso nao tenha fase "encerra" digite o valor 0 \n')
    encerrar = fase_encerra(qtd_encerrar,num_projeto)

    print (separador)
    verifica_agendamento = input ('O projeto possui fase Agendamento? Digite "Sim" ou "Nao" \n')
    verifica_agendamento = verifica_agendamento.upper()
    if verifica_agendamento =='SIM':
        agendamento = fase_agendar(num_projeto)
    else:
        print ('Nao sera inserida a fase Agendar \n')
        agendamento = ''

    print (separador)
    verifica_celular = input ('O projeto possui fase para coletar celular? Digite "Sim" ou "Nao" \n')
    verifica_celular = verifica_celular.upper()
    if verifica_celular =='SIM':
        celular = fase_verifica_celular(num_projeto)
    else:
        print ('Nao sera inserida a fase Coleta e Confirma Celular \n')
        celular = ''


    print (separador)
    verifica_cpf = input ('O projeto contem a fase Confirma_CPF Digite "Sim" ou "Nao" \n')
    verifica_cpf = verifica_cpf.upper()
    if verifica_cpf =='SIM':
        cpf = fase_cpf(num_projeto)
    else:
        print ('Nao sera inserida a fase Confirmar_CPF \n')
        cpf = ''

    print (separador)
    verifica_cpf_dtmf = input ('O projeto contem a fase Confirma_CPF_DTMF Digite "Sim" ou "Nao" \n')
    verifica_cpf_dtmf = verifica_cpf_dtmf.upper()
    if verifica_cpf_dtmf =='SIM':
        cpf_dtmf = fase_cpf_dtmf(num_projeto)
    else:
        print ('Nao sera inserida a fase Confirmar_CPF_DTMF \n')
        cpf_dtmf = ''


    print (separador)
    verifica_cnpj = input ('O projeto contem a fase Confirma_CNPJ Digite "Sim" ou "Nao" \n')
    verifica_cnpj = verifica_cnpj.upper()
    if verifica_cnpj =='SIM':
        cnpj = fase_cnpj(num_projeto)
    else:
        print ('Nao sera inserida a fase Confirmar_CNPJ \n')
        cnpj = ''

    print (separador)
    verifica_cnpj_dtmf = input ('O projeto contem a fase Confirma_CNPJ_DTMF Digite "Sim" ou "Nao" \n')
    verifica_cnpj_dtmf = verifica_cpf_dtmf.upper()
    if verifica_cnpj_dtmf =='SIM':
        cnpj_dtmf = fase_cnpj_dtmf(num_projeto)
    else:
        print ('Nao sera inserida a fase Confirmar_CNPJ_DTMF \n')
        cnpj_dtmf = ''

    print (separador)
    verifica_transferencia = input ('O projeto possui fase de Transferencia? Digite "Sim" ou "Nao" \n')
    verifica_transferencia = verifica_transferencia.upper()
    if verifica_transferencia == 'SIM':
        confirma_transferencia = informacoes_transferencia(num_projeto)
    else:
        print ('Nao sera inserida a fase transferencia!')
        confirma_transferencia = ''


    print (separador)
    verifica_recado = input ('O projeto possui fase de Recado? Digite "Sim" ou "Nao" \n')
    verifica_recado = verifica_recado.upper()
    if verifica_recado == 'SIM':
        confirma_recado = fase_recado(num_projeto)
    else:
        print ('Nao sera inserida a fase Recado!')
        confirma_recado = ''


    #print (separador)
    #nova_fase = input ('Deseja criar uma fase personalizada? Digite "Sim" ou "Nao"\n')
    #nova_fase = nova_fase.upper()
    #if nova_fase == 'SIM':
    #     fase = gera_fase(num_projeto)
    #else:
    #    fase = ''

    agente_criado = gera_agente(num_projeto,versao_script,descricao_projeto,hash_dadoscliente,diretorio_gramatica,locutor,saudacao,confirmar_cliente,qtd_encerrar,encerrar,celular,agendamento,confirma_transferencia,cpf,cpf_dtmf,cnpj,cnpj_dtmf,confirma_recado,fase)
    if agente_criado == '1':
        print ('Agente Virtual criado com sucesso, verifique o diretorio o arquivo .conf que foi criado. \n')
        resp_index_global = []
        return agente_criado
    else:
        print ('Agente Virtual nao foi criado. \n Ainda nao sabemos o que aconteceu!! \n Foi mal pelo Vacilo !! \n')
        resp_index_global = []
        return agente_criado
