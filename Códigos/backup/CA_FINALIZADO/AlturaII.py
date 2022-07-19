import matplotlib.pyplot as plt
import time #biblioteca para determinar o tempo de execução
import random #para gerar números aleatórios no vetor
import numpy as np #biblioteca externa para realizar diversas operação númericas
#usada inclusivamente neste código para gerar o vetor 
import datetime #para formatar a quantidade de tempo para horas:minutos:segundos
from Algoritmos import Algoritmos  

arquivo = open('resultadoAlturaII.txt', 'a')

for i in range(0, 100):
    tamanho = i+1
    limiteInferior = -100   #determina o limite inferior de valores onde os aleatórios pode serem gerados
    limiteSuperior = 100    #determina o limite superior de valores onde os aleatórios pode serem gerados
    vetor = np.random.randint(limiteInferior, limiteSuperior, tamanho)  #criação do vetor com números aleatórios
    print("tamanho: " + str(tamanho))
    print("Vetor Criado:")
    print(vetor)    #imprime o vetor
    start = time.perf_counter() #inicia a contagem do timer
    somaMaxima = Algoritmos.alturaII(vetor)  #chama o metódo de primeiro algoritmo
    end = time.perf_counter()   #encerra o timer
    duracao = end - start   #determina a quantidade de tempo gasta em segundos
    print("Tempo de duração: " + str(duracao)) #impressão do tempo de execução
    print("O valor da altura é: " + str(somaMaxima)+"\n")    #impressão do segmento de soma máxima
    arquivo.write(str(tamanho) + "\t\t")
    arquivo.write(str(duracao) + "\n")   
    plt.scatter(tamanho, duracao)
    
plt.xlabel('Entradas')
plt.ylabel('Tempo(s)')
plt.show()
arquivo.close