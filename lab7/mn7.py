import numpy as np
import matplotlib.pyplot as plt


def load_data(file_path):
    data = np.loadtxt(file_path, delimiter='\t', skiprows=1)
    return data[:, 0:2]

file_path = "measurements4.txt"
zz = load_data(file_path)
z = zz.T

F = np.array([[1, 0, 1, 0],
              [0, 1, 0, 1],
              [0, 0, 1, 0],
              [0, 0, 0, 1]])
Q = np.eye(4) * 0.1
x0 = np.array([0,
               0,
               0,
               0])
P0 = np.eye(4)

H = np.array([[1, 0, 0, 0],
              [0, 1, 0, 0]])
R = np.eye(2) * 10


x = x0
P = P0
for i in range(z.shape[1]):
    x = np.dot(F, x)
    P = np.dot(np.dot(F, P), F.T) + Q

    y = z[:, i] - np.dot(H, x)
    S = np.dot(np.dot(H, P), H.T) + R
    K = np.dot(np.dot(P, H.T), np.linalg.inv(S))
    x = x + np.dot(K, y)
    P = np.dot((np.eye(4) - np.dot(K, H)), P)

    if i == 0:
        res = np.array(x)
        pre = np.array(x)
    else:
        res = np.vstack((res, x))
        pre = np.vstack((pre, np.dot(F, x)))

for i in range(5):
    x = np.dot(F, x)
    prediction = np.vstack((pre, x))

plt.plot(zz[:, 0], zz[:, 1], 'xb', label='Pomiary')
plt.plot(res[:, 0], res[:, 1], '-r', label='Trajektoria')
plt.plot(pre[:, 0], pre[:, 1], 'o--g', label='Przewidywanie')
plt.legend()
plt.show()