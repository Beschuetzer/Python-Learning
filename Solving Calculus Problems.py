from matplotlib import pyplot as plt
import sympy
import math

#log() = natural logarithm
#log2() = base-2 logarithm
#log10() = base-10 logarithm
#exp() = finds the value of e^x, where e is Euler's number (~2.71828)
#the biggest drawback of the aforementioned functions is that they're not suitable for working with symbolic expression;  need to use the equivalent functions in SymPy

# print(sympy.sin(math.pi/2))
# theta = sympy.Symbol('theta')
# sympy.pprint(sympy.sin(theta) + sympy.sin(theta))

#symbolically solving the equation to find when v=0 (V_h = -9.8t + v * sin(theta)) but for t
# v, t, theta, g = sympy.symbols('v,t,theta,g')
# sol = (sympy.solve(v*sympy.sin(theta)-g*t, t))
# sympy.pprint(sol)

#when declaring symbols with Sympy, using keyword arguments like negative=True, positive=True, real=, integer=, complex=, and imaginary= may be necessary to avoid errors
# x = sympy.Symbol('x', positive=True)
# if (x+5) > 0:
#     print('Do Something')
# else:
#     print('Something else')

#using the Limit() class to find limits
#finding the limit of f(x) = 1/x as x approaches positive infinity:
# l =  sympy.Limit(1/x, x, sympy.S.Infinity)#returns an unevaluated object with the dir='-' meaning approaching the limit from the negative side
 #the S() class is a special class containing the definition of infinity (positive and negative) as well as other special values.
# print(l.doit()) #the doit() method exaluates the limit object
# print(sympy.Limit(1/x, x, 0, dir='-').doit())
# print(sympy.Limit(1/x, x, 0, dir='+').doit())
# print(sympy.Limit(sympy.sin(x)/x, x, 0).doit())

# '''Continuous Compound Interest and taking the limit to find e'''
# n = sympy.Symbol('n')
# amount = (1 + 1/n) **n
# limit = sympy.Limit(amount, n, sympy.S.Infinity)
# print(limit.doit())

# '''Compound Interest when the limit n --> + infinity = p*e**(r*t)'''
# n, p, r, t = sympy.symbols('n,p,r,t')
# amount = p*(1 + r/n)**(n*t)
# limit = sympy.Limit(amount, n, sympy.S.Infinity)
# sympy.pprint(limit.doit())

# '''Instantaneous Rate of Change  (basically taking the derivitive using Limit()'''
# t, t1, delta_t = sympy.symbols('t, t1, delta_t')
# st = 5*t**2+2*t+8
# st1 = st.subs({t:t1})
# st1_delta =st.subs({t: t1 + delta_t})
# l = sympy.Limit((st1_delta - st1)/delta_t, delta_t, 0)
# sympy.pprint(l.doit())

# '''Find the Derivitive of Functions using Derivative()'''
# St = 5*t**2+2*t+8
# sympy.pprint(sympy.Derivative(st, t).doit()) # take the derivitive of st with respect to t
# x = sympy.Symbol('x')
# st = (x**3+x**2+x) * (x**2 + x)
# d = sympy.Derivative(st, x)
# sympy.pprint(d.doit())

'''Derivative Calculator'''
def get_derivative(expr, var):
    return sympy.Derivative(expr, var).doit()

#.evalf() #is used to evaluate a sympified expression
def get_minima_and_maxima(expr, d_expr):
    minima, maxima = [], []
    critical_points = sympy.solve(d_expr)
    if len(critical_points) != 0:
        for p in critical_points:
            precision = .0001
            temp = expr.subs({x: p}).evalf()
            if temp > expr.subs({x: p + precision}).evalf() and temp > expr.subs({x: p - precision}).evalf():
                # print('{0} is a peak'.format(p.evalf()))
                maxima.append(p)
            elif temp < expr.subs({x: p + precision}).evalf() and temp < expr.subs({x: p - precision}).evalf():
                # print('{0} is a trough'.format(p.evalf()))
                minima.append(p)
    return minima, maxima

def calculate_derivative():
    to_remove = ['*','/','+','-','**','(',')','[',']']
    try:
        user_input = input('Enter the expression for which you want to take the derivative: ')
        expr = sympy.sympify(user_input)
        options = user_input
        for item in to_remove:
            options = options.replace(item, ' ')
        options = ''.join([i for i in options if not i.isdigit()])
        options = options.lstrip().rstrip()
        options = set(options.split())
        user_input = input('With respect to which variable should the derivative by taken: ')
        while user_input not in options:
            user_input = input('Invalid variable.  Valid options are {0}: '.format(options))
        var = sympy.sympify(user_input)
    except sympy.SympifyError:
        raise Exception('Invalid expression')
    else: 
        d_expr = get_derivative(expr, var)
        minima, maxima = get_minima_and_maxima(expr, d_expr)
        sympy.pprint('Derivative of "{0}" is:'.format(expr))
        sympy.pprint(d_expr)
        if len(minima) == 0:
            print('There are no local minima.')
        else:
            print('Local Minima are: {0}'.format(minima))
        if len(maxima) == 0:
            print('There are no local maxima.')
        else:
            print('Local maxima are: {0}'.format(maxima))

# if __name__ == "__main__":
#     # calculate_derivative()
#     pass



'''Gradual Ascent Algorithm for Finding Global Maximum'''
from sympy import Derivative, sympify, Symbol, solve, SympifyError
def grad_ascent(x0, f1x, x):
    #Check if f1x=0 has a solution
    if not solve(f1x):
        print('Cannont Continue, solution for {0} = 0 does not exist'.format(f1x))
        return
    epsilon = 1e-6
    step_size = 1e-4 #scientific notation of '.0001'
    x_old = x0
    x_new = x_old + step_size * f1x.subs({x:x_old}).evalf()
    while abs(x_old - x_new) > epsilon:
        x_old = x_new
        x_new = x_old + step_size * f1x.subs({x:x_old}).evalf()
    return x_new

# if __name__ == "__main__":
#     f = input('Enter a function in one variable: ')
#     var = input('Enter the variable to differentiate with respect to: ')
#     var0 = float(input('Enter the intitial value of the variable: '))
#     try:
#         f = sympify(f)
#     except SympifyError:
#         raise Exception('Invalid function entered')
#     else:
#         var = Symbol(var)
#         d = Derivative(f, var).doit()
#         var_max = grad_ascent(var0, d, var)
#         if var_max:
#             print('{0}: {1}'.format(var.name, var_max))
#             print('Maximum value: {0}'.format(f.subs({var:var_max})))

'''Solving Integrals'''
x,k = sympy.symbols('x,k')
f = k * x
i = sympy.Integral(f, x).doit
sympy.pprint(i)
