import numpy as np
import matplotlib.pyplot as plt


min = -20
max = 20

x1 = np.arange(min, max, 0.001)
x21 = np.arange(min, -3.501, 0.001)
x22 = np.arange(-3.499, max, 0.001)

def f1(x):
    return x**2 - 2*x + 0.5

def f1_prime(x):
    return (-2*x*(2*x+7) + x**2)/(2*x+7)**2

def f2(x):
    return -x**2/(2*x+7)

def f2_prime(x):
    return 2*x - 2

y1 = f1(x1)
y21 = f2(x21)
y22= f2(x22)

roots1 = np.roots([1, -2, 0.5])
approx_roots1 = [round(root, 2) for root in roots1]
print("Pierwiastki funkcji y = x^2 - 2x + 0.5 = " + str(approx_roots1))

roots2 = np.roots([1, 0, 0])
approx_roots2 = [round(root, 2) for root in roots2]
print("Pierwiastki funkcji y = (-x^2)/(2x+7) = " + str(approx_roots2))

def oblicz_NR(x0, y0, liczba_iter):
    epsilon = 10 ** (-8)
    xs = x0
    ys = y0

    for i in range(liczba_iter):
        f1 = -x0 ** 2 / (2 * x0 + 7) + y0 ** 2 - 2 * y0 + 0.5
        f2 = x0 ** 2 - 2 * x0 + 0.5 - y0

        df11 = -2 * x0 * (2 * x0 + 7) / (2 * x0 + 7) ** 2 + x0 ** 2 / (2 * x0 + 7) ** 2
        df12 = 2 * y0 - 2
        df21 = 2 * x0 - 2
        df22 = -1

        Jacob = df11 * df22 - df21 * df12

        x1 = x0 - (f1 * df22 - f2 * df12) / Jacob
        y1 = y0 - (f2 * df11 - f1 * df21) / Jacob

        err1 = abs((x1 - x0) / x1) * 100
        err2 = abs((y1 - y0) / y1) * 100

        x0 = x1
        y0 = y1

        if err1 < epsilon and err2 < epsilon:
            break

    print(f"\nWyniki dla x0: {xs} oraz y0: {ys}")
    print(f"x = {x1}, y = {y1}")

oblicz_NR(-3, 1, 100)
oblicz_NR(0.6, 0.09, 100)
oblicz_NR(1.5, -0.2, 100)

plt.plot(x1, y1, label='y = x^2 - 2x + 0.5')
plt.plot(x21, y21, label='y = (-x^2)/(2x+7)', color = 'orange')
plt.plot(x22, y22, color = 'orange')

plt.title('Wykres funkcji')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid('on')
plt.axis([-20, 20, -40, 40])

plt.show()