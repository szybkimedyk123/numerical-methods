import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    return -3 * y * t**2 + 3 * y

def analytical_solution(t):
    return 3 * np.exp(-t**3 + 3 * t)

def euler_method(t0, y0, tk, n):
    h = (tk - t0) / n
    t = np.linspace(t0, tk, n+1)
    y = np.zeros(n+1)
    y[0] = y0

    for i in range(n):
        y[i+1] = y[i] + h * f(t[i], y[i])

    return t, y

def heun_method(t0, y0, tk, n):
    h = (tk - t0) / n
    t = np.linspace(t0, tk, n+1)
    y = np.zeros(n+1)
    y[0] = y0

    for i in range(n):
        k1 = f(t[i], y[i])
        k2 = f(t[i+1], y[i] + h * k1)
        y[i+1] = y[i] + (h / 2) * (k1 + k2)

    return t, y

def midpoint_method(t0, y0, tk, n):
    h = (tk - t0) / n
    t = np.linspace(t0, tk, n+1)
    y = np.zeros(n+1)
    y[0] = y0

    for i in range(n):
        k1 = f(t[i] + h/2, y[i] + (h/2) * f(t[i], y[i]))
        y[i+1] = y[i] + h * k1

    return t, y

t0 = 0
y0 = 3
tk = 3
n = 20

t_analytical = np.linspace(t0, tk, n+1)
y_analytical = analytical_solution(t_analytical)

t_euler, y_euler = euler_method(t0, y0, tk, n)

t_heun, y_heun = heun_method(t0, y0, tk, n)

t_midpoint, y_midpoint = midpoint_method(t0, y0, tk, n)

plt.plot(t_analytical, y_analytical, label='Rozwiązanie analityczne')
plt.plot(t_euler, y_euler, label='Metoda Eulera')
plt.plot(t_heun, y_heun, label='Metoda Heuna')
plt.plot(t_midpoint, y_midpoint, label='Metoda punktu środkowego')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Rozwiązanie równania różniczkowego')
plt.legend()
plt.show()