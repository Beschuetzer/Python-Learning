import matplotlib.pyplot as plt
def fibo(n):
    '''Generates the first n fibonacci numbers'''
    if n<0:
        raise Exception("N must be larger than 0")
    elif n==0:
        return 0
    elif n==1:
        return 1 + fibo(n-1)
    else:
        return fibo(n-1) + fibo(n-2)

# print(fibo(10))

def fibo_list(n):
    '''Generates a list of the first n fibonacci numbers'''
    n1 = 1
    n2 = 1
    l = [1,1]
    if n==1:
        return [1]
    if n==2:    
        return [1,1]
    for i in range(1,n-1):
        n_next = n1+n2
        n1=n2
        n2=n_next
        l.append(n_next)
    return l
# print(fibo_list(10))

def draw_graph(x, y):
    plt.title("Ratio of Fibonacci Numbers")
    plt.xlabel('Nth Fibonacci Number')
    plt.ylabel('Ratio')
    plt.axes(xmin=1, xmax=len(x))
    plt.plot(x,y)
    

if __name__ == '__main__':
    #Number of steps I walked during the past week
    fib_seq = fibo_list(145)
    ratio = []
    x = []
    for i in range(len(fib_seq)-1):
        ratio.append(fib_seq[i+1]/fib_seq[i])
        x.append(i+1)
    draw_graph(x,ratio)
    plt.show()