# -*- coding: utf-8 -*-

# ============================ P2P - mtd_servent ============================
# Programa de chat desenvolvido para a disciplina de Redes de Computadores
# UNIVERSIDADE FEDERAL DE MINAS GERAIS
# Desenvolvido por Bhryan Henderson Lopes Perpétuo e Rafael Santos de Almeida
# Dezembro de 2017
# ===========================================================================

import sys
import socket
import struct

# obtem_chave_valor(linha_lida_do_arquivo)
# Obtém a chave e o valor de uma linha lida do arquivo
# Saída: chave e valor da linha
def obtem_chave_valor(aux):
	if aux[0] != '#' and aux != '\n':		# Salva chave contida no arquivo
		linha = aux.split()
		chave = linha[0]
		aux2 = aux.lstrip(linha[0])
		aux2 = aux2.replace('\n', '')
		while aux2[0] == '\t':
			aux2 = aux2.lstrip('\t')
		return chave, aux2
	else:
		return None, None

# conta_linhas(arquivo_que_contém_as_chaves_e_valores)
# Conta número de chaves contidas no arquivo
# Saída: número de chaves
def conta_linhas(arquivo):
	c = 0
	while True:
		aux = arquivo.readline()
		if aux == '':	 # Encerra se chegou ao final do arquivo
			arquivo.seek(0,0)
			return c
		elif aux[0] != '#' and aux != '\n':
			c = c + 1

# add_lista_chave_valor(lista_a_add_chave_e_valor, contador, chave, valor)
# Adiciona as chaves e valores lidos do arquivo em uma lista
# Saída: lista com chaves e valores adicionados
def add_lista_chave_valor(lista,c, chave, valor):
	for i in range(c):
		if lista[i][1] == chave:
			lista[i][1] = chave
			lista[i][2] = valor
			c = c -1
			return lista, c
	lista[c][0] = c
	lista[c][1] = chave
	lista[c][2] = valor
	return lista, c

# busca_chave(lista_de_chaves_e_valores, chave_procurada, numero_de_chaves)
# Procura se a chave procurada está na sua memória
# Saída: valor atrelado à chave procurada em caso de sucesso
def busca_chave(lista, chave_procurada, n_chaves):
	for i in range(n_chaves):
		if lista[i][1] == chave_procurada:
			print "Chave encontrada!"
			return lista[i][2]
	print "Chave não encontrada."
	return None

# KEYREQ(dados_recebidos)
# Obtém o número de sequência e a chave a partir dos dados recebidos do cliente
# Saída: número de sequência e chave
def KEYREQ(dados):
	nseq = struct.unpack('!I', dados[2:6])[0]
	chave = dados[6:]
	return nseq, chave