# Parámetros del Modelo de Bass
M = 1000000  # Población total (personas)
p = 0.03     # Coeficiente de innovación
q = 0.38     # Coeficiente de imitación
N0 = 0       # Valor inicial (nadie ha visto la película aún)
h = 1        # Paso de tiempo en meses
t_max = 11   # Tiempo total a simular (en meses)
# Derivada dN/dt del Modelo de Bass
def tasa_adopcion(t, N):
    return p * (M - N) + q * (N / M) * (M - N)
# Método de Euler
def metodo_euler(N0, h, t_max):
    t = 0
    N = N0
    resultados = [(t, N, tasa_adopcion(t, N))]  # Lista para guardar los resultados
    while t <= t_max:
        f_t_N = tasa_adopcion(t, N)  # Calcula la tasa de adopción actual
        N = N + h * f_t_N  # Actualiza N usando el método de Euler
        t += h             # Incrementa el tiempo
        resultados.append((t, N, f_t_N))  # Guarda los resultados
    return resultados
# Ejecutar el método de Euler
resultados = metodo_euler(N0, h, t_max)
# Imprimir los resultados en formato tabular
print(f"{'t (mes)':<10}{'N (personas)':<15}{'Tasa de adopción':<20}")
for t, N, f_t_N in resultados:
    print(f"{t:<10.1f}{N:<15.1f}{f_t_N:<20.1f}")
