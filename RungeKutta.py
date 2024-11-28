# Parámetros del Modelo de Bass
M = 1000000  # Población total (personas)
p = 0.03     # Coeficiente de innovación
q = 0.38     # Coeficiente de imitación
N0 = 0       # Valor inicial (nadie ha visto la película aún)
h = 1        # Paso de tiempo en meses
t_max = 12   # Tiempo total a simular (en meses)
# Derivada dN/dt del Modelo de Bass
def tasa_adopcion(t, N):
    return p * (M - N) + q * (N / M) * (M - N)
# Método de Runge-Kutta de 4to orden
def metodo_runge_kutta(N0, h, t_max):
    t = 0
    N = N0
    resultados = [(t, N, tasa_adopcion(t, N))]  # Lista para guardar los resultados
    while t < t_max:
        # Cálculo de los coeficientes k1, k2, k3, k4
        k1 = h * tasa_adopcion(t, N)
        k2 = h * tasa_adopcion(t + h / 2, N + k1 / 2)
        k3 = h * tasa_adopcion(t + h / 2, N + k2 / 2)
        k4 = h * tasa_adopcion(t + h, N + k3)
        # Actualizar el valor de N y t
        N = N + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t += h
        resultados.append((t, N, tasa_adopcion(t, N)))
    return resultados
# Ejecutar el método de Runge-Kutta
resultados = metodo_runge_kutta(N0, h, t_max)
print(f"{'t (mes)':<10}{'N (personas)':<15}{'Tasa de adopción':<20}")
for t, N, f_t_N in resultados:
    print(f"{t:<10.1f}{N:<15.1f}{f_t_N:<20.1f}")
