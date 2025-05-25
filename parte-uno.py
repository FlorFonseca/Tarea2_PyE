from collections import Counter

cancelaciones_por_dia = []

with open('cancelaciones.csv', 'r') as archivo:
    next(archivo)  # Saltar la primera línea (encabezados)
    for linea in archivo:
        partes = linea.strip().split(',')
        if len(partes) >= 2:
            cancelaciones_por_dia.append(int(partes[1]))

# calcular frecuencia absoluta
freq_abs = Counter(cancelaciones_por_dia)

# obtener los valores únicos y ordenados
valores_unicos = sorted(freq_abs.keys())

# calcular total de cancelaciones
total_cancelaciones = len(cancelaciones_por_dia)

tabla = []
for valor in valores_unicos:
    freq_abs_valor = freq_abs[valor]
    prob = freq_abs_valor / total_cancelaciones
    tabla.append((valor, freq_abs_valor, prob))

# calcular distribución acumulada
acumulada = 0
tabla_completa = []
for i, (valor, freq_abs_valor, prob) in enumerate(tabla):
    acumulada += prob
    tabla_completa.append((valor, freq_abs_valor, prob, acumulada))

# imprimir tabla
print("\nTabla de Frecuencias de Cancelaciones Diarias")
print("-" * 60)
print(f"{'Cancelaciones':<15} {'Frec.Abs.':<12} {'Prob.Emp.':<12} {'Dist.Acum.'}")
print("-" * 60)
for fila in tabla_completa:
    print(f"{fila[0]:<15} {fila[1]:<12} {fila[2]:<12.4f} {fila[3]:<12.4f}")

esperanza = sum(valor * prob for valor, _, prob, _ in tabla_completa)
varianza = sum(valor**2 * prob for valor, _, prob, _ in tabla_completa) - esperanza**2

print(f"\nEsperanza: {esperanza:.4f}")
print(f"Varianza: {varianza:.4f}")

cancelaciones_ordenadas = sorted(cancelaciones_por_dia)
n = len(cancelaciones_ordenadas)

# se que n es par porque el número de días es par
mediana = (cancelaciones_ordenadas[n // 2 - 1] + cancelaciones_ordenadas[n // 2]) / 2
print(f"\nMediana: {mediana}")

def calcular_cuartiles(datos):
    n = len(datos)
    
    # Cálculo de Q1 (percentil 25)
    q1_pos = 0.25 * (n + 1)
    if q1_pos.is_integer():
        q1 = datos[int(q1_pos) - 1]
    else:
        parte_entera = int(q1_pos)
        fraccion = q1_pos - parte_entera
        q1 = datos[parte_entera - 1] + fraccion * (datos[parte_entera] - datos[parte_entera - 1])
    
    # Cálculo de Q3 (percentil 75)
    q3_pos = 0.75 * (n + 1)
    if q3_pos.is_integer():
        q3 = datos[int(q3_pos) - 1]
    else:
        parte_entera = int(q3_pos)
        fraccion = q3_pos - parte_entera
        q3 = datos[parte_entera - 1] + fraccion * (datos[parte_entera] - datos[parte_entera - 1])
    
    return q1, q3

Q1, Q3 = calcular_cuartiles(cancelaciones_ordenadas)
rango_intercuartil = Q3 - Q1

print(f"\nRango intercuartil: {rango_intercuartil}")

