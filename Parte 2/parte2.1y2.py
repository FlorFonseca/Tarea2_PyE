from math import gcd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#1y2
#Decidimos evaluar la restricción de que el mcd de a y m fuera igual a 1 y que la semilla perteneciera a los numeros naturales

def algoritmoPseudoaleatorio(a, c ,m, cantSimulaciones):
    x = 1550
    #El valor de x corrsponde al horario de la comuptadora
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
    else:
        print("Error: parámetros inválidos")
        return []
    
muestra = algoritmoPseudoaleatorio(1664525, 1013904223,4294967296, 100)
print(muestra)

#Usamos Matplot y Seaborn para hacer el histograma de los datos, junto con su curva de densidad.
plt.hist(muestra, bins=15, color='blue', edgecolor='black', density=True)
#Density= true normaliza el histograma
sns.kdeplot(muestra, bw_adjust=0.5, color='red', label='Densidad estimada', fill=True)
plt.xticks(np.linspace(0,1, 21))
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.title('Histograma')
plt.legend()
plt.show()