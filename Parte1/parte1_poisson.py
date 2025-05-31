import numpy as np
import matplotlib.pyplot as plt
import math
from parte1 import leer_datos, calcular_estadisticas

def calcular_poisson(k, parametro_lambda):
    #P(X = k) = (λ^k * e^(-λ)) / k!
    return (parametro_lambda ** k * math.exp(-parametro_lambda)) / math.factorial(k)

def graficar_comparacion(datos, parametro_lambda):
    k_min, k_max = min(datos), max(datos)
    k_valores = np.arange(k_min, k_max + 1)
    prob_poisson = [calcular_poisson(k, parametro_lambda) for k in k_valores]
    
    # hacer histograma y superponer Poisson
    plt.figure(figsize=(10, 6))
    plt.hist(datos, bins=len(k_valores), density=True, alpha=0.7, 
            label='Datos observados', color='skyblue')
    plt.plot(k_valores, prob_poisson, 'ro-', 
            label=f'Poisson(λ={parametro_lambda:.2f})')
    
    plt.title('Comparación de Datos con Distribución de Poisson')
    plt.xlabel('Número de Cancelaciones')
    plt.ylabel('Densidad/Probabilidad')
    plt.legend()
    plt.grid(True)

def calcular_probabilidades(parametro_lambda):
    # P(X < 5) = P(X ≤ 4)
    prob_menos_5 = sum(calcular_poisson(i, parametro_lambda) for i in range(5))
    
    # P(X > 15) = 1 - P(X ≤ 15)
    prob_mas_15 = 1 - sum(calcular_poisson(i, parametro_lambda) for i in range(16))
    
    print("\nProbabilidades según el modelo Poisson:")
    print(f"P(X < 5) = {prob_menos_5:.4f}")
    print(f"P(X > 15) = {prob_mas_15:.4f}")

datos = leer_datos()
estadisticas = calcular_estadisticas(datos)
parametro_lambda = estadisticas['media']

print(f"\nMedia muestral (λ) = {parametro_lambda:.4f}")

# comparacion y probabilidades
graficar_comparacion(datos, parametro_lambda)
calcular_probabilidades(parametro_lambda)

plt.show() 