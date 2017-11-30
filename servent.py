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

IP = '127.0.0.1'
PORTO = 51515
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Cria socket UDP
endereco = (IP, PORTO) # Endereço local do programa

nome_arquivo = "teste"
arquivo = open(nome_arquivo)
num_chaves = mtd_servent.conta_chaves(arquivo) # Salva o número de chaves contidas no arquivo
lista = [ [ 0 for i in range(3) ] for j in range(num_chaves) ] # Cria lista com tamanho exato para caber todas as chaves
c = 0 # Contador auxiliar

while True:
	aux = arquivo.readline()
	if aux == '':
		break
	chave, valor = mtd_servent.obtem_chave_valor(aux)
	if chave != None and valor != None:
		lista, c = mtd_servent.add_lista_chave_valor(lista, c, chave, valor)
		c = c + 1

num_chaves = c
print num_chaves
print lista

arquivo.close()