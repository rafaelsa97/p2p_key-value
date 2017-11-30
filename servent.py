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
import mtd_servent

nome_arquivo = "services"
arquivo = open(nome_arquivo)
while arquivo:
	chave, valor = mtd_servent.obtem_chave_valor(arquivo)
	print chave
	print valor
arquivo.close()