import math
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from math import gcd

def algoritmoPseudoaleatorio(a, c, m, cantSimulaciones):
    semilla = 10
    if gcd(a, m) == 1 and semilla > 0:
        resultados = []
        for i in range(cantSimulaciones):
            semilla = (a * semilla + c) % m
            resultado = semilla / m
            resultados.append(resultado)
        return resultados
    else:
        print("Error: parámetros inválidos")
        return []

def transformar_a_cauchy(lista_uniformes):
    resultados = []
    for u in lista_uniformes:
        x = math.tan(math.pi * (u - 0.5))
        resultados.append(x)
    return resultados

def densidad_cauchy(x):
    return 1 / (math.pi * (1 + x**2))

uniformes = algoritmoPseudoaleatorio(a=117, c=223, m=200, cantSimulaciones=100)
muestra_cauchy = transformar_a_cauchy(uniformes)

plt.figure(figsize=(10, 6))
plt.hist(muestra_cauchy, bins=30, density=True, color='orange', edgecolor='black', label='Muestra simulada')
sns.kdeplot(muestra_cauchy, bw_adjust=0.5, color='red', label='Densidad estimada', fill=True)
x_vals = np.linspace(-10, 10, 1000)
y_vals = [densidad_cauchy(x) for x in x_vals]
plt.plot(x_vals, y_vals, color='blue', label='Densidad teórica Cauchy')
plt.title("Distribución Cauchy estándar (muestra de 100)")
plt.xlabel("Valor")
plt.ylabel("Densidad")
plt.legend()
plt.grid(True)
plt.show()