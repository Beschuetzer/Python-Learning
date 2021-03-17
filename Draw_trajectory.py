import matplotlib.pyplot as plt
import math

def draw_graph(x, y, xlabel='X-axis', ylabel='Y-axis', title='Title', legend=None):
    plt.plot(x, y, marker='o')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

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
    
def draw_trajectory(velocity, theta, height, legend=None):
    '''
    Velocity is in m/s and theta is in degrees
    '''
    g = 9.8
    theta = math.radians(theta)  #converts degrees to radians
    t_vertex = velocity * math.sin(theta) / g
    y = []
    x = []
    for t in frange(0, 1000*t_vertex, .001):
        y_val = velocity * math.sin(theta) * t - .5*g*t*t + height
        x_val = velocity * math.cos(theta) * t
        if y_val >= 0:
            # print('y value: ',y_val)
            y.append(y_val)
            x.append(x_val)
        else:
            break
    # print('Maximum horizontal distance:', max(x))
    # print('Maximum vertical distance:', max(y))
    # print('Minimum vertical distance:', min(y))

    # print('Flight time: ',t_flight)
    draw_graph(x, y, legend=legend, xlabel='Horizontal Distance in meters from thrower', ylabel='Vertical Distance in meters from the ground', title='Trajectory')

def get_roots(a, b, c):
    r_1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
    r_2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
    print('Root 1: {0}'.format(r_1))
    print('Root 2: {0}'.format(r_2))
    return (r_1, r_2)

if __name__ == '__main__':
    #plotting a trajectory
    try:
        times = int(input('Number of trajectories to plot: '))
        count = times
        l = []
        assert times > 0
        while count > 0:
            v = float(input('Enter a velocity in m/s: '))
            theta = float(input('Enter the angle at which the object is thrown in degrees: '))
            height = float(input('Enter the height from which the ball is thrown in meters: '))
            l.append('{0}m/s at {1}° from {2}m'.format(v,theta,height))
            count -= 1
            draw_trajectory(v, theta, height)
    except ValueError:
        print("You entered an invalid input")
    else:
        plt.legend(l, loc='upper right')
        plt.show()

