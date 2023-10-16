import numpy as np
from sympy import integrate, Symbol
import math


def f(x, a, b, c, d, e):
    return a*x**4 + b*x**3 - c*x**2 + d*x - e

def analytical_integral(a, b, c, d, e):
    x = Symbol('x')
    integrand = a*x**4 + b*x**3 - c*x**2 + d*x - e
    integral = integrate(integrand, x)
    return float(integral.subs(x, 5) - integral.subs(x, -20))

def romberg_integration(f, a, b, n, params):
    R = np.zeros((n,n))
    h = b - a
    R[0,0] = (h/2)*(f(a, *params) + f(b, *params))
    for j in range(1, n):
        h = h/2
        summation = 0
        for i in range(1, 2**j, 2):
            summation += f(a + i*h, *params)
        R[j,0] = R[j-1,0]/2 + h*summation
        for k in range(1, j+1):
            R[j, k] = (4 * k * R[j, k - 1] - R[j - 1, k - 1]) / (4 * k - 1)
            if abs(R[j, k] - R[j, k - 1]) / (2 ** k - 1) < 0.002 * R[j, k]:
                return R[j, k]
            print(R[j, k])
    return R[-1,-1]

def gaussian_quadrature(f, a, b, params):
    x = [-np.sqrt(3/5), 0, np.sqrt(3/5)]
    w = [5/9, 8/9, 5/9]
    fx = 0
    for i in range(len(x)):
        fx += w[i] * f((b-a)/2 * x[i] + (b+a)/2, *params)
    return (b-a)/2 * fx

a = -20
b = 5
n = 5
params = [0.02721, 0.5415, 0.1211, 4.27, 2.21]
print("Analitycznie:", analytical_integral(*params))

x = Symbol('x')
integrand = params[0]*x**4 + params[1]*x**3 - params[2]*x**2 + params[3]*x - params[4]
integral = integrate(integrand, x)
polynomial_coeffs = [float(integral.diff(x, i).subs(x, 5) - integral.diff(x, i).subs(x, -20)) / math.factorial(i) for i in range(5)]
print("Wspolrzynniki:", polynomial_coeffs)
print("Romberg:", romberg_integration(f, a, b, n, params))
print("kwadratura Gaussa:", gaussian_quadrature(f, a, b, params))