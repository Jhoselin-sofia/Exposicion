import numpy as np
def euler_method(f, t0, y0, h, t_end):
    # Crear listas para almacenar resultados
    t_vals = [t0]
    y_vals = [y0]
    # Iterar mientras t sea menor que t_end
    t, y = t0, y0
    while t < t_end:
        y += h * f(t, y)  # Fórmula de Euler
        t += h
        t_vals.append(t)
        y_vals.append(y)
    return t_vals, y_vals
# Definir la función derivada f(t, y) = cos(2t) + sin(3t)
def f(t, y):
    return np.cos(2 * t) + np.sin(3 * t)
# Parámetros iniciales
t0 = 0       # Valor inicial de t
y0 = 1       # Valor inicial de y
h = 0.1      # Tamaño del paso
t_end = 0.4  # Calcular hasta t = 0.4
# Resolver usando el método de Euler
t_vals, y_vals = euler_method(f, t0, y0, h, t_end)

# Imprimir resultados
print("t\t\ty (Euler)")
for t, y in zip(t_vals, y_vals):
    print(f"{t:.2f}\t\t{y:.6f}")
