# -*- coding: utf-8 -*-

# obtem_chave_valor(arquivo_a_ser_lido)
# Lê um arquivo indicado e obtém a chave e o valor de uma linha
# Saída: chave e valor da linha
def obtem_chave_valor(arquivo):
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
			return chave, aux2