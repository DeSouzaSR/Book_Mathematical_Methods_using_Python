# -*- coding: utf-8 -*-

# Calculte y = v0*t + (1/2)*a*t^2 using lambda function

a = 2
v0 = 1
ypos = []
y = lambda t: v0*t + 0.5*a*t**2

for t in range(4):
    ypos.append(y(t))

print('-'*28,'CODE OUTPUT','-'*29,'\n')
print(f'Position y(t) = {ypos}')