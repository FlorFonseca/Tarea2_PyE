from math import gcd
import openpyxl
#1y2
def algoritmoPseudoaleatorio(a, c ,m, cantSimulaciones):
    x = 10
    semilla : int = int(x)
    if gcd(a, m) == 1 and semilla > 0:
        resultados = []
        while cantSimulaciones > 0:
            x = (a * semilla + c) % m
            semilla = x
            resultado = x / m
            resultados.append(resultado)
            cantSimulaciones -= 1
        return resultados
    
muestra = algoritmoPseudoaleatorio(117, 223, 200, 100)
print(muestra)


