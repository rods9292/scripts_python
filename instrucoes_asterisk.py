lista_linhas = {
'1':'same => n,GoSub(TOCA_PROMPT_V2,s,1(fase,1))',
'2':'same => n(retry),GoSub(TOCA_PROMPT_V2,s,1(fase,1))',
'3':'same => n,GoSub(TOCA_PROMPT_V2,s,1(fase,1,,,1,4))',
'4':'same => n(retry),GoSub(TOCA_PROMPT_V2,s,1(fase,1,,,1,4))',
'5':'same => n,GoSub(TOCA_PROMPT_V2,s,1(fase,2))',
'6':'same => n,GoSub(TOCA_PROMPT_V2,s,1(fase,3))',
'7':'same => n,GoSub(EXECUTA_VOCALIZAR,s,1(nome,${HASH(DADOS_CLIENTE,NOME_VOCALIZAR)}))',
}
