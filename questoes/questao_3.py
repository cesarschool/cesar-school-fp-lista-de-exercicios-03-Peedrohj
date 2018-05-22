## QUESTÃO 3 ##
#
# Um robô se move em um plano a partir do ponto original (0,0). O robô pode se 
# mover nas direções CIMA, BAIXO, ESQUERDA e DIREITA de acordo com um 
# passo fornecido. O traço do movimento do robô é mostrado da seguinte forma:
#
# CIMA 5
# BAIXO 3
# ESQUERDA 3
# DIREITA 2
#
# Os números após a direção são passos. 
# Escreva um programa para calcular a distância entre a posição atual e o 
# ponto original após uma seqüência de movimentos. Se a distância for um 
# float, basta imprimir o inteiro mais próximo.
# Exemplo:
# Se as seguintes tuplas são dadas como entrada para o programa:
# 
# CIMA 5
# BAIXO 3
# ESQUERDA 3
# DIREITA 2
#
# Então, a saída do programa deve ser:
# 2
# 
# Dicas:
# As entradas devem ser lidas do console até que um valor vazio seja digitado. 
# A saída deve ser um inteiro que representa a distancia para o ponto original. 
# Entradas inválidas devem ser descartadas da contagem.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    altura = 0
lado = 0 
lista = []

while True:
        print("Me informe a posição: ")
        valor = input(">>").upper()   
	if valor != '':
		for i in valor:
                        if 'CIMA' in valor:
				for x in valor:
				    if x.isdigit():
				        soma += int(x)
						altura = altura + soma
					break
			if 'BAIXO' in valor:
				for x in valor:
				    if x.isdigit():
				        soma += int(x)
						altura = altura - soma
					break

			if 'ESQUERDA' in valor:
				for x in valor:
				    if x.isdigit():
				        soma += int(x)
						lado = lado - soma
					break

			if 'DIREITA' in valor:
				for x in valor:
				    if x.isdigit():
				        soma += int(x)
						lado = lado + soma
					break
	else:
		break

dist = ((lado ** 2) + (altura ** 2)) ** 1/2
print(dist)



    
if __name__ == '__main__':
    main()
