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

# parametros_entrada(argumentos_de_entrada)
# Obtém os argumentos de entrada digitados pelo usuário
# Saída: número de porto do programa, nome do arquivo de chaves e lista com endereços de servents
def parametros_entrada(argumentos):
	if len(argumentos) < 5:
		print "ERRO!\nQuantidade insuficiente de argumentos. Tente novamente."
		sys.exit(0)
	porto        = int(argumentos[2])
	nome_arquivo = argumentos[3]
	# Inicializa a lista de endereços de outros servents:
	servents = [ [ 0 for i in range(3) ] for j in range(len(argumentos) - 4) ]
	for i in range(len(argumentos) - 4): # Salva índice, IP e porto passado por parâmetro
		servents[i][0] = i 									  # Índice
		servents[i][1] = argumentos[i + 4].split(':')[0]      # IP
		servents[i][2] = int(argumentos[i + 4].split(':')[1]) # Porto
	return porto, nome_arquivo, servents

# obtem_chave_valor(linha_lida_do_arquivo)
# Obtém a chave e o valor de uma linha lida do arquivo
# Saída: chave e valor da linha
def obtem_chave_valor(aux):
	if aux[0] != '#' and aux != '\n':		# Salva chave contida no arquivo
		linha  = aux.split()
		chave  = linha[0]
		aux2   = aux.lstrip(linha[0])
		aux2   = aux2.replace('\n', '')
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
def add_lista_chave_valor(lista, c, chave, valor):
	for i in range(c):
		if lista[i][1] == chave: # Confere se há uma chave de mesmo nome na lista
			lista[i][1] = chave
			lista[i][2] = valor
			del lista[c]
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
		if lista[i][1] == chave_procurada: # Verifica se chave foi encontrada
			print "Chave encontrada!"
			return lista[i][2]
	print "Chave não encontrada."
	return None

# KEYREQ(dados_recebidos, endereco_do_cliente, socket)
# Obtém o número de sequência e a chave a partir dos dados recebidos do cliente
# Saída: número de sequência e chave
def KEYREQ(dados, addr, socket, lista, n_chaves, servents):
	nseq = struct.unpack('!I', dados[2:6])[0]
	chave = dados[6:]
	valor = busca_chave(lista, chave, n_chaves) 		   # Busca se a chave está em sua lista
	envia_KEYFLOOD(3, nseq, addr, chave, socket, servents) # Alaga para os outros servents
	if valor != None:
		RESP(nseq, valor, addr, socket)
	return nseq, chave

# envia_KEYFLOOD(time_to_live, num_sequência, addr_do_cliente,chave_para_buscar, socket, addrs_de_servents)
# Monta mensagem de tipo KEYFLOOD e envia para todos os servents descobertos
# Saída: ---//---
def envia_KEYFLOOD(TTL, nseq, addr, chave, socket, servents):
	pack_tipo     = struct.pack('!H',7)
	pack_TTL      = struct.pack('!H',TTL)
	pack_nseq     = struct.pack('!I',nseq)
	#pack_IP_clt   = struct.pack('!B',addr[0])
	pack_port_clt = struct.pack('!H',addr[1])
	#mensagem = pack_tipo + pack_TTL + pack_nseq + pack_IP_clt + pack_port_clt + chave
	mensagem = pack_tipo + pack_TTL + pack_nseq + pack_port_clt + chave
	print mensagem
	c = 0
	for i in servents:
		socket.sendto(mensagem, (i[1], i[2]))
		c = c + 1

def recebe_KEYFLOOD(dados):
	TTL           = struct.unpack('!H', dados[2:4])
	nseq          = struct.unpack('!I', dados[4:8])
	#IP_cliente    = struct.unpack('!I', dados[8:12])
	porto_cliente = struct.unpack('!H', dados[8:10])
	chave         = dados[10:]
	print "Dados recebidos por KEYFLOOD:"
	#print TTL + " " + nseq + " " + IP_cliente + " " + porto_cliente + " " + chave
	print str(TTL) + " " + str(nseq) + " " + str(porto_cliente) + " " + chave
	return nseq, chave

# RESP(num_sequência, valor, endereço_do_cliente, socket)
# Envia resposta para o cliente no formato do protocolo
# Saída: ---//---
def RESP(nseq, valor, addr, socket):
	pack_tipo = struct.pack('!H',9)
	pack_nseq = struct.pack('!I',nseq)
	socket.sendto(pack_tipo + pack_nseq + valor, addr)