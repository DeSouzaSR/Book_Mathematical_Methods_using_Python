# -*- coding: utf-8 -*-

from sympy import symbols, Matrix, simplify, solve
import pprint

a, b, c, d, e, f, x, y = symbols('a, b, c, d, e, f, x, y')
A = Matrix([[a, b], [c, d]])
det = A.det()
inverse = A.inv()
sol = solve([a*x+b*y-e,c*x+d*y-f],(x,y))

print('-'*28,'CODE OUTPUT','-'*29,'\n')


print('The determinant of A =', det)
print('\n The inverse of A is: ')
pp = pprint.PrettyPrinter(width=41, compact=True)
pp.pprint(inverse)
print('\n The product inverseA*A is')
print(simplify(inverse*A))
print('\n The solution of the system is:')
print('x =',sol[x])
print('y =',sol[y])