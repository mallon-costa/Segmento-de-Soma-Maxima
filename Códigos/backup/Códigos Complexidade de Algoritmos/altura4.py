import time
import random
import numpy as np
start = time.perf_counter()

def alturaIV(vetor, n):
    semi = vetor.copy()
    semi[0] = vetor[0]
    for q in range(1, n):
        if semi[q-1] >= 0:
            semi[q] = semi[q-1]+vetor[q]
        else:
            semi[q] = vetor[q]
    x = semi[0]
    for q in range(2, n):
        if semi[q] > x:
            x = semi[q]
    return x

tamanho = 6
limiteInferior = -100
limiteSuperior = 100
vetor = np.random.randint(limiteInferior, limiteSuperior, tamanho)
print(vetor) # [69, 47, 43, 64, 16]

vetor = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
print("Soma Máxima:" + str(alturaIV(vetor,len(vetor))))

end = time.perf_counter()
print(end - start)
