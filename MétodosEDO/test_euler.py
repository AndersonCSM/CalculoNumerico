import numpy as np
import matplotlib.pyplot as plt
from euler import *


# Definindo a EDO: dy/dx = x + y
def edo(y, t):
    return y - t**2 + 1


def exata(t):
    return (t + 1)**2 - 0.5 * np.exp(t)


# Condição inicial
y0 = 0.5
t0 = 0

n = 10  # Intervalo de x
h = 0.2  # Tamanho do passo

# Aplicando o método de Euler
x_p, y_p = euler_method(edo, y0, t0, n, h)

t_points = [t0 + i*h for i in range(n+1)]
y_exato = [exata(t) for t in t_points]

plt.plot(x_p, y_p, label='Método de Euler')
plt.plot(x_p, y_exato, label='Valores exatos')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solução da EDO usando o Método de Euler')
plt.legend()
plt.grid(True)
plt.show()
