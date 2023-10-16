import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def f(t, x, y, z):
    return -10 * x + 10 * y

def g(t, x, y, z):
    return 28 * x - y - x * z

def i(t, x, y, z):
    return -8 / 3 * z + x * y

def runge_kutta(t0, x0, y0, z0, h, num_steps):
    t_values = [t0]
    x_values = [x0]
    y_values = [y0]
    z_values = [z0]

    for _ in range(num_steps):
        t = t_values[-1]
        x = x_values[-1]
        y = y_values[-1]
        z = z_values[-1]

        k1_x = h * f(t, x, y, z)
        k1_y = h * g(t, x, y, z)
        k1_z = h * i(t, x, y, z)

        k2_x = h * f(t + h / 2, x + k1_x / 2, y + k1_y / 2, z + k1_z / 2)
        k2_y = h * g(t + h / 2, x + k1_x / 2, y + k1_y / 2, z + k1_z / 2)
        k2_z = h * i(t + h / 2, x + k1_x / 2, y + k1_y / 2, z + k1_z / 2)

        k3_x = h * f(t + h / 2, x + k2_x / 2, y + k2_y / 2, z + k2_z / 2)
        k3_y = h * g(t + h / 2, x + k2_x / 2, y + k2_y / 2, z + k2_z / 2)
        k3_z = h * i(t + h / 2, x + k2_x / 2, y + k2_y / 2, z + k2_z / 2)

        k4_x = h * f(t + h, x + k3_x, y + k3_y, z + k3_z)
        k4_y = h * g(t + h, x + k3_x, y + k3_y, z + k3_z)
        k4_z = h * i(t + h, x + k3_x, y + k3_y, z + k3_z)

        t_values.append(t + h)
        x_values.append(x + (k1_x + 2 * k2_x + 2 * k3_x + k4_x) / 6)
        y_values.append(y + (k1_y + 2 * k2_y + 2 * k3_y + k4_y) / 6)
        z_values.append(z + (k1_z + 2 * k2_z + 2 * k3_z + k4_z) / 6)

    return t_values, x_values, y_values, z_values


t0 = 0
x0 = y0 = z0 = 5
h = 0.03125
num_steps = int(25 / h)

t_values, x_values, y_values, z_values = runge_kutta(t0, x0, y0, z0, h, num_steps)

plt.figure(figsize=(8, 4))
plt.plot(t_values, x_values)
plt.xlabel('t')
plt.ylabel('x')
plt.title('Wykres x(t)')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 4))
plt.plot(t_values, y_values)
plt.xlabel('t')
plt.ylabel('y')
plt.title('Wykres y(t)')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 4))
plt.plot(t_values, z_values)
plt.xlabel('t')
plt.ylabel('z')
plt.title('Wykres z(t)')
plt.grid(True)
plt.show()

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_values, y_values, z_values)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Trajektoria fazowa')
plt.show()