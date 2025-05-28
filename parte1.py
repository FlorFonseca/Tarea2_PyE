import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def leer_datos():
    #devolver lista de numeros apartir de archivo csv
    datos = []
    with open('cancelaciones.csv', 'r') as f:
        next(f)  
        for linea in f:
            datos.append(int(linea.strip().split(',')[1]))
    return np.array(datos)

def calcular_frecuencias(datos):

    valores_unicos = sorted(set(datos))
    frecuencias = []
    for valor in valores_unicos:
        freq = sum(1 for x in datos if x == valor)
        frecuencias.append(freq)
    return np.array(valores_unicos), np.array(frecuencias)

def calcular_probabilidades_empiricas(frecuencias, n):

    return frecuencias / n

def calcular_distribucion_acumulada(prob_empiricas):
    return np.cumsum(prob_empiricas)

def calcular_estadisticas(datos):
    n = len(datos)
    
    media = sum(datos) / n
    varianza = sum((x - media) ** 2 for x in datos) / (n - 1)
    desv_std = np.sqrt(varianza)
    datos_ordenados = sorted(datos)
    
    if n % 2 == 0:
        mediana = (datos_ordenados[n//2 - 1] + datos_ordenados[n//2]) / 2
    else:
        mediana = datos_ordenados[n//2]
   
    def encontrar_cuartil(p):
        k = p * (n - 1)
        f = np.floor(k)
        c = np.ceil(k)
        if f == c:
            return datos_ordenados[int(k)]
        d0 = datos_ordenados[int(f)] * (c - k)
        d1 = datos_ordenados[int(c)] * (k - f)
        return d0 + d1
    
    q1 = encontrar_cuartil(0.25)
    q3 = encontrar_cuartil(0.75)
    rango_iq = q3 - q1
    
    return {
        'media': media,
        'varianza': varianza,
        'desv_std': desv_std,
        'mediana': mediana,
        'q1': q1,
        'q3': q3,
        'rango_iq': rango_iq
    }

def mostrar_resultados(valores, frecuencias, prob_empiricas, dist_acumulada, stats):
    n = len(datos)
    
    print("\nTabla de Frecuencias y Probabilidades:")
    print("=====================================")
    print("Valor | Frec. Absoluta | Prob. Empírica | Dist. Acumulada")
    print("-" * 60)
    
    for i in range(len(valores)):
        print(f"{valores[i]:^5d} | {frecuencias[i]:^14d} | {prob_empiricas[i]:^13.4f} | {dist_acumulada[i]:^14.4f}")
    
    print("\nEstadísticas:")
    print("============")
    print(f"Total de observaciones (n): {n}")
    print(f"Media muestral: {stats['media']:.2f}")
    print(f"Varianza muestral: {stats['varianza']:.2f}")
    print(f"Desviación estándar muestral: {stats['desv_std']:.2f}")
    print(f"Mediana: {stats['mediana']:.2f}")
    print(f"Primer cuartil (Q1): {stats['q1']:.2f}")
    print(f"Tercer cuartil (Q3): {stats['q3']:.2f}")
    print(f"Rango intercuartílico: {stats['rango_iq']:.2f}")

def crear_graficos(datos, valores, frecuencias, dist_acumulada, stats):
    plt.figure(figsize=(15, 5))
    
    # Histograma
    plt.subplot(1, 3, 1)
    plt.hist(datos, bins=len(valores), edgecolor='black')
    plt.title('Histograma de Frecuencias')
    plt.xlabel('Número de Cancelaciones')
    plt.ylabel('Frecuencia Absoluta')
    
    # Distribución acumulada empírica
    plt.subplot(1, 3, 2)
    plt.plot(valores, dist_acumulada, 'bo-')
    plt.title('Distribución Acumulada Empírica')
    plt.xlabel('Número de Cancelaciones')
    plt.ylabel('Probabilidad Acumulada')
    plt.grid(True)
    
    # Diagrama de cajas
    plt.subplot(1, 3, 3)
    plt.boxplot(datos, vert=False)
    plt.title('Diagrama de Cajas')
    plt.xlabel('Número de Cancelaciones')
    plt.grid(True)
    
    plt.tight_layout()

datos = leer_datos()
valores, frecuencias = calcular_frecuencias(datos)
prob_empiricas = calcular_probabilidades_empiricas(frecuencias, len(datos))
dist_acumulada = calcular_distribucion_acumulada(prob_empiricas)
stats = calcular_estadisticas(datos)

mostrar_resultados(valores, frecuencias, prob_empiricas, dist_acumulada, stats)
crear_graficos(datos, valores, frecuencias, dist_acumulada, stats)
plt.show() 