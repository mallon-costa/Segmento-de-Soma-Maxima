
import numpy as np

def altura(vetor):
    print(len(vetor))
    x = vetor[0]
    for i in range(0, len(vetor)):
        for k in range(i, len(vetor)):
            s = 0
            for j in range(i, k+1):
                s = s + vetor[j]
            if s > x:
                x = s
    return x

tamanho = 6
limiteInferior = -100
limiteSuperior = 100
vetor = np.random.randint(limiteInferior, limiteSuperior, tamanho)
print(vetor)

#vetor = [-25, -20, -23, -74, 51, 52]
print("Soma Máxima:" + str(altura(vetor)))