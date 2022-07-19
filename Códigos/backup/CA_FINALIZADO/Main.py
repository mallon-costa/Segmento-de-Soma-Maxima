#--------------------UNIVERSIDADE FEDERAL DO SUL E SUDESTE DO PARÁ---------------------------------------------
# COMPLEXIDADE DE ALGORITMOS - IMPLEMENTAÇÃO DE 4 ALGORITMOS DE SEGMENTO DE SOMA MÁXIMA
#PROFESSOR MANOEL RIBEIRO
#ALUNOS:
#AMANDA SAVINO
#BEATRIZ CAVALCANTE
#MANOEL MALON COSTA

#-------------------------------PROGRAMA PRINCIPAL-------------------------------------------------------------

#------------------------IMPORTAÇÃO DAS BIBLIOTECAS------------------------------------------------------------
import time #biblioteca para determinar o tempo de execução
import random #para gerar números aleatórios no vetor
import numpy as np #biblioteca externa para realizar diversas operação númericas
#usada inclusivamente neste código para gerar o vetor 
import datetime #para formatar a quantidade de tempo para horas:minutos:segundos

from Algoritmos import Algoritmos  #importação da classe onde tem os métodos  

#-----------------------INICIAÇÃO DO PROGRAMA-------------------------------------------------------------------
#essa função abre o arquivo denominado "resultado.txt", se não tiver no diretório
#é criado o arquivo com este mesmo nome
#não tem o nome das colunas afim de melhorar o tratamento dos dados, porém
#é na seguinte ordem em relaçao ao tempo de execução: 
#tamanho    alturaI   alturaII  alturaIII   alturaIV

while(True):
    arquivo = open('resultado.txt', 'a')
    #recebe um valor inteiro do usuário
    tamanho = int(input("Digite o tamanho da entrada: "))
    limiteInferior = -100   #determina o limite inferior de valores onde os aleatórios pode serem gerados
    limiteSuperior = 100    #determina o limite superior de valores onde os aleatórios pode serem gerados
    vetor = np.random.randint(limiteInferior, limiteSuperior, tamanho)  #criação do vetor com números aleatórios
    print("Vetor Criado:")
    print(vetor)    #imprime o vetor
    arquivo.write(str(tamanho) + "\t\t")    #escreve uma mensagem no arquivo txt
    #------------------------------------------------------------------------------------------------------------------

    #-------------------------TODOS OS BLOCOS SEGUEM A MESMA LÓGICA----------------------------------------------------
    #BLOCO DE EXECUÇÃO DO PRIMEIRO ALGORITMO
    print("\n-------------Execução do Primeiro Algoritmo O(n³)-------------") 
    start = time.perf_counter() #inicia a contagem do timer
    somaMaxima = Algoritmos.alturaI(vetor)  #chama o metódo de primeiro algoritmo
    end = time.perf_counter()   #encerra o timer
    duracao = end - start   #determina a quantidade de tempo gasta em segundos
    duracao = datetime.timedelta(seconds = duracao) #formata para horas:minutos:segundos
    print("Tempo de duração: " + str(duracao)) #impressão do tempo de execução
    print("O valor da altura é: " + str(somaMaxima))    #impressão do segmento de soma máxima
    arquivo.write(str(duracao) + "\t\t")    #escreve o tempo de execução e faz tabulação
    #------------------------------------------------------------------------------------------------------------------

    #------------------------------------------------------------------------------------------------------------------
    #BLOCO DE EXECUÇÃO DO SEGUNDO ALGORITMO
    print("\n-------------Execução do Segundo Algoritmo O(n²)-------------")
    start = time.perf_counter()
    somaMaxima = Algoritmos.alturaII(vetor)
    end = time.perf_counter()
    duracao = end - start
    duracao = datetime.timedelta(seconds = duracao)
    print("Tempo de duração: " + str(duracao))
    print("O valor da altura é: " + str(somaMaxima))
    arquivo.write(str(duracao) + "\t\t")
    #------------------------------------------------------------------------------------------------------------------

    #------------------------------------------------------------------------------------------------------------------
    #BLOCO DE EXECUÇÃO DO TERCEIRO ALGORITMO
    print("\n-------------Execução do Terceiro Algoritmo O(nlogn)-------------")
    start = time.perf_counter()
    somaMaxima = Algoritmos.alturaIII(vetor, 0, len(vetor)-1)
    end = time.perf_counter()
    duracao = end - start
    duracao = datetime.timedelta(seconds = duracao)
    print("Tempo de duração: " + str(duracao))
    print("O valor da altura é: " + str(somaMaxima))
    arquivo.write(str(duracao) + "\t\t")
    #------------------------------------------------------------------------------------------------------------------

    #------------------------------------------------------------------------------------------------------------------
    #BLOCO DE EXECUÇÃO DO QUATRO ALGORITMO
    print("\n-------------Execução do Quatro Algoritmo O(n)-------------")
    start = time.perf_counter()
    somaMaxima = Algoritmos.alturaIV(vetor)
    end = time.perf_counter()
    duracao = end - start
    duracao = datetime.timedelta(seconds = duracao)
    print("Tempo de duração: " + str(duracao))
    print("O valor da altura é: " + str(somaMaxima))
    arquivo.write(str(duracao) + "\n") #escreve o tempo de execução do quatro algoritmo e quebra uma linha
    #------------------------------------------------------------------------------------------------------------------

    arquivo.close #arquivo é fechado
    print("------------------------------------------------")
    print("1 - Entrar com outro nº de entradas")
    print("2 - Sair do programa")

    opcao = int(input("> "))
    if opcao == 1:
        continue
    elif (opcao == 2):
        break
    else:
        print("Opcao invalida!")

#------------------------------------FIM--------------------------------------------------------------------
