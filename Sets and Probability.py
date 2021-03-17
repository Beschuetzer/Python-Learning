from sympy import FiniteSet, symbols, Symbol, pi, pprint, solve, expand, factor
from fractions import Fraction
from matplotlib_venn import venn3
import matplotlib.pyplot as plt
import random
import timeit

def iterate_nicely(items):
    i = 0
    for s in items:
        i += 1
        print('Item number', i, 'is:', s)

# s = FiniteSet(1,2.35,6, Fraction(3, 7)) #a set of discrete numbers; sets use {} in python amd don't keep track of order
# s_length = len(s) #cardinality of set s
# print(2.35 in s) # checking membership of a set
# l = [1,6,8]
# s3 = FiniteSet(*l) # creating a set from a list/tuple (need the * python syntax before the list so each item is passed individually rather then as a whole)
# s2 = FiniteSet() #empty set
# print(s, s2)
# s4 = FiniteSet(4,5,6) 
# s5 = FiniteSet(6,5,4)
# print(s5 == s4) #sets are equal when they contain all the same members
# s6 = FiniteSet(3,4)
# s7 = FiniteSet(3,7,8,4)
# print(s6.is_subset(s7), s7.is_superset(s6)) #using is_... methods to determine super and subsets
# #emptysets are subsets of all sets and any set is also a subset of itself
# s = FiniteSet(1,2,3)
# power_set = s.powerset() #power sets are the set of all possible subsets of a given set; a set of s has precisely 2^s subsets where s is the cardinality (length) of s, so set {1,2,3,4} has a cardinality of 4 and its powerset is 2^4 or 16
# print(power_set)
# s = FiniteSet(1,2,3,4)
# t = FiniteSet(1,2,3)

# print(s.is_proper_subset(t), t.is_proper_subset(s)) #proper subsets/supersets differ by at least one member (i.e. s1 != s2)

# #rational numbers are numbers that can be expressed by a fraction (all integers plus and number with a decimal ending that terminates or repeats)
# #irrational numbers don't terminate or repeat
# #real numbers are the set of all irrational and rational numbers
# #complex number are the set of all real numbers and all numbers with an imaginary component

# s = FiniteSet(1,2,4)
# s2 = FiniteSet(1,2,3)
# s3 = FiniteSet(2,4,5,6)
# print('Union:',s.union(s2)) #union of two sets is a set that contains all of the distinct members of the two sets (e.g. {1,2,4} U {1,2,3} = {1,2,3,4})
# print('Intersection',s.intersection(s2)) #intersection of two sets is a set that contains all the common members of both sets (e.g {1,2,4} ∩ {1,2,3} = {1,2})
# print('Multiple Unions', s.union(s2).union(s3))
# print('Multiple Intersections', s.intersection(s2).intersection(s3))
# cartesian = s * s2 #cartesian product of two sets creates a set that consists of all possible pairs made by taking an element from each set (need to iterate through them to get the individual items)
# print('Cartesian Set:',cartesian)
# iterate_nicely(cartesian)

# cartesian = s**3 #applying the exponential operator (**) to a set gives of the Cartesian product of that set times itself the specified number of times; useful for finding all possible combinations of the set members
# print('Cardinal set (set with **3 exponent):', cartesian)
# iterate_nicely(cartesian)

#Applying a Formula to Multiple Sets of Variables
# def calculate_time_period(length, g):
#     t = 2*pi*(length/g)**.5 #Formulat fo the time period of a simple pendulum of length L; g = 9.8 m/s^2 and pi = 3.141592653...
#     return t

# if __name__ == '__main__':
#     L = FiniteSet(15,18,21,22.5,25) #in cm but need to convert to meters later
#     G = FiniteSet(9.8, 9.78, 9.83)
#     print('{0:^15}{1:^15}{2:^15}'.format('Length(cm)','Gravity(m/s^2)','Time Period(s)'))
#     for elem in L*G: #L*G is the cartesian product of the two sets; could achieve the same results by doing two for loops
#         l = elem[0]
#         g = elem[1]
#         t = calculate_time_period(l/100, g)
#         print('{0:^15}{1:^15}{2:^15}'.format(float(l), float(g), round(float(t),4)))

#Sample Space is all possible outcomes of an expirement (e.g. the sample space for a six-sided die roll is {1,2,3,4,5,6}); 'S' is used in the formulae to represent sample space
#An Event is a set of outcomes that we want to calculate the probability of and that form a subset of the sample space; 'E' is used in the formulae to represent an Event
#Uniform distribution means that each outcome in the sample space is equally likely to occur
#P(E) = n(E)/n(S)
def probability(event, space): 
    types = (FiniteSet, list, tuple, set)
    assert isinstance(event, types)
    assert isinstance(space, types)
    return round(len(event)/len(space) * 100, 4)

def is_prime(number):
    assert number > 0, 'Number must be greater than 0'
    if number == 1:
        return True
    if number == 2:
        return True
    for n in range(2, int(number**.5)+1):
        if number % n == 0:
            # print(number, 'is not prime because',n,'is a factor of' ,n)
            return False
    return True

# if __name__ == '__main__':
#     space = FiniteSet(*range(1,21))
#     primes = []
#     for num in space:
#         if is_prime(num):
#             primes.append(num)
#     event = FiniteSet(*primes)
#     prob = probability(event, space)
#     print('Event: {0}'.format(event))
#     print('Sample Space: {0}'.format(space))
#     print('Probability: {0}%'.format(prob))
#     pass

#Probability of either Event A and Event B
#use the union of Event A and Event B as the event set
#Probability of either Event A or Event B
#use the intersection of Event A and Event B as the event set
def convert_to_finite_set(*kwarg):
    types = (FiniteSet, list, tuple, set)
    assert isinstance(kwarg[0], types)
    res = []
    for i in range(1, len(kwarg)):
        assert isinstance(kwarg[i], types)
        # print(kwarg[i])
        temp = FiniteSet(*kwarg[i])
        res.append(temp)
    return res

def calculate_event_space(*kwarg, operation='and'):
    set_list = convert_to_finite_set(*kwarg)
    res = set_list[0]
    for i in range(1, len(set_list)):
        assert isinstance(set_list[i], FiniteSet)
        # print(set_list[i])
        if operation.upper() == 'AND':
            res = res.union(set_list[i])
        elif operation.upper() == 'OR':
            res = res.intersection(set_list[i])
    return res

def print_results(event, space):
    prob = probability(event, space)
    print('Event: {0}'.format(event))
    print('Sample Space: {0}'.format(space))
    print('Probability: {0}%'.format(prob))

# if __name__ == '__main__':
#     space = [i for i in range(1,21)]
#     event = calculate_event_space([1,2,3,4,5,6],FiniteSet(4,5,6,7,8,9),[3,7,9,35,23,33],operation='OR')
#     print_results(event, space)

#     #Generating random numbers inclusive of the arguments
#     #Roll a die until score adds up to 20
#     count, total = 0, 0
#     target_score = 20
#     while total < target_score:
#         roll = random.randint(1, 6)
#         total += roll
#         count += 1
#     print('Score of {0} reached in {1} rolls'.format(total, count))

    #Is the target score possible in the given number or die rolls? If so what is the probability?
def get_event_space(target_score, space, roll_count):
    res = []
    for s in space:
        if sum(s) >= target_score:
            res.append(s)
    print('Number of outcomes greater than or equal to {0} with {1} rolls: {2}'.format(target_score, roll_count, len(res)))
    return res

def find_prob(target_score, roll_count):
    '''returns the probability of getting at least the target sum is possible given the number of rolls given'''
    assert isinstance(roll_count, int)
    roll_poss = FiniteSet(1,2,3,4,5,6)
    space = roll_poss**roll_count
    event = get_event_space(target_score, space, roll_count)
    prob = round(len(event)/len(space) * 100, 4)
    print('Sample Space: {0}\nProbability: {1}%'.format(len(space),prob))

# if __name__ == "__main__":
#     start = timeit.default_timer()

#     try:
#         target_score = int(input('Enter the target score: '))
#         roll_count = int(input('Enter the maximum number of rolls: '))
#         assert target_score > 0, 'Target score must be larger than 0'
#         assert roll_count > 0, 'Number of rolls must be larger than 0'
#         find_prob(target_score, roll_count)
#     except ValueError:
#         raise Exception('Invalid Input')
#     stop = timeit.default_timer()
#     print('Time: ',stop - start)


#mimicks a biased coin toss where heads is 2x more likely than tails (66% percent heads)
def toss():
    #0 -> Heads, 1 -> Tails
    if random.random() < 2/3:
        return 0
    else:
        return 1

'''Simulate a fictional ATM that dispenses dolar bills of various denominations with varying probabilty'''
import random
def get_probs(probs):
    assert sum(probs) >= .9999999999999999, 'the sum of the probabilities must be 1'
    res = []
    k = 0
    m = 0
    for i in range(len(probs)):
        m = k
        first = probs[0]
        while m > 0: 
            first += probs[m]
            m -= 1
        res.append(first)
        k += 1
    return res

def get_item(items_list, probs_list=[]):
    '''items_list is a list of the corresponding items.
    
    probs_list is a list of the probability of getting each item.  If omitted, it is assumed each item has the same probability.
    '''
    if probs_list != []:
        r = random.random()
        probs = get_probs(probs_list)
        condition1 = 0
        for i in range(len(probs)):
            if r == 0:
                return items_list[0]
            elif r == 1:
                return items_list[len(items_list)]
            if r > condition1 and r <= probs[i]:
                return items_list[i]
            condition1 = probs[i]
    else:
        item = random.choice(items_list)
        return item
    

def pick_item():
    dollar_bills = [5, 10, 20, 50, 100]
    probs = [1/6, 1/6, 1/3, 1/4, (1-2/3-1/4)]
    return get_item(dollar_bills, probs)

def calculate_payment(principal=None, rate=None, num_months=None):
    try:
        if principal == None:
            principal = float(input('What is the principal: '))
        if rate == None:
            rate = float(input('What is the rate: '))
        if num_months == None:
            num_months = int(input('What is the length of the loan (term): '))
    except TypeError:
        raise Exception('Invalid Input.')
    else:
        num = (rate/12 * principal)
        denom = (1 - (1 + rate/12)**-num_months)
        montly_payment = round(num/denom,2)
        total_financed = montly_payment * num_months
        difference = round(total_financed - principal, 2)
        percent_extra = round((difference) / principal * 100, 2)
        print("Monthly payment: {0}\nAmount Paid in Interest: {1}\nPercent Extra paid: {2}".format(montly_payment, difference, percent_extra))

def calculate_budget():
    rent = 1100
    food = 500
    insurance = 100
    phone = 70
    car_payment = 300
    internet = 65
    car_payment_reimbursement = -0
    expenses = [rent, food, insurance, phone, car_payment, internet, car_payment_reimbursement]
    sum_expenses = sum(expenses)
    hourly_rate = 16.97
    yearly_income = hourly_rate * 40 * 50
    take_home_rate = .7846
    monthly_disposable_income = yearly_income * take_home_rate / 12
    remaining = monthly_disposable_income - sum_expenses
    print("Disposable Income: {0}\nExpenses: {1}\nNet Remaining: {2}".format(monthly_disposable_income, sum_expenses, remaining))

def get_primes_in_range(start_num, num):
    res = []
    assert isinstance(num, int), 'Number must be int'
    assert isinstance(start_num, int), 'Number must be int'
    for n in range(start_num, num):
        if is_prime(n):
            res.append(n)
    return res

if __name__ == "__main__":
#     down = [0,1000,2000,3000,4000,5000,6000,7000]
#     for item in down:
#         calculate_payment(principal=11000-item, rate=.0509, num_months=36)
#     calculate_budget()
    test = []
    for i in range(200000):
        test.append(pick_item())
    test_length = len(test)
    print('Total: {0}'.format(test_length))
    for item in set(test):
        total = test.count(item)
        print('Percent that are {0}: {1}'.format(item ,total/test_length))

'''Drawing a Venn diagram (use venn2() for two sets and venn3 for three sets; from matlibplot_venn)'''
def read_csv_file(filename, separator,order='vertical'):
    sorted_lists = []
    res = {}
    l2 = []
    with open(filename) as f:
        for line in f:
            l = line.split(separator)
            header = l
            number_of_elements = len(l)
            # print('length of l:', number_of_elements)
            l2.append(header)
            break
        for line in f:
            l = line.split(separator)
            l2.append(l)
    # print('l2:',l2)
    for i in range(len(l2[0])):
        # print('i:',i)
        temp_list = []
        for item in l2:
            if len(item) != number_of_elements or "" in item:
                raise Exception(r"The number of headers doesn't match match the elements on line", line)
            else:
                # print('item', item)
                item[i] = item[i].replace('\n','')
                temp_list.append(item[i])
                # print('adding {0} to temp_list'.format(item[i]))
        sorted_lists.append(temp_list)
    if order.lower() == 'vertical':
        for i in range(len(sorted_lists)):
            exec("res[sorted_lists[i][0]] = sorted_lists[i][1:] ")
    elif order.lower() == 'horizontal':
        return l2
    return res

def draw_venn3_dynamically(filename):
    '''Draws a 3 set venn diagram using a CSV file named filename

    Each row is an entry for a unique item

    Only works if columns are binary choices (1 or 0)
    '''
    data = read_csv_file(filename, ',',     order='horizontal')
    sets = data[0][1:]
    new_set = []
    for s in sets:
        s = s.lower().lstrip().rstrip().replace(' ','')
        new_set.append(s)
        exec("%s=[]" % (s))
    for item in data:
        if item[1:] == ['1','1','1']:
            exec("%s.append(item[0])" % new_set[0])
            exec("%s.append(item[0])" % new_set[1])
            exec("%s.append(item[0])" % new_set[2])
        elif item[1:] == ['1','1','0']:
            exec("%s.append(item[0])" % new_set[0])
            exec("%s.append(item[0])" % new_set[1])
        elif item[1:] == ['1','0','0']:
            exec("%s.append(item[0])" % new_set[0])
        elif item[1:] == ['1','0','1']:
            exec("%s.append(item[0])" % new_set[0])
            exec("%s.append(item[0])" % new_set[2])
        elif item[1:] == ['0','1','0']:
            exec("%s.append(item[0])" % new_set[1])
        elif item[1:] == ['0','1','1']:
            exec("%s.append(item[0])" % new_set[1])
            exec("%s.append(item[0])" % new_set[2])
        elif item[1:] == ['0','0','1']:
            exec("%s.append(item[0])" % new_set[2])
    for i in range(len(new_set)):
        exec("%s=FiniteSet(*%s)" % (new_set[i],new_set[i]))
        # print('Set {1}: {0}'.format(new_set[i], i+1))
    labels = new_set
    exec("venn3(subsets=[%s, %s, %s], set_labels=(%s))" % (new_set[0],new_set[1],new_set[2], labels))
    plt.show()
# if __name__ == "__main__":
#     draw_venn3_dynamically('data.txt')

'''Law of large numbers; discrete random variables only take integral values.  Continuous random variables can take any real value

The expectation (E) of a discrete random variable is the equivalent of the average or mean:
E = x_1*P(x_1)+x_2*P(x_2)+x_3*P(x_3)+...+x_n*P(x_n)
'''
# E = 1*(1/6)+2*(1/6)+3*(1/6)+4*(1/6)+5*(1/6)+6*(1/6)
# if __name__ == "__main__":
#     probs = [1/6,1/6,1/6,1/6,1/6,(1-5/6)]
#     items = [1,2,3,4,5,6]
#     trials = [100, 1000, 10000, 100000, 500000,1000000]
#     for t in trials:
#         res = []
#         for i in range(t):
#             res.append(get_item(probs, items))
#         avg = sum(res) / len(res)
#         print('Trials: {0} Trial Average: {1}'.format(t, avg))
'''Shuffling a deck'''
def create_deck_dict():
    rank = FiniteSet('Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King')
    suites = FiniteSet('clubs', 'diamonds', 'spades', 'hearts')
    card_dict = {}
    i = 1
    for s in suites:
        for r in rank:
            card_dict[i] = '{0} of {1}'.format(r, s)
            i += 1
    return card_dict
    
# if __name__ == "__main__":
#     card_dict = create_deck_dict()
#     cards = [i for i in range(1,53)]
#     random.shuffle(cards)
#     for c in cards:
#         print(card_dict[c])

#Estimating the Area of a Circle
# if __name__ == "__main__":
#     pass
#     r = 2
#     square_area = (2*r)**2
#     circle_area = 3.141592654 * r**2
#     prob_in_circle = circle_area / square_area
#     prob_outside_circle = 1 - prob_in_circle
#     prob = [prob_in_circle, prob_outside_circle]
#     result = [1, 0]
#     darts = [1000,10000,100000,1000000,10000000]
#     pprint('Circle Radius: {0}\nArea of Circle: {1}'.format(r, circle_area))
#     for d in darts:
#         throw = []
#         for i in range(d):
#             throw.append(get_item(prob, result))
#         hits = throw.count(1)
#         estimated_cirlce_area = hits / d * square_area
#         miss = d - hits
#         assert hits + miss == d
#         print('Estimated Radius with {0} darts: {1}'.format(d, estimated_cirlce_area))
#         print('Estimate of PI: {0}'.format(hits/d*4))


# get_item(probs_list, items_list)
# fraction = n / (n+m)