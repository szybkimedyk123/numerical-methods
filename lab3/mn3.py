import numpy as np
import scipy.linalg as linalg

Qa = 200; Qb = 300; Qc = 150; Qd = 350
ca = 2; cb = 2
Ws = 1500; Wq = 2500
E12 = 25; E23 = 50; E35 = 25; E34 = 50

#uklad równań

A = np.array([[E12 + Qa, -E12, 0, 0, 0],
              [-E12 - Qa, E12 + E23 + Qa + Qb, -E23, 0, 0],
              [0, -E23 - Qa - Qb, E23 + E34 + E35 + Qa + Qb, -E34, -E35],
              [0, 0, -E34 - Qa - Qb + Qd, E34 + Qc, 0],
              [0, 0, -E35 - Qa - Qb + Qc, 0, E35 + Qd]])

B = np.array([[Ws + Qa * ca],
              [Qb * cb],
              [0],
              [0],
              [Wq]])


_, L, U = linalg.lu(A)

pom1 = linalg.solve_triangular(L, B, lower=True)
x = linalg.solve_triangular(U, pom1)

for i in range(len(x)):
    print("Wektor stężeń CO P" + str(i+1) + ": {:.3f}".format(float(x[i])))
print('\n')

Ws_zmn = 800; Wq_zmn = 1200
B_zmn = np.array([Ws_zmn + Qa * ca, Qb * cb, 0, 0, Wq_zmn])

pom1_zmn = linalg.solve_triangular(L, B_zmn, lower=True)
x_zmn = linalg.solve_triangular(U, pom1_zmn)

for i in range(len(x_zmn)):
    print("Wektor stężeń - nowy CO P" + str(i+1) + "", '{:6.3f}]'.format(x_zmn[i]))
print('\n')

temp = linalg.solve_triangular(L, [1, 0, 0, 0, 0], lower=True)
rzad1 = linalg.solve_triangular(U, temp)
temp = linalg.solve_triangular(L, [0, 1, 0, 0, 0], lower=True)
rzad2 = linalg.solve_triangular(U, temp)
temp = linalg.solve_triangular(L, [0, 0, 1, 0, 0], lower=True)
rzad3 = linalg.solve_triangular(U, temp)
temp = linalg.solve_triangular(L, [0, 0, 0, 1, 0], lower=True)
rzad4 = linalg.solve_triangular(U, temp)
temp = linalg.solve_triangular(L, [0, 0, 0, 0, 1], lower=True)
rzad5 = linalg.solve_triangular(U, temp)

A_inv = np.array([rzad1, rzad2, rzad3, rzad4, rzad5])
A_inv = np.transpose(A_inv)

np.set_printoptions(precision=3)#, suppress=True, formatter={'float_kind': lambda x: "%.10f" % x})
print('A^-1:')
print(A_inv)
print('\n')

udz_grill = (A_inv[3, 4] * Wq) / x[3]
udz_palacz = (A_inv[3, 0] * Ws) / x[3]
udz_ulica = (A_inv[3, 0] * Qa * ca + A_inv[3, 1] * cb * cb) / x[3]

print('udziały procentowe:')
print('grill: {:.2f}%'.format(float(udz_grill * 100)))
print('palacz: {:.2f}%'.format(float(udz_palacz * 100)))
print('ulica: {:.2f}%'.format(float(udz_ulica * 100)))




'''
A_inv_np = np.linalg.inv(A)
print('A^ -1 z numpy:')
print(A_inv_np)
print('\n')

udz_grill_zmn = (A_inv[3, 4] * Wq_zmn) / x_zmn[3]
udz_palacz_zmn = (A_inv[3, 0] * Ws_zmn) / x_zmn[3]
udz_ulica_zmn = (A_inv[3, 0] * Qa * ca + A_inv[3, 1] * Qb * cb) / x_zmn[3]

print('udziały procentowe:')
print('grill: {:.2f}%'.format(udz_grill_zmn * 100))
print('palacz: {:.2f}%'.format(udz_palacz_zmn * 100))
print('ulica: {:.2f}%'.format(udz_ulica_zmn * 100))
print('\n')
'''