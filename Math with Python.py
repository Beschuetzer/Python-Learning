from pylab import plot, show
x_numbers = [1,2,3]
y_numbers = [2,4,6]
plot(x_numbers, y_numbers)



def get_factors(number):
    # highest = number / 2
    # factors = []
    # for i in range(2,int(highest+1)):
    #     if (number%i == 0):
    #         factors.append(i)
    if number == 1:
        return [1]
    if number == 2:
        return [1,2]
    else:
        factors = [i for i in range(2,int((number/2)+1)) if number%i==0]
        return factors

def is_factor(a, b):
    if b%a ==0:
        return True
    else:
        return False
    
def get_roots(a, b, c):
    r_1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
    r_2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
    print('Root 1: {0}'.format(r_1))
    print('Root 2: {0}'.format(r_2))



def get_multiplication_table(number, length):
    while True:
        menu = """
Choose the Operation to Use for the Table:
1 = Add
2 = Subtract
3 = Divide
4 = Multiply
5 = Exponent
6 = Root
0 = Exit"""
        print(menu)
        operation = int(input('\nChoice: ',))
        for i in range(1,length+1):
            if operation == 0:
                break
                print('breaking')
            elif operation == 1:
                op = '+'
                print('{0} {3} {1} = {2}'.format(number, i, number+i, op)) 
            elif operation ==2:
                op = '-'
                print('{0} {3} {1} = {2}'.format(number, i, number-i, op)) 
            elif operation ==3:
                op = '/'
                print('{0} {3} {1} = {2}'.format(number, i, number/i, op)) 
            elif operation ==4:
                op = 'x'
                print('{0} {3} {1} = {2}'.format(number, i, number*i, op)) 
            elif operation ==5:
                op = '^'
                print('{0} {3} {1} = {2}'.format(number, i, number**i, op))
            elif operation ==6:
                op = '^1/2'
                print('{1}th root of {0} = {2}'.format(number, i, number**(1/i))) 
            else:
                print(operation,'is not a valid option')
                break


def vending_maching(number):
    next = [number + i for i in range(2,20,2)]
    if float(number).is_integer == False:
        print('{0} is not a positive integer'.format(number))
    if number % 2 == 0:
        return 'Even', next
    if number % 2 != 0:
        return 'Odd', next



# y = input('how far into the future do you want to see? ')
# res = [[[2**i, 2**(i+1)] for i in range(y)] for y in range(20)]
# print(res)
if __name__ == '__main__':
    # print(vending_maching(int(input('Enter a number: '))))

    # get_roots(float(input('Enter a: ')),float(input('Enter b: ')),float(input('Enter c: ')))

    # try:
    #     x = int(input('Enter a number to factor: '))
    #     x = float(x)
    #     if x>0 and x.is_integer():
    #         print(get_factors(x))
    #     else:
    #         print(int(x),'is not an integer greater than 1')
    # except ValueError:
    #     print('Please enter an integer')
    get_multiplication_table(int(input('Enter the number: ')), int(input('Enter the number up to which to calculate: ')))

def CreateGraph():
    # from pylab import plot, show, legend, title, xlabel, ylabel, axis
    import matplotlib.pyplot as plt
    months = range(1,13)
    nyc_temp_2000 = [31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 72.3, 72.7, 66.0, 57.0, 45.3, 31.1]
    nyc_temp_2006 = [40.9, 35.7, 43.1, 55.7, 63.1, 71.0, 77.9, 75.8, 66.6, 56.2, 51.9, 43.6]
    nyc_temp_2012 = [37.3, 40.9, 50.9, 54.8, 65.1, 71.0, 78.8, 76.7, 68.8, 58.0, 43.9, 41.5]
    plt.plot(months, nyc_temp_2000, months, nyc_temp_2006, months,nyc_temp_2012)
    plt.legend([2000,2006,2012]) #must come after plot()

    # years = range(2000,2013)
    # nyc_avg_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4, 57.3]
    # plt.plot(years, nyc_avg_temp,'o')

    plt.title('NY Average Temperature by Month')
    plt.xlabel('Month')
    plt.ylabel('Fahrenheit')
    # axis(ymin=0) #can retrieve current range of data and set a new range for the axes (returns in a tuple with following patter: xmin, xmax, ymin, ymax)
    # plt.axis([6,9,0,80]) #using a list to set the min and max of the axes
    plt.savefig("mygraph.png") #can save as PDF, PNG, or SVG file; must come before show() to work correctly
    plt.show() #shows all the objects created by plot(), legend(), xlabel, ylabel, etc before it is called
