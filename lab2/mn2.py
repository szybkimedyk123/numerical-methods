import matplotlib.pyplot as plt
import numpy as np

#funkcja cos(x + a)

def funkcja(h0, x0):
        arg = np.pi / 4 + x0
        funkcja1 = np.cos(arg + h0)
        funkcja2 = np.cos(arg - h0)
        wynik = (funkcja1 - funkcja2) / (2 * h0)
        return wynik

x = 0.5
n = 20
poczatek = 0.4
krok = 1 / 5
punkty = 20
h = poczatek * krok ** np.arange(punkty)

idealna = -(np.sin(x + np.pi/4))
fun = funkcja(h, x)
lista_ide = np.full((punkty,), idealna)
blad = abs(np.subtract(lista_ide,fun))
najmniejszy_blad = min(blad)
indeks = np.where(najmniejszy_blad == blad)
h_najmniejszy_blad = h[indeks]

formatted_najmniejszy_blad = '{:.20f}'.format(najmniejszy_blad)
print('-sin(x + a) = ' + str(idealna))
print('najmniejszy_blad = ' + str(formatted_najmniejszy_blad) + 'dla h = ' + str(h_najmniejszy_blad))
wyswietlanie = np.stack((h, fun, blad), axis=1)
np.set_printoptions(precision=17, suppress=True)
print("         h         |         funkcja         |         blad         ")
print("--------------------------------------------------------------------")
print(wyswietlanie)


fig = plt.figure()
plt.grid(color='grey', linestyle='--', linewidth=0.2)
plt.loglog(h, blad, 'r')
plt.show()




'''
h_values = np.logspace(-16, -1, num=1000, base=0.2)
approx_deriv_values = f0(x, h_values)
true_deriv = math.cos(x + math.pi/4)
abs_error_values = abs(approx_deriv_values - true_deriv)

# wyświetlenie wyników w postaci tabeli
results = list(zip(h_values, approx_deriv_values, abs_error_values))
header = "|{:12}|{:12}|{:12}|".format("h", "przybliżenie", "błąd")
print(header)
print("-"*len(header))
for result in results:
    print("|{:12.10f}|{:12.10f}|{:12.10f}|".format(*result))

# wyświetlenie wykresu błędu
plt.loglog(h_values, abs_error_values)
plt.title("Wykres błędu jako funkcja od h")
plt.xlabel("h")
plt.ylabel("błąd bezwzględny")
plt.show()

# znalezienie wartości h dla minimalnego błędu
min_error_idx = np.argmin(abs_error_values)
min_error_h = h_values[min_error_idx]
min_error = abs_error_values[min_error_idx]
print("Wartość h dla minimalnego błędu: {:.10f}".format(min_error_h))
print("Minimalny błąd bezwzględny: {:.10f}".format(min_error))
'''