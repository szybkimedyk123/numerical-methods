import matplotlib.pyplot as plt
import numpy as np
import math


def rozwiniecie(n0, x0):
    if n0 == 0:
        return np.cos(np.pi/4)
    else:
        lista_n = np.arange(1, n0+1)
        lista_x = np.full((n0,), x0)
        arg = (np.pi / 4) + (lista_n * (np.pi / 2))
        silnia = np.cumprod(lista_n)
        wynik = pow(lista_x, lista_n) * np.cos(arg) / silnia
        suma = sum(wynik) + np.cos(np.pi/4)
        return suma


print("   n  |  x  |  rozwiniecie   | blad bezwgledny |  blad wzgledny")
print("----------------------------------------------------------------")

for n in range(1, 12):
    x = 0.5
    f_rozwiniecia = rozwiniecie(n, x)
    f_wartosc = np.cos(x + np.pi / 4)
    blad_bezwgledny = abs(f_wartosc - f_rozwiniecia)
    blad_wzgledny = blad_bezwgledny / f_wartosc * 100
    print(f"  {n-1:2d}  | {x:4.1f} | {f_rozwiniecia:.12f} | {blad_bezwgledny:.12f}  | {blad_wzgledny:.12f} ")

os_x = np.linspace(0, 1, 10)
y1 = []
y2 = []
y3 = []
yid = []

for x in os_x:
    n1 = 0
    f1 = rozwiniecie(n1, x)
    y1.append(f1)
    n2 = 1
    f2 = rozwiniecie(n2, x)
    y2.append(f2)
    n3 = 2
    f3 = rozwiniecie(n3, x)
    y3.append(f3)
    yid1 = np.cos(x + np.pi/4)
    yid.append(yid1)

fig = plt.figure()
plt.grid(color='grey', linestyle='--', linewidth=0.2)
plt.plot(os_x, y1, 'r', os_x, y2, 'g', os_x, y3, 'b', os_x, yid, 'm')
plt.legend(['red - n=0', 'green - n=1', 'blue - n = 2', 'magenta - ideal'])
plt.show()