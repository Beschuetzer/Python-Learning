'''Patches allow us to draw geometric shapes, each of which is called a patch'''
#When calling plot(), it creates a Figure() object; we can do this manually so:
import matplotlib.pyplot as plt
import math
# x = [1,2,3]
# y = [1,2,3]
# fig = plt.figure()
# ax = plt.axes()
# plt.plot(x,y)
# plt.show()

'''Creating a circle'''
def create_circle(center_coordinates, radius):
    circle = plt.Circle(center_coordinates, radius = radius, fc='b', ec='b') #fc means fill color and ec edge color
    return circle

def show_shape(patch):
    ax = plt.gca() #stands for get current axis and creates one if one hasn't been created yet
    ax.add_patch(patch) #adds the patch (in this case the circlce object) passed to it to the plot; mathplotlib supports other patches such as Ellispe(), Polygon(), and Rectangle()
    ax.set_aspect('equal') #sets the aspect ratio of the axes
    plt.axis('scaled') #tells it to automatically adust the axis limits
    plt.show()

# if __name__ == "__main__":
#     c = create_circle([0,0],.5)
#     show_shape(c)

'''Creating animated figures'''
from matplotlib import animation

def update_radius(i, circle):
    circle.radius = i * .05
    return circle


def create_animation():
    fig = plt.gcf()
    ax = plt.axes(xlim=(-10,10), ylim=(-10,10))
    ax.set_aspect('equal')
    circle = create_circle([0,0],.5)
    ax.add_patch(circle)
    #need to create a label for the animation.FuncAnimation object otherwise Python's garbage collection deletes it as it isn't referenced anywhere
    anim = animation.FuncAnimation(fig, update_radius, fargs= (circle,), frames=200, interval=1)
    plt.title('Simple Circle Animation')
    plt.show()

#creating a simple circle expanding animation
# if __name__ == "__main__":
#     create_animation()

'''Animating a Projectile's Trajectory'''
g = 9.8

def get_intervals(u, theta):
    t_flight = 2*u*math.sin(theta)/g
    intervals = []
    start = 0
    interval = .005
    while start < t_flight:
        intervals.append(start)
        start += interval
    return intervals

def update_position(i, circle, intervals, u, theta):
    t = intervals[i]
    x = u*math.cos(theta)*t
    y = u*math.sin(theta)*t - .5*g*t**2
    circle.center = x, y
    return circle,

def create_animation2(u, theta):
    intervals = get_intervals(u, theta)
    xmin = 0
    xmax_temp = u*math.cos(theta)*intervals[-1]
    xmax = xmax_temp * 1.05
    ymin = 0
    t_max = u*math.sin(theta)/g
    ymax_temp = u*math.sin(theta)*t_max - .5*g*t_max**2
    ymax = ymax_temp * 1.1
    fig = plt.gcf()
    circle_size = ymax_temp / xmax_temp
    ax = plt.axes(xlim=(xmin, xmax), ylim=(ymin, ymax))
    circle = plt.Circle((xmin, ymin), circle_size)
    ax.add_patch(circle)
    anim = animation.FuncAnimation(fig, update_position, fargs=(circle, intervals, u, theta), frames=len(intervals), interval=.1)
    plt.title('Projectile Motion')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

# if __name__ == "__main__":
#     try:
#         u = float(input('Enter the intitial velocity (m/s): '))
#         theta = float(input('Enter the angle of projection (degrees): '))
#     except ValueError:
#         print('You entered an invalid input')
#     else:
#         theta = math.radians(theta)
#         create_animation2(u, theta)

'''Drawing Fractals'''
#fractals invole the repetitive application of the same geometric transformation of points in a plane.
'''Example of selecting a transformation from two equally probable transformations'''
import random

# def transformation_1(p):
#     x = p[0]
#     y = p[1]
#     return (x+1, y-1)

# def transformation_2(p):
#     x = p[0]
#     y = p[1]
#     return (x+1, y+1)

# def transform(p):
#     #list of transformation functions
#     transformations = [transformation_1, transformation_2]
#     t = random.choice(transformations)
#     x, y = t(p)
#     return x, y

# def build_trajectory(p, n):
#     x = [p[0]]
#     y = [p[1]]
#     for i in range(n):
#         p = transform(p)
#         x.append(p[0])
#         y.append(p[1])
#     return x, y
    
# if __name__ == "__main__":
#     #Initial Point
#     p = (1,1)
#     n = int(input('Enter the number of iterations: '))
#     x, y = build_trajectory(p, n)
#     plt.plot(x, y)
#     plt.xlabel('X')
#     plt.ylabel('Y')
#     plt.show()
def transformation_1(p):
    x = p[0]
    y = p[1]
    return (.85*x + .04*y, -.04*x + .85*y + 1.6)

def transformation_2(p):
    x = p[0]
    y = p[1]
    return (.2*x -.26*y, .23*x + .22*y + 1.6)

def transformation_3(p):
    x = p[0]
    y = p[1]
    return (-.15*x + .28*y, .26*x + .24*y + .44)

def transformation_4(p):
    y = p[1]
    return (0,.16*y)

def get_prob_ranges(probs):
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
        probs = get_prob_ranges(probs_list)
        condition1 = 0
        for i in range(len(probs)):
            if r == 0:
                return items_list[0]
            elif r == 1:
                return items_list[len(items_list)]
            elif r > condition1 and r <= probs[i]:
                return items_list[i]
            condition1 = probs[i]
    else:
        item = random.choice(items_list)
        return item

# if __name__ == "__main__":
#     try:
#         n = int(input('Enter the number of iterations:'))
#     except TypeError:
#         raise Exception('Invalid number')
#     transformations = [transformation_1, transformation_2, transformation_3, transformation_4]
#     probs = [.85, .07, .07, .01]
#     p = (0,0)
#     x, y = [0], [0]
#     for i in range(n):
#         transformation = get_item(transformations, probs_list=probs)
#         p = transformation(p)
#         x.append(p[0])
#         y.append(p[1])
#     plt.plot(x, y, 'o')
#     plt.title('Barnsley Fern Fractal ({0} iterations)'.format(n))
#     plt.show()

'''Packing Circles into a Square'''
from matplotlib import pyplot as plt
def draw_square(points, limits):
    assert len(points) == 4, 'There must be 4 points to draw a square'
    assert isinstance(points, (tuple, list)),'The points object must be a list or tuple'
    assert len(limits) == 2, 'The limits iterable must have to objects which represent x and y limits (x_min, xmax), (y_min, y_max)'
    assert isinstance(limits, (list, tuple)),'The limits object must be a list or tuple'
    ax = plt.axes(xlim=limits[0], ylim=limits[0])
    square = plt.Polygon(points, closed=True) #closed tells matplotlib we want to draw a closed polygon, where the starting and ending vertices are the same; the points are drawn in the order in which they are given like connect the dots
    ax.add_patch(square)

def show_shape2(shape):
    ax = plt.gca()
    ax.add_patch(shape)
    ax.set_aspect('equal')
    plt.axis('scaled')

def get_maximums(points):
    x = points[0][0]
    y = points[0][1]
    for p in points[1:]:
        if p[0] > x:
            x = p[0]
        if p[1] > y:
            y = p[1]
    assert y == x, 'Object must be a square'
    return x,y

def get_minimums(points):
    x = points[0][0]
    y = points[0][1]
    for p in points[1:]:
        if p[0] < x:
            x = p[0]
        if p[1] < y:
            y = p[1]
    assert y == x, 'Object must be a square'
    return x,y

def confirm_circle(points):
    assert abs(points[0][0] - points[1][0]) == abs(points[2][0] - points[3][0]), 'Check the x coordinates of the circle'
    assert abs(points[0][1] - points[1][1]) == abs(points[2][1] - points[3][1]), 'Check the y coordinates of the circle'
    assert abs(points[1][0] - points[2][0]) == abs(points[3][0] - points[0][0]), 'Check the x coordinates of the circle'
    assert abs(points[1][1] - points[2][1]) == abs(points[3][1] - points[0][1]), 'Check the y coordinates of the circle'

def pack_circles_into_triangle():
    try:
        radius = float(input('What is the radius of the circles to fit into the square: '))
    except TypeError:
        raise Exception('Invalid Number')
    except ValueError:
        raise Exception('Invalid Number')
    else:
        p1 = 1,1
        p2 = 1,5
        p3 = 5,5
        p4 = 5,1
        points = [p1, p2, p3, p4]
        confirm_circle(points)
        x_max, y_max = get_maximums(points)
        x_min, y_min = get_minimums(points)
        x_range = x_max - x_min
        y_range = y_max - y_min
        circle_number = int(x_range / radius / 2)
        xlim = x_min,x_max
        ylim = y_min,y_max
        limits = [xlim, ylim]
        draw_square(points, limits) 
        center = (x_min + radius, y_min + radius)
        counter = 1
        for i in range(circle_number**2):            
            circle = create_circle(center,radius)
            show_shape2(circle)
            x = center[0]
            y = center[1]
            if counter % circle_number == 0:
                center = (x_min + radius, y + 2*radius)
            else:
                center = (2*radius + x, y)
            # print('x:',x,'y;',y)
            # print('center:', center)
            # print('counter', counter)
            counter += 1
        plt.title('{0} circles fit into the square'.format(circle_number**2))
        plt.show()

# if __name__ == "__main__":
#     pack_circles_into_triangle()

'''Sierpinski Triange'''
def transformation_striangle_1(p):
    x = p[0]
    y = p[1]
    return x * .5, y * .5
def transformation_striangle_2(p):
    x = p[0]
    y = p[1]
    return x *.5 + .5, y *.5 + .5
def transformation_striangle_3(p):
    x = p[0]
    y = p[1]
    return x * .5 + 1, y * .5

def get_sierpinski_triangle_points(n):
    p = (0,0)
    sierpinski_transformations = [transformation_striangle_1, transformation_striangle_2, transformation_striangle_3]
    x, y = [],[]
    for i in range(n):
        x.append(p[0])
        y.append(p[1])
        t = get_item(sierpinski_transformations)
        p = t(p)
    return x, y

def draw_sierpinski_triange():
    try:
        n = int(input('How many iterations would you like to use: '))
    except ValueError:
        raise Exception('Invalid integer')
    else:
        colors = ['red','green','yellow','blue','magenta','cyan','white','black']
        x, y = [],[]
        x, y = get_sierpinski_triangle_points(n)
        assert len(x) == len(y),'The lists for the x and y coordinates must be the same length'
        assert isinstance(x, list),'X must be a list'
        assert isinstance(y, list),'Y must be a list'
        plt.plot(x, y, 'o', color=get_item(colors))  #need to remember that without 'o' argument, plot() connects the points
        plt.title('Sierpinski Triangle with {0} points'.format(n))
        plt.show()

# if __name__ == "__main__":
#     draw_sierpinski_triange()
#     pass

'''Henon Function'''

def henon_transform(p):
    x = p[0]
    y = p[1]
    return (y+1-1.4*x**2, .3*x)

def get_henon_points(n, p):
    x,y = [],[]
    for i in range(n):
        x.append(p[0])
        y.append(p[1])
        p = henon_transform(p)
    return x,y

# if __name__ == "__main__":
#     try:
#         n = int(input('How many points for the Henon function: '))
#     except ValueError:
#         raise Exception('Invalid Integer')
#     else:
#         p = (0,0)
#         x, y = [],[]
#         x, y = get_henon_points(n, p)
#         plt.plot(x,y,'o')
#         plt.title('Henon Function with {0} Points'.format(n))
#         plt.show()

'''Drawing the Mandelbrot Set'''

import matplotlib.cm as cm
from sympy import Symbol, sympify, pprint
import matplotlib.pyplot as plt
import random

def initialize_image(x_p, y_p):
    image = []
    for i in range(y_p):
        x_colors = []
        for j in range(x_p):
            x_colors.append(0)
        image.append(x_colors)
    return image

def color_points():
    num_points = 400
    x_p = num_points
    y_p = num_points
    
    max_iteration = 100
    iteration = 0
    image = initialize_image(x_p, y_p)
    for k in range(y_p):
        for i in range(x_p):
            z1 = complex(0,0)
            c = complex(i,k*-1)
            while abs(z1) < 2 and iteration < max_iteration:
                z1 = z1**2 + c
                iteration += 1
                image[k][i] = iteration
    plt.imshow(image, origin='lower', extent=(-2.5,1,-1,1), cmap=cm.Greys_r, interpolation='nearest') #imshow() automatically deduces the color of a point from its position in the image list and doesn't care about its specific x- and y-coordinates; origin='lower' sets the color of the point (0,0) to image[0][0]; extent=(0,5,0,5) = (xmin, xmax, ymin, ymax); cmap=cm.Greys_r specifies the use of grayscale image; iterpolation='nearest' specifies that matplotlib should color a point for which the color wasn't specified with the same color as the one nearest to it (the reason why there are color 'boxes' around each point in the figure)
    plt.colorbar() #displays the color bar in the figure showing which integer corresponds to which color
    plt.show()

if __name__ == "__main__":
    color_points()


