from sympy import symbols, Symbol, factor, expand, pprint, init_printing, simplify, sympify, SympifyError, solve, Subs, plot, summation, Poly, solve_poly_inequality, solve_rational_inequalities, solve_univariate_inequality
# w = Symbol('w') #Symbol is a class
# x,y,z = symbols('x,y,z') #symbols is a function that creates three Symbol objects
# p = expand((x+2)*(x+3)) #expand() multiples out expressions with multiple terms
# p = factor(x**2-y**2) #factor() factors
# expr=x**3+x*y**2+2*y+3*z
# res = expr.subs({x:1, y:2, z:5}) #the subs() method of an expression subsititutes values into the variables (provide values as a dictionary)
# init_printing(order='rev-lex') #used to change many aspects of how pprint works (e.g. changing the order, etc); put it before pprint()
# pprint(expr) #pprint() or pretty print displays the expressions more naturally
# expr = x*x + x*y + x*y + y*y
# expr_subs = expr.subs({x:1-y}) #if you know x = 1-y substitute it this way then use simplify() to cancel out terms and simplify:
# pprint('{0} simplifies to {1}'.format(expr_subs, simplify(expr_subs)))
# pprint(simplify(expr_subs))
# expr = input("Enter an algebraic expression: ")
# try:
#     expr = sympify(expr) #sympify() parses a string into a mathematical expression
#     print (2*expr)
# except SympifyError:    #this error needs to be imported from module
#     raise Exception('Invalid expression syntax')
# expr = x - 5 - 7 # equation must be set equal to zero (this one is x - 5 = 7 or x - 7 = 5)
# print(solve(expr)) #solve() outputs a list by default and a dictionary if solving simultaneous equations
# expr = x**2 + x + 1
# print(solve(expr,dict=True))
# a,b,c,x = symbols('a,b,c,x')
# expr = a*x**2+b*x+c #quadratic equation
# print(solve(expr, x, dict=True)) #solves the expression in terms of x giving the quadratic equation (2nd argument is the variable to solve for if multiple are present)
# x,n = symbols('x,n')
# s = summation(x**n/n, (n, 1, 5))  #summation() is the sigma symbol used to summate an expression; in this case from n=1 to n=5
# pprint(s)

#solving for one variable in terms of others
# s,t,v,a = symbols('s,t,v,a') #create all the symbol/variables
# expr = 1/2*a*t**2+v*t-s #expression with the variables
# t_expr = solve(expr,t,dict=True) #solve the expression in terms of t, outputted as a list of dictionaries
# for expr in t_expr: #iterating through each dictionary
#     pprint(expr)
#     print(expr[t].subs({a:5,v:1,s:1})) #substituting the values in to solve for t given a,s, and v
# t_res = t_expr[0].subs({a:5,v:0,s:0})
# pprint(t_res)

#solving systems of equations:
# x,y = symbols('x,y')
# expr1 = 2*x+3*y-6
# expr2 = 3*x+2*y-12
# ans = solve((expr1,expr2),dict=True)  #need to use a tuple for the 1st argument where each expression is in the tuple
# pprint(ans)
# pprint(expr1.subs({x:ans[0][x],y:ans[0][y]}))  #plugging the ans from solve() back in to the expr to see if they are true solutions (i.e. 0)
# pprint(expr2.subs({x:ans[0][x],y:ans[0][y]}))

# #plotting using sympy; can just type an expression an it plots the whole thing:
# x = Symbol('x')
# expr = 2*x**3+2
# expr2 = 4*x**2*2*x+7
# soln = solve((expr,expr2),dict=True)
# pprint(soln)
# p = plot(expr, expr2, (x,-1,1), xlabel='X-axis', ylabel='Y-axis', title="Title Goes Here", show=False, legend=True)  #plots 2x+3 from x = -5 to 5; y range is automatically calculated; plot() automatically calls show() but you can use kwarg to stop this; can plot as many expressions as you want just put them first
# p[0].line_color = 'c' #color option are green, red, blue, cyan, magenta, yellow, black, and white; just use the 1st letter
# p[1].line_color = 'm' 
# p.save(r"linear.png") #saving the plot
# p.show() #shows the plot for when kwarg show=False

#Factor finder
def find_factor():
    expr = input('Enter an expression to factor: ')
    try:
        sympify(expr) 
    except SympifyError:
        raise Exception('Invalid Expression')
    else:
        pprint(factor(expr))

#Graphical Equation Solver: (when using solve() you have to put the whole equation in when set equal to 0; e.g. 2x+3=y is put in as 2*x+3-y )
def solver_equation_graphically():
    elist = []
    try:
        n = int(input('How many equations would you like to solve for? '))
        assert isinstance(n, int)
        for i in range(1,n+1):
            if i == 1:
                expr = input('Enter the {0}st expression: '.format(i))
            elif i == 2:
                expr = input('Enter the {0}nd expression: '.format(i))
            elif i == 3:
                expr = input('Enter the {0}rd expression: '.format(i))
            else:
                expr = input('Enter the {0}th expression: '.format(i))
            elist.append(sympify(expr))
    except SympifyError:
        raise Exception('Invalid Expression')
    else:
        elist = tuple(elist)
        # print(elist)
        ans = solve(elist,dict=True)
        # pprint(ans)
        if len(ans) == 0:
            print('There is no solution for {0}'.format(elist))
        else:
            for i in range(len(ans)):
                if i == 0:
                    print('{2}st Solution found when x = {0} and y = {1}'.format(ans[i][x],ans[i][y],i+1))
                elif i ==1:
                    print('{2}nd Solution found when x = {0} and y = {1}'.format(ans[i][x],ans[i][y],i+1))
                elif i ==2:
                    print('{2}rd Solution found when x = {0} and y = {1}'.format(ans[i][x],ans[i][y],i+1))
                else:
                    print('{2}th Solution found when x = {0} and y = {1}'.format(ans[i][x],ans[i][y],i+1))

#Summing a series:
def sum_series():
    nth_term = input('Enter the nth term: ')
    try:
        nth_term = sympify(nth_term)
        n_num = int(input('Enter the number of terms: '))
        assert isinstance(n_num, int)
    except SympifyError:
        raise Exception('Invalid Expression')
    except ValueError:
        raise Exception('Invalid number of terms')
    else:
        n = Symbol('n')
        ans = summation(nth_term, (n,1,n_num))
        pprint(ans)

#solving polynomial inequalities

#Solving inequalities in the form of (expression </> 0); using a class with methods to do
class Inequality():  
    try:
        ineq_obj = sympify(input('Enter an inequality to solve: '))
        lhs = ineq_obj.lhs
    except SympifyError:
        raise Exception('Invalid expression.  Try again.')
    except AttributeError:
        raise Exception('Invalid Expression.  Include either < or >')

    #solving the polynomials
    def poly_solve(self):
        lhs = self.ineq_obj.lhs   #.lhs is the attribute for the left-hand side of the equation
        p = Poly(lhs, x) 
        rel = self.ineq_obj.rel_op  #assigning the relational operator via .rel_op to a variable
        print(solve_poly_inequality(p,rel)) #specifying the Poly object which is the left-hand side of the inequality object and the relational operator

    #solving rational inequaltities (when the numerator and denominator are both polynomials)
    def rational_solve(self):
        numer, denom = self.lhs.as_numer_denom()
        p1 = Poly(numer)
        p2 = Poly(denom)
        rel = self.ineq_obj.rel_op
        print(solve_rational_inequalities([[((p1,p2), rel)]]))
        
    #solving univariate inequalities (neither rational nor polynomial)
    def univariate_solve(self):
        # x = Symbol('x')
        print(solve_univariate_inequality(self.ineq_obj, x , relational=False
        ))

#printing a series using recursion
def printing_series(n):
    x = Symbol('x')
    series = ((x**n)/(4*x)) + x*n + 5
    init_printing(order='rev-lex')
    assert isinstance(n, int), 'n must be an integer larger than 0'
    if n==1:
        return series
    elif n<1:
        raise Exception('N must be larger than 0')
    else:
        return series + printing_series(n-1)

def evaluate_series(n, values):
    expr = printing_series(n)
    assert isinstance(values, dict), 'X must be a dictionary'
    ans = expr.subs(values)
    # ans = ans.simplify()
    print('\nInserting {0} into {1} yields:'.format(values,expr), ans)
    # return ans

def expression_operator(expr_list, operation):
    operation = operation.upper()
    while operation not in ('M','D','S','A','EXIT'):
        print('Operation must either be one of the following: M, D, S, A, or EXIT')
        operation = input('Try again: ')
    
    if operation in ('M','D'):
        res = 1
    else:
        res = 0
    k = 0
    for expr in expr_list:
        if operation == 'M':
            res = res * expr
        elif operation == 'D':
            if k == 0:
                res = expr
            else:
                res = res / expr
        elif operation == 'S':
            if k == 0:
                res = expr
            else:
                res = res - expr
        elif operation == 'A':
            res = res + expr
        elif operation == 'EXIT':
            return('Exiting...')
        k += 1    
    if operation in ('M'):
        return expand(res)
    else:
        return res

if __name__ == "__main__":
    # c = Inequality()
    # if c.lhs.is_polynomial():
    #         c.poly_solve()
    # elif c.lhs.is_rational_function():
    #     c.rational_solve()
    # else:
    #     c.univariate_solve()
    # find_factor()
    # pprint(printing_series(int(input('How many terms of series do you want: '))))
    # sum_series()
    # solver_equation_graphically()
    #Expression Operator
    # n = int(input('How many expressions would you like to use? '))
    # elist = []
    # for i in range(1,n+1):
    #     new_expr = input('Enter the {0}th expression: '.format(i))
    #     try:
    #         elist.append(sympify(new_expr))
    #     except SympifyError:
    #         raise Exception("Invalid Expression")
    # operation = input('Enter the operation to perform (Options are: (M)ultiply, (D)ivide, (S)ubtract, (A)dd, or Exit): ')
    # print('\nResult:')
    # pprint(expression_operator(elist, operation))
    pass





    #Evaluate Series 
    # n = input('Enter the number of terms you want to go to in the series: ')
    # x_val = float(input('Enter the value of x at which you want to evaluate the series: '))  #important to use floats
    # y_val = float(input('Enter the value of y at which you want to evaluate the series: '))  #important to use floats

    # x,y = symbols('x,y')
    # values = {x:x_val,y:y_val}
    # pprint(evaluate_series(int(n),values))