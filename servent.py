# -*- coding: utf-8 -*-

# ===========================================================================
# Programa de chat desenvolvido para a disciplina de Redes de Computadores
# UNIVERSIDADE FEDERAL DE MINAS GERAIS
# Desenvolvido por Bhryan Henderson Lopes Perpétuo e Rafael Santos de Almeida
# Dezembro de 2017
# ===========================================================================

import sys
import socket
import struct

nome_arquivo = "services"
arquivo = open(nome_arquivo)
while True:
	aux = arquivo.readline()
	if aux == '':	 # Encerra se chegou ao final do arquivo
		break
	elif aux[0] != '#' and aux != '\n':		# Salva chave contida no arquivo
		linha = aux.split()
		chave = linha[0]
		aux2 = aux.lstrip(linha[0])
		if aux2[0] == '\t':
			aux2 = aux2.lstrip('\t')
arquivo.close()