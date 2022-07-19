
def max(num1, num2, num3):
    if num3 == None:
        num3 = 0
    if num2 == None:
        num3 = 0
    if num1 == None:
        num3 = 0

    if num1 > num2 and num1 > num3:
        return num1
    if num2 > num1 and num2 > num3:
        return num2
    if num3 > num1 and num3 > num2:
        return num3

def alturaIII(vetor, p, r):
    if p == r:
        return vetor[p]
    else:
        q = (p+r)//2
        x1 = alturaIII(vetor, p, q)
        x2 = alturaIII(vetor, q+1, r)
        y1 = s = vetor[q]
        for i in range(q-1, p, -1):
            s = vetor[i] + s
            if s > y1:
                y1 = s
        y2 = s = vetor[q+1]
        for j in range(q+2, r):
            s = s + vetor[j]
            if s > y2:
                y2 = s
        x = max(x1, y1 + y2, x2)
        return x

#vetor = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
vetor = [-25, -20, -23, -74, 51, 52]
print("Soma Máxima:" + str(alturaIII(vetor, 0, len(vetor)-1)))
