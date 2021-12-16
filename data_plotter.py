from matplotlib import pyplot as plt

################################
## Functions
################################

def labels():
    labels = []

    ext = input('What is the title of your graph? ')
    labels.append(ext)

    ext = input('What would you like to label your x axis? ')
    labels.append(ext)

    ext = input('What would you like to label your y axis? ')
    labels.append(ext)

    plt.title(labels[0])
    plt.xlabel(labels[1])
    plt.ylabel(labels[2])

def pop():
    '''
    Requests the size of the dataset to be plotted. 
    '''
    while True:
        global pop   
        pop = input('Please enter the sample size: ') 
        is_num0 = None
        try:
            is_num0 = int(pop)
        except:
            if (is_num0 == None):
                print('Enter a numerical value!')
            continue
        else:
            pop = int(pop)
            break  
    

def x_values():                                                 
    '''
    Asks user for sample size before iterating over input command by user defined range.
    while True tests for ability to convert input to float to force accepted input.
    '''
    global x_sample
    x_sample = []                                                
    print('Please enter your x values.')
    
    for i in range(0, pop):
        while True:
            ext = input()  
            is_num0 = None
            try:
                is_num0 = float(ext)
            except:
                if (is_num0 == None):
                    print('Enter a numerical value!')
                continue
            else:
                ext = float(ext)
                x_sample.append(ext)
                break                                  


def y_values():  
    '''
    Asks user for sample size before iterating over input command by user defined range.
    while True tests for ability to convert input to float to force accepted input.
    '''
    global y_sample
    y_sample = [] 
    print('Please enter your y values.')

    for i in range(0, pop):
        while True:
            ext = input()
            ## y_sample.append(ext)  
            is_num0 = None
            try:
                is_num0 = float(ext)
            except:
                if (is_num0 == None):
                    print('Enter a numerical value!')
                continue
            else:
                ext = float(ext)
                y_sample.append(ext)
                break


def x_scale():
    '''
    Uses while True to test for accepted input and prevent errors.
    Plot scales can be changed using log or linear condition in plt.xscale()
    '''

    while True:
        x_scale = input('What scale would you like to make the x axis? linear / log ')
        if x_scale not in ['linear', 'log']:
            print('Please enter a valid input!')
            continue
        else:
            break

    plt.xscale(x_scale)


def y_scale():
    '''
    Uses while True to test for accepted input and prevent errors.
    Plot scales can be changed using log or linear condition in plt.xscale()
    '''

    while True:
        y_scale = input('What scale would you like to make the y axis? linear / log ')
        if y_scale not in ['linear', 'log']:
            print('Please enter a valid input!')
            continue
        else:
            break

    plt.yscale(y_scale)

################################
## Main Body
################################

labels()

pop()

x_values()
y_values()


x_scale()
y_scale()
plt.plot(x_sample, y_sample)
