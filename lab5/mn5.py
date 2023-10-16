import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


A = np.array([[-3.15, 2.525, -0.45], [1,0,0], [0,1,0]])
B = np.array([[1],[0],[0]])
C = np.array([[1,1,1]])
D = np.array([0])
sys = signal.StateSpace(A, B, C, D)

dt = 0.01
t, y = signal.step(sys, T=np.arange(0,5, dt))

plt.plot(t, y)
plt.grid('on')
plt.xlabel('Czas')
plt.ylabel('Odpowiedź')
plt.show()

eigvals, eigvecs = np.linalg.eig(A)

if np.all(np.real(eigvals) < 0):
    print("Układ jest stabilny")
else:
    print("Układ nie jest stabilny")

c1 = 1
c2 = 0.5
n = A.shape[0]
Q = c1 * np.eye(n)
R = c2

iteracje = 100
blad = 1e-6
P = Q
for i in range(iteracje):
    P_krok = A.T @ P @ A - A.T @ P @ B @ np.linalg.inv(R + B.T @ P @ B) @ B.T @ P @ A + Q
    if np.all(np.abs(P - P_krok) < blad):
        break
    P = P_krok

K = np.linalg.inv(R + B.T @ P @ B) @ B.T @ P @ A

x0 = np.array([[1], [0], [0]])

Ad, Bd, Cd, Dd, dd = signal.cont2discrete((A, B, C, D), dt)
Kd, Pd, ed = signal.dlqr(Ad, Bd, Q, R)

t, y, _ = signal.dstep((Ad-Bd@Kd, Bd, Cd, Dd), t=np.arange(0, 5, dt), x0=x0)

plt.plot(t, y.squeeze())
plt.grid('on')
plt.xlabel('Czas')
plt.ylabel('Odpowiedź')
plt.show()