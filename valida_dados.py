# -*- coding: iso-8859-1 -*
from instrucoes_asterisk import *
global resp_index_global
resp_index_global = []

def valida_horario(horario):

    conta_hr = len(horario)
    hr_final = '0'

    if conta_hr == 0:
        print ("Nao foi inserido horario para discagem \n")
        hr_final = '2'
        return hr_final
    elif horario[2] == ':':
        if conta_hr != 5:
            print ('horario invalido = ' +horario)
            hr_final = '0'
            return hr_final
        else:
            print ('horario valido = ' +horario)
            hr_final = '1'
            return hr_final
    else:
        print ('horario invalido = ' +horario)
        hr_final = '0'
        return hr_final

def valida_template_fase_saudacao(template):

    template_final = '0'
    list_template = ['st1','st2','st3']

    if template in list_template:
        template_final = '1'
        return template_final
    else:
        template_final = '0'
        return template_final

def valida_template_fase_confirma(template):

    template_final = '0'
    list_template = ['st1','st2','st3']

    if template in list_template:
        template_final = '1'
        return template_final
    else:
        template_final = '0'
        return template_final

def valida_mailing(layout):

    layout_final = '0'

    list_mailing = ['7','9','1']
    #print (list_mailing[0])
    if layout in list_mailing:
        if layout == "7":
            layout_final = '1'
            print ('Layout Mailing = VIRTUS \n')
            return layout_final
        elif layout == "9":
            layout_final = '1'
            print ('Layout Mailing = VIRTUS_NEXT \n')
            return layout_final
        elif layout == "1":
            layout_final = '1'
            print ('Layout Mailing = SYSTEM_INTERACT \n')
            return layout_final
    else:
        print ('Layout invalido: ' +layout)
        layout_final = '0'
        return layout_final

def valida_projeto(projeto):

    projeto_final = '0'
    conta_projeto = len(projeto)

    if projeto.isdigit() is True:
        if conta_projeto == 3:
            projeto_final = '1'
            return projeto_final
        else:
            print ('O numero do projeto contem mais ou menos do que 3 caracteres!! \n')
            projeto_final = '0'
            return projeto_final
    else:
        print ('O numero do projeto contem caracteres do tipo string! \n')
        projeto_final = '0'
        return projeto_final

def valida_versao_projeto(versao):
    valida_versao = '0'
    if versao.isdigit() is True:
        valida_versao = '1'
        return valida_versao
    else:
        valida_versao = '0'
        return valida_versao

def valida_locutor(locutor):

    locutor_valido = '0'
    lista_locutor = ['gs','br','am','ap','em','fa','ga','gc','jm','lb','mc','sf']
    if locutor in lista_locutor:
        locutor_valido = '1'
        return locutor_valido
    else:
        return locutor_valido

def lista_resp_index(fase):

    resp = input ('Qual a RESP_INDEX da fase '+fase+' ? \n')
    resp_valida = '0'
    #global resp_index_global
    while resp_valida == '0':
        if resp in resp_index_global:
            print ('Lista de RESP_INDEX utilizadas: ',resp_index_global)
            resp = input ('RESP_INDEX '+resp+' ja esta sendo utilizada em outra fase do projeto, insira uma RESP_INDEX valida!! \n')
        else:
            resp_index_global.append(resp)
            resp_valida = '1'
            return resp
    else:
        resp_index_global.append(resp)
        resp_valida = '1'
        return resp

def fase_encerra(qtd,num_projeto):

    x = 0
    lista_fase = []
    print (qtd)
    while int(qtd) > int(x):

        nome_fase = input ('Digite o nome da fase encerrar, exemplo: "encerrar_acordo" \n')
        nome_fase_tratado1 = nome_fase.replace('_','')
        nome_fase_tratado2 = nome_fase.replace('_',' ')
        nome_fase_tratado3 = nome_fase_tratado2.title()

        fase = '''[ivr_'''+num_projeto+'''_outbound_'''+nome_fase+''']
        exten => s,1,MSet(URA_FASE='''+nome_fase_tratado3.replace(' ','')+''')
            same => n,GoSub(TOCA_PROMPT_V2,s,1('''+nome_fase_tratado1+''',1))
            same => n,Hangup() ''' '\n \n'

        lista_fase.append(fase)
        x = x + 1
    else:
        print ('Fases criadas, retornando para o menu de criacao do Agente Virtual \n')
        return lista_fase

def informacoes_transferencia(num_projeto):

    caller_id = input ('Qual o Caller ID? \n')
    vdn = input ('Qual a VDN para transferencia? \n')
    tronco = input ('Qual o nome do tronco SIP utilizado na transferencia? \n')
    tronco = tronco.lower()
    fase_transferencia = '''[ivr_'''+num_projeto+'''_outbound_transferir]
    exten => s,1,Set(URA_FASE=Transferir)
        same => n,MSet(STATUS_URA=Efetivo,SUB_STATUS_URA=Transferida)
        same => n,GoSub(TOCA_PROMPT_V2,s,1(transferir,1))
        same => n,Set(TRONCO_TRANSFERENCIA='''+tronco+''')
        same => n,Set(SEC_DIAL_TRANSFER='''+caller_id+''')
        same => n,Set(VDN_TRANSFERENCIA='''+vdn+''')
        same => n,Set(CALLERID(num)=${HASH(DADOS_CLIENTE,CODIGO_CLIENTE)}#${DDD}${TELEFONE}#TR)
        same => n,Set(ARRAY(TECH_PREFIX)=${IVR_TRESTTO_OVX_SELECT_GET_TECH_PREFIX(${VDN_TRANSFERENCIA},${TRONCO_TRANSFERENCIA})})
        same => n,Set(CDR(link)=${TRONCO_TRANSFERENCIA})
        same => n,Dial(SIP/${TRONCO_TRANSFERENCIA}/${STRREPLACE(TECH_PREFIX,NAO,)}${VDN_TRANSFERENCIA},${SEC_DIAL_TRANSFER})
        same => n,Wait(5)'''
    return fase_transferencia

def fase_cpf(num_projeto):

    fase = "confirma_cpf"
    resp = lista_resp_index(fase)
    ponto = input('Qual o ponto de reconhecimento da fase? \n')
    ponto = ponto.upper()
    confirma_cpf = '''[ivr_'''+num_projeto+'''_outbound_confirmar_cpf]
    exten => s,1,MSet(URA_FASE=ConfirmarCPF,RESP_INDEX='''+resp+''',COUNT_REPETIR=0,COUNT_INVALIDO=0,COUNT_QUEM_FALA=0,COUNT_QUE_INFO=0)
        same => n(retry),GoSub(TOCA_PROMPT_V2,s,1(confirmarcpf,1))
        same => n(recvoz),ClearHash(RV)
        same => n,MSet(HASH(RV,PROMPT)=,HASH(RV,BARGE_IN)=0,HASH(RV,MAX_SPEECH_TIMEOUT)=5000,HASH(RV,BEFORE_SPEECH_TIMEOUT)=5000,HASH(RV,AFTER_SPEECH_TIMEOUT)=800,HASH(RV,INCOMPLETE_TIMEOUT)=1200,HASH(RV,CONFIDENCE)=0.4)
        same => n,GoSub(REC_VOZ_V3,s,1('''+ponto+''',${PATH_RECVOZ}/BIN_TRESTTO_GLOBAL/,${RV_RETRY_COUNT},${RV_RETRY_TIME}))
        same => n,GotoIf($[$[$["${GOSUB_RETVAL}" = "SUCCESS"] & $["${HASH(RV,STATUS)}" = "000"]] & ${DIALPLAN_EXISTS(${CONTEXT},${HASH(RV,RESPOSTA)},1)}]?${HASH(RV,RESPOSTA)},1:i,1)
    exten => repetir,1,MSet(CDR(Resp_${RESP_INDEX})=${EXTEN},COUNT_REPETIR=$[${COUNT_REPETIR} + 1])
        same => n,GotoIf($[${COUNT_REPETIR} > 1]?${IVR_CTX_PREFIX}_confirmar_cpf_dtmf,s,1:s,retry)
    exten => quem_fala,1,MSet(CDR(Resp_${RESP_INDEX})=${EXTEN},COUNT_QUEM_FALA=$[${COUNT_QUEM_FALA}+1])
        same => n,GotoIf($[${COUNT_QUEM_FALA} > 1]?${IVR_CTX_PREFIX}_confirmar_cpf_dtmf,s,1)
        same => n,GoSub(TOCA_PROMPT_V2,s,1(confirmarcpf,2))
        same => n,Goto(s,recvoz)
    exten => nao_sei,1,MSet(SUB_STATUS_URA=NaoQuerInformarCPF,CDR(Resp_${RESP_INDEX})=${EXTEN})
        same => n,Goto(${IVR_CTX_PREFIX}_confirmar_cpf_dtmf,s,1)
    exten => nao,1,MSet(SUB_STATUS_URA=NaoQuerInformarCPF,CDR(Resp_${RESP_INDEX})=${EXTEN})
        same => n,Goto(${IVR_CTX_PREFIX}_confirmar_cpf_dtmf,s,1)
    exten => que_info,1,MSet(CDR(Resp_${RESP_INDEX})=${EXTEN},COUNT_QUEM_FALA=$[${COUNT_QUEM_FALA}+1])
        same => n,GotoIf($[${COUNT_QUEM_FALA} > 1]?${IVR_CTX_PREFIX}_confirmar_cpf_dtmf,s,1)
        same => n,GoSub(TOCA_PROMPT_V2,s,1(confirmarcpf,3))
        same => n,Goto(s,recvoz)
    exten => _XXX,1,MSet(SUB_STATUS_URA=CPFInformado,CDR(Resp_${RESP_INDEX})=${EXTEN})
        same => n,GotoIf($["${EXTEN}" = "${HASH(DADOS_CLIENTE,CPF):0:3}"]?${IVR_CTX_PREFIX}_vocalizar_debito,s,1:${IVR_CTX_PREFIX}_confirmar_cpf_dtmf,s,1)
    exten => i,1,Set(COUNT_INVALIDO=$[${COUNT_INVALIDO}+1])
        same => n,GotoIf($[${COUNT_INVALIDO} > 1]?${IVR_CTX_PREFIX}_confirmar_cpf_dtmf,s,1)
        same => n,GoSub(TOCA_PROMPT_V2,s,1(confirmarcpf,1,,2,1))
        same => n,Goto(s,recvoz)
    exten => t,1,Goto(i,1)'''
    return confirma_cpf

def fase_cpf_dtmf(num_projeto):

    fase = "confirmar_cpf_dtmf"
    resp = lista_resp_index(fase)
    confirma_cpf_dtmf = '''[ivr_'''+num_projeto+'''_outbound_confirmar_cpf_dtmf]
    exten => s,1,MSet(URA_FASE=ConfirmarCPFDTMF,RESP_INDEX='''+resp+''',COUNT_INVALIDO=0,COUNT_REPETIR=0)
        same => n,GosubIf($["${TIPO_TELEFONE_CLIENTE}"="Fixo"]?TOCA_PROMPT_V2,s,1(confirmarcpfdtmf,1,,,2))
        same => n,GosubIf($["${TIPO_TELEFONE_CLIENTE}"="Celular"]?TOCA_PROMPT_V2,s,1(confirmarcpfdtmf,1))
        same => n(dtmf),WaitExten(5)
    exten => _XXX,1,MSet(SUB_STATUS_URA=CPFInformado,CDR(Resp_${RESP_INDEX})=${EXTEN},COUNT_REPETIR=$[${COUNT_REPETIR}+1])
        same => n,GotoIf($["${EXTEN}" = "${HASH(DADOS_CLIENTE,CPF):0:3}"]?${IVR_CTX_PREFIX}_vocalizar_debito,s,1)
        same => n,GotoIf($["${TIPO_TELEFONE_CLIENTE_CLIENTE}"="celular"]?${IVR_CTX_PREFIX}_encerrar_cpf_invalido,s,1)
        same => n,GotoIf($[${COUNT_REPETIR} > 1]?${IVR_CTX_PREFIX}_encerrar_cpf_invalido,s,1)
        same => n,GoSub(TOCA_PROMPT_V2,s,1(confirmarcpfdtmf,2))
        same => n,Goto(s,dtmf)
    exten => i,1,Set(COUNT_INVALIDO=$[${COUNT_INVALIDO}+1])
        same => n,GotoIf($[${COUNT_INVALIDO} > 2]?${IVR_CTX_PREFIX}_encerrar_cpf_invalido,s,1)
        same => n,GoSub(TOCA_PROMPT_V2,s,1(confirmarcpfdtmf,1,,2,1))
        same => n,Goto(s,dtmf)
    exten => t,1,Goto(i,1)'''
    return confirma_cpf_dtmf

def fase_cnpj(num_projeto):

    fase = "confirmar_cnpj"
    resp = lista_resp_index(fase)
    ponto = input('Qual o ponto de reconhecimento da fase? \n')
    ponto = ponto.upper()
    confirma_cnpj = '''[ivr_'''+num_projeto+'''_outbound_confirmar_cnpj]
    exten => s,1,MSet(URA_FASE=ConfirmarCNPJ,RESP_INDEX='''+resp+''',COUNT_REPETIR=0,COUNT_INVALIDO=0,COUNT_QUEM_FALA=0)
        same => n(retry),GoSubIf($["${FLAG_RESPONSAVEL_FINANCEIRO}"="1"]?TOCA_PROMPT_V2,s,1(confirmarcnpj,1,,,1):TOCA_PROMPT_V2,s,1(confirmarcnpj,1,,,2))
        same => n(recvoz),ClearHash(RV)
        same => n,MSet(HASH(RV,PROMPT)=,HASH(RV,BARGE_IN)=0,HASH(RV,MAX_SPEECH_TIMEOUT)=5000,HASH(RV,BEFORE_SPEECH_TIMEOUT)=5000,HASH(RV,AFTER_SPEECH_TIMEOUT)=800,HASH(RV,INCOMPLETE_TIMEOUT)=1200,HASH(RV,CONFIDENCE)=0.4)
        same => n,GoSub(REC_VOZ_V3,s,1('''+ponto+''',,${RV_RETRY_COUNT},${RV_RETRY_TIME}))
        same => n,GotoIf($[$[$["${GOSUB_RETVAL}" = "SUCCESS"] & $["${HASH(RV,STATUS)}" = "000"]] & ${DIALPLAN_EXISTS(${CONTEXT},${HASH(RV,RESPOSTA)},1)}]?${HASH(RV,RESPOSTA)},1:i,1)
    exten => repetir,1,MSet(CDR(Resp_${RESP_INDEX})=${EXTEN},COUNT_REPETIR=$[${COUNT_REPETIR} + 1])
        same => n,GotoIf($[${COUNT_REPETIR} > 2]?${IVR_CTX_PREFIX}_confirmar_cnpj_dtmf,s,1:s,retry)
    exten => quem_fala,1,MSet(CDR(Resp_${RESP_INDEX})=${EXTEN},COUNT_QUEM_FALA=$[${COUNT_QUEM_FALA}+1])
        same => n,GotoIf($[${COUNT_QUEM_FALA} > 1]?${IVR_CTX_PREFIX}_confirmar_cnpj_dtmf,s,1)
        same => n,GoSub(TOCA_PROMPT_V2,s,1(confirmarcnpj,2))
        same => n,Goto(s,recvoz)
    exten => nao_sei,1,MSet(SUB_STATUS_URA=NaoSabeInformarCNPJ,CDR(Resp_${RESP_INDEX})=${EXTEN})
        same => n,Goto(${IVR_CTX_PREFIX}_confirmar_cnpj_dtmf,s,1)
    exten => nao,1,MSet(SUB_STATUS_URA=NaoQuerInformarCNPJ,CDR(Resp_${RESP_INDEX})=${EXTEN})
        same => n,Goto(${IVR_CTX_PREFIX}_confirmar_cnpj_dtmf,s,1)
    exten => _XX,1,MSet(SUB_STATUS_URA=CNPJInformado,CDR(Resp_${RESP_INDEX})=${EXTEN})
        same => n,GotoIf($["${EXTEN}" = "${HASH(DADOS_CLIENTE,CPF):0:2}"]?${IVR_CTX_PREFIX}_vocalizar_debito,s,1:${IVR_CTX_PREFIX}_confirmar_cnpj_dtmf,s,1)
    exten => i,1,Set(COUNT_INVALIDO=$[${COUNT_INVALIDO}+1])
        same => n,GotoIf($[${COUNT_INVALIDO} > 2]?${IVR_CTX_PREFIX}_confirmar_cnpj_dtmf,s,1)
        same => n,GoSub(TOCA_PROMPT_V2,s,1(confirmarcnpj,1,,2))
        same => n,Goto(s,recvoz)
    exten => t,1,Goto(i,1)'''
    return confirma_cnpj

def fase_cnpj_dtmf(num_projeto):

    fase = "confirmar_cnpj_dtmf"
    resp = lista_resp_index(fase)
    confirma_cnpj_dtmf = '''[ivr_'''+num_projeto+'''_outbound_confirmar_cnpj_dtmf]
    exten => s,1,MSet(URA_FASE=ConfirmarCNPJ_DTMF,RESP_INDEX='''+resp+''',COUNT_REPETIR=0,COUNT_INVALIDO=0)
        same => n(retry),Goto(${TIPO_TELEFONE_CLIENTE})
        same => n(celular),GoSub(TOCA_PROMPT_V2,s,1(confirmarcnpjdtmf,1,,,2):TOCA_PROMPT_V2,s,1(confirmarcnpjdtmf,1,,,1))
        same => n,GoTo(dtmf)
        same => n(fixo),GoSub(TOCA_PROMPT_V2,s,1(confirmarcnpjdtmf,2,,,1):TOCA_PROMPT_V2,s,1(confirmarcnpjdtmf,2,,,2))
        same => n(dtmf),WaitExten(5)
    exten => _XX,1,MSet(SUB_STATUS_URA=CNPJInformadoDTMF,CDR(Resp_${RESP_INDEX})=${EXTEN},COUNT_REPETIR=$[${COUNT_REPETIR}+1])
        same => n,GotoIf($["${EXTEN}" = "${HASH(DADOS_CLIENTE,CPF):0:2}"]?${IVR_CTX_PREFIX}_vocalizar_debito,s,1)
        same => n,GoToIf($["${TIPO_TELEFONE_CLIENTE}"="celular"]?${IVR_CTX_PREFIX}_encerrar_sem_validar_dados,s,1)
        same => n,GotoIf($[${COUNT_REPETIR} > 1]?${IVR_CTX_PREFIX}_encerrar_sem_validar_dados,s,1)
        same => n,GoSub(TOCA_PROMPT_V2,s,1(confirmarcnpjdtmf,3))
        same => n,Goto(s,dtmf)
    exten => i,1,Set(COUNT_INVALIDO=$[${COUNT_INVALIDO}+1])
        same => n,GotoIf($[${COUNT_INVALIDO} > 1]?${IVR_CTX_PREFIX}_encerrar_sem_validar_dados,s,1)
        same => n,GoSub(TOCA_PROMPT_V2,s,1(confirmarcnpjdtmf,2,,2))
        same => n,Goto(s,dtmf)
    exten => t,1,Goto(i,1)'''
    return confirma_cnpj_dtmf

def fase_recado(num_projeto):

    fase = "vocalizar_recado"
    resp = lista_resp_index(fase)
    ponto = input('Qual o ponto de reconhecimento da fase? \n')
    ponto = ponto.upper()
    recado = ''' [ivr_'''+num_projeto+'''_outbound_vocalizar_recado]
    exten => s,1,MSet(URA_FASE=VocalizarRecado,RESP_INDEX='''+resp+''',COUNT_REPETIR=0,COUNT_INVALIDO=0)
        same => n,GoSub(TOCA_PROMPT_V2,s,1(vocalizarrecado,1))
        same => n(recvoz),ClearHash(RV)
        same => n,MSet(HASH(RV,PROMPT)=,HASH(RV,BARGE_IN)=0,HASH(RV,MAX_SPEECH_TIMEOUT)=5000,HASH(RV,BEFORE_SPEECH_TIMEOUT)=5000,HASH(RV,AFTER_SPEECH_TIMEOUT)=800,HASH(RV,INCOMPLETE_TIMEOUT)=1200,HASH(RV,CONFIDENCE)=0.5)
        same => n,GoSub(REC_VOZ_V3,s,1('''+ponto+''',${PATH_RECVOZ}/BIN_TRESTTO_GLOBAL/,${RV_RETRY_COUNT},${RV_RETRY_TIME}))
        same => n,GotoIf($[$["${GOSUB_RETVAL}" = "SUCCESS"] & $["${HASH(RV,STATUS)}" = "000"]]?${IF($[${DIALPLAN_EXISTS(${CONTEXT},${HASH(RV,RESPOSTA)},1)} = 0]?s-)}${HASH(RV,RESPOSTA)},1:i,1)
    exten => repetir,1,MSet(SUB_STATUS_URA=RepetirRecado,CDR(Resp_${RESP_INDEX})=${EXTEN})
        same => n,Goto(${IVR_CTX_PREFIX}_encerrar,s,1)
    exten => sim,1,MSet(SUB_STATUS_URA=RepetirRecado,CDR(Resp_${RESP_INDEX})=${EXTEN})
        same => n,Goto(${IVR_CTX_PREFIX}_encerrar,s,1)
    exten => nao,1,MSet(SUB_STATUS_URA=NaoRepetirRecado,CDR(Resp_${RESP_INDEX})=${EXTEN})
        same => n,Goto(${IVR_CTX_PREFIX}_encerrar,s,1)
    exten => i,1,MSet(COUNT_INVALIDO=$[ ${COUNT_INVALIDO} + 1 ])
        same => n,GotoIf($[${COUNT_INVALIDO} > 2]?${IVR_CTX_PREFIX}_encerrar,s,1)
        same => n,GoSub(TOCA_PROMPT_V2,s,1(vocalizarrecado,1,,2,1))
        same => n,Goto(s,recvoz)'''
    return recado

def fase_verifica_celular(num_projeto):

    fase1 = 'coletar_celular'
    fase2 = 'confirmar_celular'
    resp1 = lista_resp_index(fase1)
    resp2 = lista_resp_index(fase2)
    ponto = input ('Qual o ponto de reconhecimento da fase '+fase2+'\n')
    ponto = ponto.upper()
    coleta_celular = '\n''''[ivr_'''+num_projeto+'''_outbound_coletar_celular]
        exten => s,1,MSet(URA_FASE=ColetarCelular,RESP_INDEX='''+resp1+''',COUNT_INVALIDO=0,COUNT_COLETARCELULAR=$[${COUNT_COLETARCELULAR} + 1])
            same => n,GoSubIf($[${COUNT_TENTATIVA_COLETAR_CELULAR} > 1]?TOCA_PROMPT_V2,s,1(coletarcelular,1,,,2):TOCA_PROMPT_V2,s,1(coletarcelular,1))
            same => n(dtmf),NoOp(DTMF)
            same => n,WaitExten(5)
        exten => _0ZZZZ9XXXXXXXX,1,Goto(${EXTEN:3},1)
        exten => _0ZZ9XXXXXXXX,1,Goto(${EXTEN:1},1)
        exten => _ZZ9XXXXXXXX,1,MSet(SUB_STATUS=NovoTelefoneColetado,CDR(RESP_${RESP_INDEX})=${EXTEN},NUMERO_SMS=${EXTEN})
            same => n,Goto(${IVR_CTX_PREFIX}_confirmar_celular,s,1)
        exten => _0ZZZZ7XXXXXXX,1,Goto(${EXTEN:1},1)
        exten => _0ZZ7XXXXXXX,1,Goto(${EXTEN:1},1)
        exten => _ZZ7XXXXXXX,1,MSet(SUB_STATUS=NovoTelefoneColetado,CDR(RESP_${RESP_INDEX})=${EXTEN},NUMERO_SMS=${EXTEN})
            same => n,Goto(${IVR_CTX_PREFIX}_confirmar_celular,s,1)
        exten => t,1,Goto(i,1)
        exten => i,1,Set(COUNT_INVALIDO=$[ ${COUNT_INVALIDO} + 1 ])
           same => n,GotoIf($[${COUNT_INVALIDO} > 2]?${IVR_CTX_PREFIX}_encerrar,s,1)
           same => n,GoSub(TOCA_PROMPT_V2,s,1(coletarcelular,1,,2,1))
           same => n,Goto(s,dtmf)

      [ivr_'''+num_projeto+'''_outbound_confirmar_celular]
        exten => s,1,MSet(URA_FASE=ConfirmarCelular,RESP_INDEX='''+resp2+''',COUNT_REPETIR=0,COUNT_INVALIDO=0,COUNT_QUAL_NUMERO=0)
            same => n(retry),GoSub(TOCA_PROMPT_V2,s,1(confirmarcelular,1))
            same => n(tts_celular_coletado),GoSub(EXECUTA_VOCALIZAR,s,1(telefone,${NUMERO_SMS}))
            same => n,GoSub(TOCA_PROMPT_V2,s,1(confirmarcelular,2))
            same => n(recvoz),MSet(HASH(RV,PROMPT)=,HASH(RV,BARGE_IN)=0,HASH(RV,MAX_SPEECH_TIMEOUT)=5000,HASH(RV,BEFORE_SPEECH_TIMEOUT)=5000,HASH(RV,AFTER_SPEECH_TIMEOUT)=800,HASH(RV,INCOMPLETE_TIMEOUT)=1200,HASH(RV,CONFIDENCE)=0.5)
            same => n,GoSub(REC_VOZ_V3,s,1('''+ponto+''',,${RV_RETRY_COUNT},${RV_RETRY_TIME}))
            same => n,GotoIf($[$[$["${GOSUB_RETVAL}" = "SUCCESS"] & $["${HASH(RV,STATUS)}" = "000"]] & ${DIALPLAN_EXISTS(${CONTEXT},${HASH(RV,RESPOSTA)},1)}]?${HASH(RV,RESPOSTA)},1:i,1)
        exten => repetir,1,MSet(CDR(Resp_${RESP_INDEX})=${EXTEN},COUNT_REPETIR=$[${COUNT_REPETIR} + 1])
            same => n,GotoIf($[${COUNT_REPETIR} > 2]?${IVR_CTX_PREFIX}_transferir,s,1:s,retry)
        exten => nao,1,MSet(SUB_STATUS_URA=TransferidoNaoConfirmouTelColetado,CDR(Resp_${RESP_INDEX})=${EXTEN})
            same => n,GoToIf($[${COUNT_COLETAR_CELULAR}>1]?${IVR_CTX_PREFIX}_transferir,s,1:${IVR_CTX_PREFIX}_coletar_celular,s,1)
        exten => qual_numero,1,MSet(SUB_STATUS_URA=TransferidoQualNumero,CDR(Resp_${RESP_INDEX})=${EXTEN},COUNT_QUAL_NUMERO=$[${COUNT_QUAL_NUMERO} + 1])
            same => n,GoToIf($[${COUNT_QUAL_NUMERO}>1]?${IVR_CTX_PREFIX}_transferir,s,1)
            same => n,GoSub(TOCA_PROMPT_V2,s,1(confirmarcelular,3))
            same => n,GoTo(s,tts_celular_coletado)
        exten => sim,1,MSet(SUB_STATUS_URA=ConfirmouCelularColetado,CDR(Resp_${RESP_INDEX})=${EXTEN},FLAG_BACKOFFICE=1)
            same => n,GoTo({IVR_CTX_PREFIX}_encerrar_acordo,s,1)
        exten => i,1,Set(COUNT_INVALIDO=$[ ${COUNT_INVALIDO} + 1 ])
            same => n,GotoIf($[${COUNT_INVALIDO} > 2]?${IVR_CTX_PREFIX}_transferir,s,1)
            same => n,Goto(s,retry)''' '\n'

    return coleta_celular

def fase_agendar(num_projeto):

    fase = "agendar_ligacao"
    resp = lista_resp_index(fase)
    ponto = input('Qual o ponto de reconhecimento da fase? \n')
    ponto = ponto.upper()
    fase_agendar = '''[ivr_'''+num_projeto+'''_outbound_agendar_ligacao]
    exten => s,1,MSet(URA_FASE=AgendarLigacao,RESP_INDEX='''+resp+''',COUNT_REPETIR=0,COUNT_INVALIDO=0)
        same => n(retry),GoSub(TOCA_PROMPT_V2,s,1(agendarligacao,1))
        same => n(recvoz),ClearHash(RV)
        same => n,MSet(HASH(RV,PROMPT)=,HASH(RV,BARGE_IN)=0,HASH(RV,MAX_SPEECH_TIMEOUT)=5000,HASH(RV,BEFORE_SPEECH_TIMEOUT)=5000,HASH(RV,AFTER_SPEECH_TIMEOUT)=800,HASH(RV,INCOMPLETE_TIMEOUT)=1200,HASH(RV,CONFIDENCE)=0.5)
        same => n,GoSub(REC_VOZ_V3,s,1('''+ponto+''',${PATH_RECVOZ}/BIN_TRESTTO_GLOBAL/,${RV_RETRY_COUNT},${RV_RETRY_TIME}))
        same => n,GotoIf($[$["${GOSUB_RETVAL}" = "SUCCESS"] & $["${HASH(RV,STATUS)}" = "000"]]?${IF($[${DIALPLAN_EXISTS(${CONTEXT},${HASH(RV,RESPOSTA)},1)} = 0]?s-)}${HASH(RV,RESPOSTA)},1:i,1)
    exten => repetir,1,MSet(CDR(Resp_${RESP_INDEX})=${EXTEN},COUNT_REPETIR=$[${COUNT_REPETIR} + 1])
        same => n,GotoIf($[${COUNT_REPETIR} > 2]?${IVR_CTX_PREFIX}_encerrar,s,1)
        same => n,Goto(s,retry)
    exten => manha,1,MSet(SUB_STATUS_URA=AgendamentoManha,CDR(RESP_${RESP_INDEX})=${EXTEN})
        same => n,Goto(${IVR_CTX_PREFIX}_vocalizar_recado,s,1)
    exten => tarde,1,MSet(SUB_STATUS_URA=AgendamentoTarde,CDR(RESP_${RESP_INDEX})=${EXTEN})
        same => n,Goto(${IVR_CTX_PREFIX}_vocalizar_recado,s,1)
    exten => noite,1,MSet(SUB_STATUS_URA=AgendamentoNoite,CDR(RESP_${RESP_INDEX})=${EXTEN})
        same => n,Goto(${IVR_CTX_PREFIX}_vocalizar_recado,s,1)
    exten => qualquer_horario,1,MSet(SUB_STATUS_URA=AgendamentoQualquerHorario,CDR(RESP_${RESP_INDEX})=${EXTEN})
        same => n,Goto(${IVR_CTX_PREFIX}_vocalizar_recado,s,1)
    exten => nenhum,1,MSet(SUB_STATUS_URA=AgendadaNenhum,CDR(RESP_${RESP_INDEX})=${EXTEN})
        same => n,Goto(${IVR_CTX_PREFIX}_encerrar,s,1)
    exten => i,1,MSet(COUNT_INVALIDO=$[ ${COUNT_INVALIDO} + 1 ])
        same => n,GotoIf($[${COUNT_INVALIDO} > 2]?${IVR_CTX_PREFIX}_encerrar,s,1)
        same => n,GoSub(TOCA_PROMPT_V2,s,1(agendarligacao,1,,2,1))
        same => n,Goto(s,recvoz)'''
    return fase_agendar

def gera_saida(qtd_saidas):
    s = 0
    saidas_fase = []
    #variaveis_fase = []
    print (qtd_saidas)
    while int(qtd_saidas) > int(s):

        nome_saida = input ('Digite o nome da saida, exemplo: "sim", "nao_conheco", "mudou" \n')
        nome_saida = nome_saida.lower()
        nome_saida_prompt = nome_saida.replace('_','')
        substatus = input ('Digite o Substatus da Saida: \n Exemplo: Confirmou Cliente, Agendamento Qualquer Horario \n')
        substatus = substatus.title()
        dest_saida = input ('Qual o destino da saida '+nome_saida+'? \n')
        #variaveis_saida = input ('Se a saida setar alguma variavel, digite o nome da mesma: \n')
        #variaveis_saida = variaveis_saida.upper()
        saida = '''exten => '''+nome_saida+''',1,MSet(SUB_STATUS_URA='''+substatus.replace(' ','')+''',CDR(RESP_${RESP_INDEX})=${EXTEN})
                        same => n,Goto(${IVR_CTX_PREFIX}_'''+dest_saida+''',s,1)'''
        saidas_fase.append(saida)
        s = s + 1
    else:
        print ('Saidas inseridas: ',saidas_fase)


    repetir = input('A fase possui a saida Repetir: Sim ou Nao? \n')
    repetir = repetir.upper()
    if repetir == 'SIM':
        qtd_rpt = input ('Qual a quantidade de tentatias da saida Repetir? \n')
        dst_rpt = input ('Qual o destino da saida Repetir? \n Exemplo: "encerrar_acordo", "ecenrrar", "transferir" \n')
        retry_rpt = input ('Qual o ponto de retorno da saida? \n Exemplo: "retry", "retry2" \n')
        saida_repetir = '''exten => repetir,1,MSet(CDR(Resp_${RESP_INDEX})=${EXTEN},COUNT_REPETIR=$[${COUNT_REPETIR} + 1])
                    same => n,GotoIf($[${COUNT_REPETIR} > '''+qtd_rpt+''']?${IVR_CTX_PREFIX}_'''+dst_rpt+''',s,1)
                    same => n,Goto(s,'''+retry_rpt+''')'''
        saidas_fase.append(saida_repetir)
    else:
        print ('Nao foi inserida a saida Repetir')

    invalido = input ('A fase possui a saida Invalido: Sim ou Nao? \n')
    invalido = invalido.upper()
    if invalido == 'SIM':
        qtd_inv = input ('Qual a quantidade de tentatias da saida Invalido? \n')
        dst_inv = input ('Qual o destino da saida Invalido? \n Exemplo: "encerrar_acordo", "encerrar", "transferir" \n')
        retry_inv = input ('Qual o ponto de retorno da saida? \n Exemplo: "retry", "recvoz" \n')
        saida_invalido = '''exten => i,1,MSet(COUNT_INVALIDO=$[ ${COUNT_INVALIDO} + 1 ])
            same => n,GotoIf($[${COUNT_INVALIDO} > '''+qtd_inv+''']?${IVR_CTX_PREFIX}_'''+dst_inv+''',s,1)
            same => n,GoSub(TOCA_PROMPT_V2,s,1(agendarligacao,1,,2,1))
            same => n,Goto(s,'''+retry_inv+''')'''
        saidas_fase.append(saida_invalido)
    else:
        print ('Nao foi inserida da saida Invalido')


    print ('Saidas criadas, retornando para criacao da Fase!! \n')
    print ('Saidas: ' ,saidas_fase)
    return saidas_fase


def gera_fase(num_projeto):

    sequencia_comandos = []
    nome_fase = input ('Qual o nome da fase? \n Exemplo: consulta_pagamento \n')
    nome_prompt = nome_fase.replace('_','')
    nome_prompt = nome_prompt.lower()
    sequencia_comandos.append('[ivr_'+num_projeto+'_outbound_'+nome_fase+']')
    resp = lista_resp_index(nome_fase)
    sequencia_comandos.append('   exten => s,1,MSet(URA_FASE='+nome_fase+',RESP_INDEX='+resp+',COUNT_REPETIR=0,COUNT_INVALIDO=0)')
    qtd_instrucoes = input ('Quantas instrucoes essa fase contem antes de iniciar o reconhecimento de voz? \n')
    rpt = 0
    num_instrucao = 1
    while int(qtd_instrucoes) > int(rpt):
        print ('1 -',lista_linhas['1'])
        print ('2 -',lista_linhas['2'])
        print ('3 -',lista_linhas['3'])
        print ('4 -',lista_linhas['4'])
        print ('5 -',lista_linhas['5'])
        print ('6 -',lista_linhas['6'])
        print ('7 -',lista_linhas['7'])
        linha = input ('Qual a instrução '+str(num_instrucao)+' da fase? Selecione o numero da linha\n')
        if linha in lista_linhas:
            sequencia_comandos.append(lista_linhas[''+linha+''])
            num_instrucao = num_instrucao + 1
            rpt = rpt + 1
            print ('A sequencia de comandos atual eh: ',sequencia_comandos)
        else:
            print ('Opcao invalida \n')
    else:
        print ('As linhas foram inseridas no codigo! \n')

    ponto = input('Qual o ponto de reconhecimento da fase? \n')
    ponto = ponto.upper()
    recvoz = '''same => n(recvoz),ClearHash(RV)
    same => n,MSet(HASH(RV,PROMPT)=,HASH(RV,BARGE_IN)=0,HASH(RV,MAX_SPEECH_TIMEOUT)=5000,HASH(RV,BEFORE_SPEECH_TIMEOUT)=5000,HASH(RV,AFTER_SPEECH_TIMEOUT)=800,HASH(RV,INCOMPLETE_TIMEOUT)=1200,HASH(RV,CONFIDENCE)=0.5)
    same => n,GoSub(REC_VOZ_V3,s,1('''+ponto+''',,${RV_RETRY_COUNT},${RV_RETRY_TIME}))
    same => n,GotoIf($[$[$["${GOSUB_RETVAL}" = "SUCCESS"] & $["${HASH(RV,STATUS)}" = "000"]] & ${DIALPLAN_EXISTS(${CONTEXT},${HASH(RV,RESPOSTA)},1)}]?${HASH(RV,RESPOSTA)},1:i,1)'''
    qtd_saidas = input ('Quantas saidas a fase possui, exceto Repetir e Invalido? \n')
    #qtd_variaveis = input ('Quantas variaveis serão utilizadas na fase? \n')
    saidas = gera_saida(qtd_saidas)
    sequencia_comandos.append(recvoz)
    sequencia_comandos.append(saidas)
    print (sequencia_comandos)
    return(sequencia_comandos)

def gera_agente(num_projeto,versao_script,descricao_projeto,hash_dadoscliente,diretorio_gramatica,locutor,saudacao,confirmar_cliente,qtd_encerrar,encerrar,celular,agendamento,valida_transferencia,cpf,cpf_dtmf,cnpj,cnpj_dtmf,confirma_recado,fase):

    fase_1 = '''[ivr_'''+num_projeto+'''_outbound]
     exten => _X!,1,NoOp(===== '''+descricao_projeto+''' =====)
        same => n,Set(VERSAO_SPEC='''+versao_script+''')
        same => n,ExecIf($[ "${CHANNEL:0:5}" == "Local"]?NoCDR())
        same => n,ExecIf($[ "${CHANNEL:0:5}" == "Local"]?Hangup())
        same => n,Set(HASH(DADOS_CLIENTE)=${'''+hash_dadoscliente+'''(${CAMPANHA},${ID_CLIENTE})})
        same => n,GoSub(INICIALIZA_URA_V5,${EXTEN},1('''+num_projeto+''',${VERSAO_SPEC},'''+num_projeto+'''0,'''+locutor+'''))
        same => n,Set(GRAMMAR_DIR=${PATH_RECVOZ}/'''+diretorio_gramatica+'''/)
        same => n,MSet(COUNT_COLETAR_NOVO_CONTATO=0,COUNT_COLETAR_CELULAR=0)
        same => n,ExecIf($[$[${LEN(${TELEFONE})} = 9] | $["${TELEFONE:0:1}" = "7"]]?Set(TIPO_TELEFONE_CLIENTE=Celular):Set(TIPO_TELEFONE_CLIENTE=Fixo))
        same => n,ExecIf($["${LEN(${HASH(DADOS_CLIENTE,CPF)})}"="11"]?Set(TIPO_VALIDACAO=cpf):Set(TIPO_VALIDACAO=cnpj))
        same => n,Goto(${IVR_CTX_PREFIX}_saudacao,s,1)'''

    fase_saudacao = '''[ivr_'''+num_projeto+'''_outbound_saudacao]
     exten => s,1,GoSub(saudacao_'''+saudacao+''',s,1)
        same => n,Goto(${IVR_CTX_PREFIX}_confirma_cliente,s,1)'''

    fase_confirma_cliente = '''[ivr_'''+num_projeto+'''_outbound_confirma_cliente]
    exten => s,1,GoSub(confirma_cliente_'''+confirmar_cliente+''',s,1)
        same => n,Noop(${GOSUB_RETVAL})
        same => n,Goto(${IVR_CTX_PREFIX}_${GOSUB_RETVAL},s,1)'''

    fase_hangup = '''[ivr_'''+num_projeto+'''_hangup]
    exten => _X!,1,NoOp(Hangup URA)
        same => n,GoSub(FINALIZA_URA,${EXTEN},1)'''


    arq = open("ivr_"+num_projeto+"_outbound.conf",'a+')
    arq.writelines(fase_1)
    arq.writelines("\n \n")
    arq.writelines(fase_saudacao)
    arq.writelines("\n \n")
    arq.writelines(fase_confirma_cliente)
    arq.writelines("\n \n")
    if cpf == '':
        print ('Nao sera inserida a fase CPF!! \n')
    else:
        print ('Adicionando fase CPF!! \n')
        arq.writelines(cpf)
        arq.writelines("\n \n")

    if cpf_dtmf == '':
        print ('Nao sera inserida a fase CPF_DTMF!! \n')
    else:
        print ('Adicionando fase CPF_DTMF!! \n')
        arq.writelines(cpf_dtmf)
        arq.writelines("\n \n")

    if cnpj == '':
        print ('Nao sera inserida a fase CNPJ!! \n')
    else:
        print ('Adicionando fase CNPJ!! \n')
        arq.writelines(cnpj)
        arq.writelines("\n \n")

    if cnpj_dtmf == '':
        print ('Nao sera inserida a fase CNPJ_DTMF!! \n')
    else:
        print ('Adicionando fase CNPJ_DTMF!! \n')
        arq.writelines(cnpj_dtmf)
        arq.writelines("\n \n")

    if agendamento == '':
        print ('Nao sera inserida a fase Agendamento!! \n')
    else:
        print ('Adicionando fase Agendamento!! \n')
        arq.writelines(agendamento)
        arq.writelines("\n \n")

    if celular == '':
        print ('Nao sera inserida a fase Coleta e Confirma Celular!! \n')
    else:
        print ('Adicionando fase Coleta e Confirma Celular!! \n')
        arq.writelines(celular)
        arq.writelines("\n \n")

    if fase == '':
        print ('Nao sera inserida fases personalizadas!! \n')
    else:
        print ('Inserindo fase personalizada!! \n')
        arq.writelines(str(fase))
        arq.writelines("\n \n ")

    if confirma_recado == '':
        print ('Nao sera inserida a fase Recado!! \n')
    else:
        print ('Adicionando fase Recado!! \n')
        arq.writelines(confirma_recado)
        arq.writelines("\n \n")

    if valida_transferencia == '':
        print ('Nao sera inserida a fase Transferencia!! \n')
    else:
        print ('Adicionando fase Transferencia!! \n')
        arq.writelines(valida_transferencia)
        arq.writelines("\n \n")

    if encerrar == '':
        print ('Nao sera inserida a fase Encerrar!! \n')
    else:
        print ('Adicionando fase Encerrar!! \n')
        arq.writelines(encerrar)
        arq.writelines("\n \n")

    arq.writelines(fase_hangup)
    arq.close()

    agente_criado = '1'
    return agente_criado
