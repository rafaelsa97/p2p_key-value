# -*- coding: utf-8 -*-

# ============================== P2P - Servent ==============================
# Programa de chat desenvolvido para a disciplina de Redes de Computadores
# UNIVERSIDADE FEDERAL DE MINAS GERAIS
# Desenvolvido por Bhryan Henderson Lopes Perpétuo e Rafael Santos de Almeida
# Dezembro de 2017
# ===========================================================================

import sys
import socket
import struct
import mtd_servent

mtd_servent.parametros_entrada(sys.argv)

porto, nome_arquivo, servents = mtd_servent.parametros_entrada(sys.argv)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Cria socket UDP
s.bind(('localhost',porto))

arquivo = open(nome_arquivo)
n_chaves = mtd_servent.conta_linhas(arquivo) # Salva o número de linhas contidas no arquivo
lista = [ [ 0 for i in range(3) ] for j in range(n_chaves) ] # Cria lista com tamanho exato para caber todas as chaves
c = 0 # Contador auxiliar

# Lê as chaves e os valores do arquivo:
while True:
	aux = arquivo.readline() #Lê uma linha do arquivo
	if aux == '': # Encerra o laço se chegou ao final do arquivo
		break
	chave, valor = mtd_servent.obtem_chave_valor(aux)
	# Adiciona a chave e o valor em uma lista:
	if chave != None and valor != None:
		lista, c = mtd_servent.add_lista_chave_valor(lista, c, chave, valor)
		c = c + 1
n_chaves  = c
historico = []
nseq      = None

# Trata as mensagem recebidas:
while True:
	aux, addr = s.recvfrom(1024)
	print "Endereço do cliente: " + str(addr[0]) + " " + str(addr[1])
	tipo_msg  = struct.unpack('!H',aux[0:2])[0]
	if tipo_msg == 5: # KEYREQ
		nseq, chave, historico = mtd_servent.KEYREQ(aux, addr, s, lista, servents, historico)
	if tipo_msg == 7: # KEYFLOOD
		nseq, chave, historico, addr = mtd_servent.recebe_KEYFLOOD(aux, lista, s, historico, servents)

arquivo.close()