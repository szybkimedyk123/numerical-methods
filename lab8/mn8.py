import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate


file_path = "data4.txt"
data = np.loadtxt(file_path)
x = data[:, 0]
y = data[:, 1]

def newton_interpolation(x, y, xi):
    n = len(x)
    F = np.zeros((n, n))
    F[:, 0] = y
    for i in range(1, n):
        for j in range(i, n):
            F[j, i] = (F[j, i - 1] - F[j - 1, i - 1]) / (x[j] - x[j - i])
    p = F[n - 1, n - 1]
    for k in range(1, n):
        p = F[n - 1 - k, n - 1 - k] + (xi - x[n - 1 - k]) * p
    return p

spline_interpolation = interpolate.interp1d(x, y, kind='cubic')

x_new = np.linspace(x.min(), x.max(), 500)
y_new_newton = [newton_interpolation(x, y, xi) for xi in x_new]
y_new_spline = spline_interpolation(x_new)

plt.plot(x, y, 'o', label='Dane wejściowe')
plt.plot(x_new, y_new_newton, '-', label='Interpolacja Newtona')
plt.plot(x_new, y_new_spline, '-', label='Interpolacja funkcjami sklejanymi')
plt.legend()
plt.show()