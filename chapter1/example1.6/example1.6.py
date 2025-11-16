# -*- coding: utf-8 -*-

# Calculte y = v0*t + (1/2)*a*t^2

def f(v0, a, t):
    y = v0*t + 0.5*a*t**2
    return y
    
ypos = []

for t in range(4):
    ypos.append(f(1, 2, t))

print('-'*28,'CODE OUTPUT','-'*29,'\n')
print(f'Position y(t) = {ypos}')