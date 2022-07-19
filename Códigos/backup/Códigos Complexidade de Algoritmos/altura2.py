
def alturaII(vetor):
    x = vetor[0]
    for q in range(1, len(vetor)):
        s = 0
        for j in range(q, 1, -1):
            s = s + vetor[j]
            if s > x:
                x = s
    return x


vetor = [-25, -20, -23, -74, 51, 52]
print("Soma Máxima:" + str(alturaII(vetor)))