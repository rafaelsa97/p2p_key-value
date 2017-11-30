# -*- coding: utf-8 -*-

# ============================== P2P - Cliente ==============================
# Programa de chat desenvolvido para a disciplina de Redes de Computadores
# UNIVERSIDADE FEDERAL DE MINAS GERAIS
# Desenvolvido por Bhryan Henderson Lopes Perpétuo e Rafael Santos de Almeida
# Dezembro de 2017
# ===========================================================================

import sys
import socket
import struct
import mtd_servent

nome_arquivo = "teste"
arquivo = open(nome_arquivo)
while True:
	aux = arquivo.readline()
	if aux == '':
		break
	chave, valor = mtd_servent.obtem_chave_valor(aux)
	if chave != None and valor != None:
		print chave + valor
num_linhas = mtd_servent.conta_linhas(arquivo)
arquivo.close()