import matplotlib.pyplot as plt
import numpy as np
import scipy
import os


file_path = os.path.join('lab_6_dane', 'data4.txt')
data = np.loadtxt(file_path)
t = data[:, 0]
y = data[:, 1]

def funkcja(s, k, tau_z, tau, zeta):
    licznik = [k*tau_z, k]
    mianownik = [tau**2, 2*zeta*tau, 1]
    return np.polyval(licznik, s) / np.polyval(mianownik, s)

def roznica(poczatkowe, t, y):
    k, tau_z, tau, zeta = poczatkowe
    y_obl = [funkcja(1j*w, k, tau_z, tau, zeta).imag for w in t]
    return np.mean((y_obl - y)**2)

poczatkowe = [1, 1, 1, 1]

koncowe = scipy.optimize.fmin(roznica, poczatkowe, args=(data[:,0], data[:,1]), disp=False)

k_est, tau_z_est, tau_est, zeta_est = koncowe

print("Obliczone:")
print(f"k_est = {k_est:.4f}")
print(f"tau_z_est = {tau_z_est:.4f}")
print(f"tau_est = {tau_est:.4f}")
print(f"zeta_est = {zeta_est:.4f}")

t = np.linspace(0, 12.5, 1250)
y_obl = [funkcja(1j*w, k_est, tau_z_est, tau_est, zeta_est).imag for w in t]

plt.plot(data[:,0], data[:,1], 'bo', label='Zmierzone')
plt.plot(t, y_obl, 'r-', label='Przyblizone')
plt.legend()
plt.xlabel('Czas')
plt.ylabel('Odpowiedz')
plt.show()