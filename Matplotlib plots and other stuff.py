import os
import matplotlib.pyplot as plt

# class variable_dict(dict):
#     dict = dict()

#     def add(self,k, v):
#         self.dict[k] = v
    
#     def remove(self,k):
#         self.dict.pop(k)

# v = variable_dict()
# v.add('test',1)
# print(v.dict)
# v.remove('test')
# print(v.dict)

def calculate_linear_correlation(s1, s2):
    if len(s1) != len(s2):
        raise Exception('The two sets must be the same length')
    sum_of_sum1_squares, sum_of_sum2_squares, product = 0, 0, 0
    sum1 = sum(s1)
    sum2 = sum(s2)
    sum1_squared = sum1**2
    sum2_squared = sum2**2
    n = len(s1)
    for x, y in zip(s1, s2):
        product += x*y
        sum_of_sum1_squares += x**2
        sum_of_sum2_squares += y**2
    correlation = (n*product-sum1*sum2) / ((n*sum_of_sum1_squares-sum1_squared)*(n*sum_of_sum2_squares-sum2_squared))**.5
    return correlation

def draw_scatter(x,y):
    plt.scatter(x,y)
    plt.show()    

def find_percentile(l, percentile):
    # assert l is list
    item_count = len(l)
    # assert percentile is int
    assert percentile >= 0 and percentile <= 100
    l.sort()
    if percentile == 100:
        return l[len(l)-1]
    elif percentile == 0:
        return l[0]
    print("l is:",l)
    i = item_count*percentile/100 + .5
    print('i is',i)
    if i.is_integer():
        return l[int(i-1)]
    else:
        k = int(i)
        f = i - k
        return ((1-f)*l[k-1] + f*l[k])

def find_percentile_score(data, percentile):
    if percentile < 0 or percentile > 100:
        return None
    data.sort()
    if percentile == 0:
        return data[0]
    if percentile == 100:
        return data[-1]
    n = len(data)
    i = ((n*percentile)/100) + 0.5

    if i.is_integer():
        real_idx = int(i-1)
        return data[real_idx]
    else:
        k = int(i)
        f = i - k
        real_idx_1 = k - 1
        real_idx_2 = k 
        return (1-f)*data[real_idx_1] + f*data[real_idx_2]

l = [10,20,30,40,2,7,6,3,4]

def __create_classes__(data,n):
    
    low = float(min(data))
    high = float(max(data))
    width = float((high-low)/n)
    classes = []
    next_item = 0
    while next_item < high-width:
    # for i in range(n):
        next_item = low + width
        classes.append((low, next_item))
        low = next_item  
    classes.append((next_item, high+1))    
    return classes

def draw_frequency_table(data, n):
    '''creates a number n of evenly placed ranges for the values in numbers'''
    classes = __create_classes__(data, n)
    frequencies = __categorize_values_by_class__(data,classes)
    # print('classes:',classes,'and freq:', frequencies)
    print('Grade\t\tFrequency')
    for i in range(len(classes)):
        print('{0}-{1}\t\t{2}'.format(classes[i][0], classes[i][1],frequencies[i]))



def __categorize_values_by_class__(data, classes):
    frequency = []
    # print('data is:',data)
    class_length = len(classes)
    # print('Class length',class_length)
    for i in range(class_length):
        n = 0
        for v in data:
            if v >= classes[i][0] and v< classes[i][1]:
                # print(v,'is between', classes[i][0], 'and',classes[i][1])
                n += 1
        # print('n is:',n)
        frequency.append(n)
    return frequency

l=[7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1,10]
l.sort()
draw_frequency_table(l,3)
    


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
                item[i] = item[i].lstrip()
                temp_list.append(item[i])
                # print('adding {0} to temp_list'.format(item[i]))
        sorted_lists.append(temp_list)
    return sorted_lists

def create_named_lists(lists):
    for i in range(len(lists)):
        # print('i:',i)
        # print('lists:',lists)
        # print('length of lists:',len(lists))
        name = lists[i][0]
        exec("%s = lists[i]" % (name))
        exec("print('%ss are:', %s)" % (name, name))


def calculate_cost_to_drive(cost_per_gallon, miles_per_day, mpg):
    number_of_work_days = 5*52
    cost_per_year = cost_per_gallon * miles_per_day * number_of_work_days / mpg
    return round(cost_per_year,2)

if __name__ == '__main__':
    # lists =  read_csv_file('data.txt',',')
    # create_named_lists(lists)
    # l1 = [1,0,-2,-4,-3,-1,3]
    # l2 = [5,6,8,10,9,7,3]
    # print(calculate_linear_correlation(l1,l2))
    # print(calculate_cost_to_drive(3.5,50,34))
    # print(find_percentile_score(l,0))
    # print(find_percentile(l, 0))
    pass
