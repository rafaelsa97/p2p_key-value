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

nome_arquivo = "teste.txt"
arquivo = open(nome_arquivo)
while True:
	aux = arquivo.readline()
	if aux == '':			# Encerra se chegou ao final do arquivo
		break
	elif aux[0] != '#':		# Salva chave contida no arquivo
		sys.stdout.write(aux); sys.stdout.flush()
arquivo.close()