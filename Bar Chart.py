import matplotlib.pyplot as plt 
def create_bar_chart(data, labels):
    #number of bars
    num_bars = len(data)
    #This list is the point on the y-axis where each bar is centered. Here it will be [1,2,3,...]
    positions = range(1, num_bars+1)
    #barh() is the method that creates bar charts (like plot() but for bar charts)
    plt.barh(positions, data)
    #Set the label of each bar
    plt.yticks(positions, labels)
    plt.xlabel('Steps')
    plt.ylabel('Day')
    plt.title('Number of steps walked')
    #Turns on the grid which may assist in visual estimation
    plt.grid()
    plt.show()

if __name__ == '__main__':
    #Number of steps I walked during the past week
    steps = [6534,7000,8900,10786,3467,11045,5095]
    #Corresponding days
    labels = ['Sun','Mon','Tue','Wed','Thurs','Fri','Sat']
    create_bar_chart(steps, labels)