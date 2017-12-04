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

endereco = ('127.0.0.1', 51515) # Endereço local do programa
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Cria socket UDP
s.bind(endereco)

nome_arquivo = "teste"
arquivo = open(nome_arquivo)
num_chaves = mtd_servent.conta_linhas(arquivo) # Salva o número de linhas contidas no arquivo
lista = [ [ 0 for i in range(3) ] for j in range(num_chaves) ] # Cria lista com tamanho exato para caber todas as chaves
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
num_chaves = c

# Trata as mensagem recebidas:
while True:
	aux, addr = s.recvfrom(1024)
	tipo_msg  = struct.unpack('!H',aux[0:2])[0]
	if tipo_msg == 5: # KEYREQ
		nseq, chave = mtd_servent.KEYREQ(aux, addr, s)
	print nseq
	print chave
chave_procurada = mtd_servent.busca_chave(lista, "daytime", num_chaves)

arquivo.close()