import numpy as np
import matplotlib.pyplot as plt

upperEdge = np.linspace(400, 300, 21)
bottomEdge = np.linspace(300, 200, 21)
leftEdge = np.linspace(400, 300, 21)
rightEdge = np.linspace(300, 200, 21)

h = 0.2
Ta = 100
d = 0.5
A = np.zeros([361, 361])
b = np.zeros((361, 1))

d_squared = d ** 2
factor1 = -1 / d_squared / h
factor2 = -factor1
factor3 = Ta

for i in range(np.shape(A)[0]):
    A[i, i] = (4 / d_squared + h) / h
    if i % 19 == 0:
        if i < 19:
            A[i, i + 19] = factor1
            A[i, i + 1] = factor1
            b[i][0] = factor3 + factor2 * leftEdge[int(i / 19) + 1] + factor2 * upperEdge[i + 1]
        elif i >= 19 * 18:
            A[i, i - 19] = factor1
            A[i, i + 1] = factor1
            b[i][0] = factor3 + factor2 * leftEdge[int(i / 19) + 1] + factor2 * bottomEdge[(i % 19) + 1]
        else:
            A[i, i + 19] = factor1
            A[i, i - 19] = factor1
            A[i, i + 1] = factor1
            b[i][0] = factor3 + factor2 * leftEdge[int(i / 19) + 1]
    elif i % 19 == 18:
        if i < 19:
            A[i, i + 19] = factor1
            A[i, i - 1] = factor1
            b[i][0] = factor3 + factor2 * rightEdge[int(i / 19) + 1] + factor2 * upperEdge[i + 1]
        elif i >= 19 * 18:
            A[i, i - 19] = factor1
            A[i, i - 1] = factor1
            b[i][0] = factor3 + factor2 * rightEdge[int(i / 19) + 1] + factor2 * bottomEdge[(i % 19) + 1]
        else:
            A[i, i + 19] = factor1
            A[i, i - 19] = factor1
            A[i, i - 1] = factor1
            b[i][0] = factor3 + factor2 * rightEdge[int(i / 19) + 1]
    elif i < 19:
        A[i, i + 19] = factor1
        A[i, i + 1] = factor1
        A[i, i - 1] = factor1
        b[i][0] = factor3 + factor2 * upperEdge[i + 1]
    elif i >= 19 * 18:
        A[i, i - 19] = factor1
        A[i, i + 1] = factor1
        A[i, i - 1] = factor1
        b[i][0] = factor3 + factor2 * bottomEdge[(i % 19) + 1]
    else:
        A[i, i + 19] = factor1
        A[i, i - 19] = factor1
        A[i, i + 1] = factor1
        A[i, i - 1] = factor1
        b[i][0] = factor3

invA = np.linalg.inv(A)

x = np.matmul(invA, b)
result = x.reshape([19, 19])

print(np.min(x))

plt.imshow(result, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.xticks(range(result.shape[1]))
plt.yticks(range(result.shape[0]))
plt.show()