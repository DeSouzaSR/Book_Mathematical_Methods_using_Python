# """
# # lambdify function
#
# Example 1.18: Example of using the lambdify function
#
# Use SymPy to evaluate the symbolic derivative of the function $f = a\sin(bt)$ with respect to time
# $t$, and plot the function $f(t)$ and its derivative in the interval $t = 0$ to $t = 6$. Use the numerical
# values $a = 1$ and $b = 2$.
# """

import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, sin, diff
from sympy.utilities.lambdify import lambdify

a, b, t = symbols('a, b, t', real=True)

# Evaluate symbolic derivarive of f
f = a*sin(b*t)
deriv = diff(f, t)
print("Function: ", f)
print('Symbolic derivative', deriv)

# Sequence of times
tims = np.linspace(0,6,50)

# substitute a=1 and b=2 in f
y = lambdify(t, f.subs({a:1, b:2}))

# substitute a=1 and b=2 in deriv
u = deriv.subs({a:1, b:2})

# Lambdify creates derivative function v(t)
v = lambdify(t, u)

# Plots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Primeiro gráfico (sem eixo x)
ax1.plot(tims, y(tims))
ax1.set_ylabel('y(t)')
ax1.tick_params(labelbottom=False)  # remove rótulos do eixo x
ax1.spines['bottom'].set_visible(False)  # remove a linha do eixo x, opcional

# Segundo gráfico
ax2.plot(tims, v(tims))
ax2.set_xlabel('Time [s]')
ax2.set_ylabel('Speed v(t) = dy/dt')

# Diminuir espaço vertical entre os gráficos
plt.subplots_adjust(hspace=0.01)

plt.show()
