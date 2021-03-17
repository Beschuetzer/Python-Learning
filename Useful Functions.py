def frange(start, stop, increment):
    '''
    A re-work of range() that includes the stop value.  Increment values must be positive, but they can be a floating point number.
    '''
    values = []
    if increment <= 0:
        raise Exception("The increment value must be greater than 0")
    elif start == stop:
        raise Exception("The start and stop values must be different")
    elif start < stop:
        while start <= stop:
            values.append(round(start, len(str(increment))))
            start = start + increment
    else:
        while start >= stop:
            values.append(round(start, len(str(increment))))
            start -= increment
    return values


def read_csv_file(filename, separator):
    sorted_lists = []
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
    return sorted_lists

def calculate_yearly_cost_to_drive(cost_per_gallon, miles_per_day, mpg):
    number_of_work_days = 5*51
    cost_per_year = (cost_per_gallon * miles_per_day * number_of_work_days / mpg) + (5*cost_per_gallon*2*52 / mpg)
    # print('cost per year:', cost_per_year)
    return round(cost_per_year,2)

def calculate_yearly_cost_difference(gas_cost, miles_driven_a_day, most_effecient_car_mpg, car_considering_mpg):
    print('Cost extra buying the {0} mpg car vs the {1} one: '.format(most_effecient_car_mpg, car_considering_mpg),round(calculate_yearly_cost_to_drive(gas_cost,miles_driven_a_day,car_considering_mpg) - calculate_yearly_cost_to_drive(gas_cost,miles_driven_a_day,most_effecient_car_mpg), 2))

def calculate_loan_monthly_payment(principal=None, rate=None, num_months=None):
    try:
        if principal == None:
            principal = float(input('What is the principal: '))
        if rate == None:
            rate = float(input('What is the rate: '))
            rate_original = rate
            if rate >= 1:
                rate /= 100
            else:
                rate_original *= 100
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
        percent_larger = round((percent_extra-rate_original) / rate_original * 100, 2)
        print("Monthly payment: {0}\nAmount Paid in Interest: {1}\nPercent Extra paid: {2}\nThe total interest upon completion is {3}% larger than the original of {4}%\n".format(montly_payment, difference, percent_extra, percent_larger, rate_original))


if __name__ == '__main__':
    gas_cost = 3
    miles_driven_a_day = 60
    most_effecient_car_mpg = 50
    car_considering_mpg = 42
    calculate_yearly_cost_difference(gas_cost, miles_driven_a_day, most_effecient_car_mpg, car_considering_mpg)
    while True:
        calculate_loan_monthly_payment()
    # print(read_csv_file('data.txt',','))
    # l1 = [1,0,-2,-4,-3,-1,3]
    # l2 = [5,6,8,10,9,7,3]
    # header, data = read_csv_file('data.txt',',')
    # print(header, data)
    # print(calculate_linear_correlation(l1,l2))
    # print(calculate_cost_to_drive(3.5,50,34))
    pass