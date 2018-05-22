## QUESTÃO 2 ##
#
# Escreva um programa para calcular a frequencia das palavras de uma entrada. 
# A saída deve mostrar a frequencia depois de ordenar a chave alfanumericamente.
# Suponha que a seguinte entrada seja fornecida ao programa:
#     New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
#
# Então, a saída deve ser:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    frase= input('Digite qualquer coisa aqui: ').split()
    lista = []
    l = []

    for i in frase:
        lista.append("{}:{}".format(i,frase.count(i)))

    for i in lista:
            if i not in l:
                l.append(i)

    print(l)



if __name__ == '__main__':
    main()
