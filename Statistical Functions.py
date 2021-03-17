from collections import Counter

def calculate_mean(numbers):
    assert type(numbers) is list
    return sum(numbers) / len(numbers)


def calculate_mode(numbers):
    assert type(numbers) is list
    c = Counter(numbers)
    mode = []
    most_common_list = c.most_common()
    highest_freq = most_common_list[0][1]
    for n in most_common_list:
        if n[1] == highest_freq:
            mode.append(n[0])
    return mode

def calculate_median(numbers):
    assert type(numbers) is list
    numbers.sort()
    len_numbers = len(numbers)
    if len_numbers % 2 == 0:
        n1 = len_numbers / 2
        n2 = len_numbers / 2 + 1
        n1 = int(n1) -1
        n2 = int(n2) -1
        median = (numbers[n1] + numbers[n2]) / 2
    else:
        n1 = int(len_numbers / 2)
        median = numbers[n1]
    return median

def calculate_variance(numbers):
    assert type(numbers) is list
    mean = calculate_mean(numbers)
    v = []
    for n in numbers:
        variance = (n - mean)**2
        v.append(variance)
    res = sum(v) / len(numbers)
    return res

def calculate_standard_deviation(numbers):
    assert type(numbers) is list
    res = calculate_variance(numbers)**.5
    return res

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



if __name__ == '__main__':
    l = [382, 389, 377, 397, 396, 368, 369, 392, 398, 367, 393,396]
    l1 = [1,0,-2,-4,-3,-1,3]
    l2 = [5,6,8,10,9,7,3]
    # print(calculate_linear_correlation(l1,l2))
    # print(calculate_median(l))
    # print(calculate_mode(l))
    # print(calculate_standard_deviation(l))
    # print(calculate_variance(l))
