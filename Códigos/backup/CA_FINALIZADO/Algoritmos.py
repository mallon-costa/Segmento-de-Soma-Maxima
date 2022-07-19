#--------------------UNIVERSIDADE FEDERAL DO SUL E SUDESTE DO PARÁ-------------------------
# COMPLEXIDADE DE ALGORITMOS - IMPLEMENTAÇÃO DE 4 ALGORITMOS DE SEGMENTO DE SOMA MÁXIMA
#PROFESSOR MANOEL RIBEIRO
#ALUNOS:
#AMANDA SAVINO
#BEATRIZ CAVALCANTE
#MANOEL MALON COSTA
#------------------------------------------------------------------------------------------

#Esta classe contém os métodos para calcular cada um dos algoritmos de segmento
#de soma máxima e são todos estáticos para não precisar instanciar um objeto 
#para chamar um metódo
class Algoritmos:
#-------------------------------------------------------------------------------
    #PRIMEIRO ALGORITMO
    #teta(n³) = n*n*n
    @staticmethod
    def alturaI(vetor):
        x = vetor[0]
        for i in range(0, len(vetor)):
            for k in range(i, len(vetor)):
                s = 0
                for j in range(i, k+1):
                    s = s + vetor[j]
                if s > x:
                    x = s
        return x
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
    #SEGUNDO ALGORITMO
    #teta(n²) = n*n
    @staticmethod
    def alturaII(vetor):
        x = vetor[0]
        for q in range(1, len(vetor)): #
            s = 0
            for j in range(q, 1, -1):
                s = s + vetor[j]
                if s > x:
                    x = s
        return x
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
    #método responsável por determinar o maior número entre 3 - necessário
    #para executar a alturaIII
    @classmethod
    def max(cls, num1, num2, num3):
        if num3 == None:
            num3 = 0
        if num2 == None:
            num3 = 0
        if num1 == None:
            num3 = 0
        
        if num1 > num2 and num1 > num3:
            return cls.num1
        if num2 > num1 and num2 > num3:
            return cls.num2
        if num3 > num1 and num3 > num2:
            return cls.num3

    #TERCEIRO ALGORITMO
    #teta(nlogn)
    @staticmethod
    def alturaIII(vetor, p, r):
        if p == r:
            return vetor[p]
        else:
            q = (p+r)//2
            x1 = Algoritmos.alturaIII(vetor, p, q) #T(n/2)
            x2 = Algoritmos.alturaIII(vetor, q+1, r) #T(n/2)
            y1 = s = vetor[q]
            for i in range(q-1, p, -1): #n/2
                s = vetor[i] + s
                if s > y1:
                    y1 = s
            y2 = s = vetor[q+1]
            for j in range(q+2, r): #n/2
                s = s + vetor[j]
                if s > y2:
                    y2 = s
            x = max(x1, y1 + y2, x2)
            return x
        #Equaçao: T(n) = T(n/2) + T(n/2) + n/2 + n/2
        #T(n) = 2T(n/2) + n => Pela Tabela => T(n) = teta(nlogn)
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
    #QUATRO ALGORITMO
    #Teta(n)
    @staticmethod
    def alturaIV(vetor):
        n = len(vetor)
        semi = vetor.copy()
        semi[0] = vetor[0]
        for q in range(1, n): # T(n) = n
            if semi[q-1] >= 0:
                semi[q] = semi[q-1]+vetor[q]
            else:
                semi[q] = vetor[q]
        x = semi[0]
        for q in range(2, n): # T(n) = n
            if semi[q] > x:
                x = semi[q]
        return x
#-------------------------------------------------------------------------------
