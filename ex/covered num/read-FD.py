import numpy as np
import matplotlib.pyplot as plt
import show

def readFile(ax, inputFile):
#   fig, ax = plt.subplots()
    inf = open(inputFile)
    line = inf.readline()
    bar_inc = [0, 0.35, 0.7];
    a = ['ICT','SCT','FD']
    color = ['k','k','w']
    dot = ['-', '-.']
    mark = ['o','d']
    i = 0
    lengthMin = 0
    while line:
        line = line.strip()
        if len(line) != 0 and line[0] == '(':
            [x, y] = dealLine(line)
            #get ride of bigger than 100
            if(inputFile.find('tcas') != -1):
                z = [(x[i],y[i]) for i in range(len(x)) if x[i] < 50]
                x = np.array([i[0] for i in z])
                y = np.array([i[1] for i in z])

            if(inputFile.find('2-way tomcat.txt') != -1):
                z = [(x[i],y[i]) for i in range(len(x)) if x[i] < 15]
                x = np.array([i[0] for i in z])
                y = np.array([i[1] for i in z])

            if(inputFile.find('3-way tomcat.txt') != -1):
                z = [(x[i],y[i]) for i in range(len(x)) if x[i] < 25]
                x = np.array([i[0] for i in z])
                y = np.array([i[1] for i in z])

            if(inputFile.find('2-way HSQLDB.txt') != -1):
                z = [(x[i],y[i]) for i in range(len(x)) if x[i] < 15]
                x = np.array([i[0] for i in z])
                y = np.array([i[1] for i in z])
                
            if(inputFile.find('3-way HSQLDB.txt') != -1):
                z = [(x[i],y[i]) for i in range(len(x)) if x[i] < 30]
                x = np.array([i[0] for i in z])
                y = np.array([i[1] for i in z])
                
            if(inputFile.find('4-way HSQLDB.txt') != -1):
                z = [(x[i],y[i]) for i in range(len(x)) if x[i] < 40]
                x = np.array([i[0] for i in z])
                y = np.array([i[1] for i in z])

            if(inputFile.find('2-way JFlex.txt') != -1):
                z = [(x[i],y[i]) for i in range(len(x)) if x[i] < 15]
                x = np.array([i[0] for i in z])
                y = np.array([i[1] for i in z])
                
            if(inputFile.find('3-way JFlex.txt') != -1):
                z = [(x[i],y[i]) for i in range(len(x)) if x[i] < 25]
                x = np.array([i[0] for i in z])
                y = np.array([i[1] for i in z])

            if(inputFile.find('4-way JFlex.txt') != -1):
                z = [(x[i],y[i]) for i in range(len(x)) if x[i] < 35]
                x = np.array([i[0] for i in z])
                y = np.array([i[1] for i in z])
                
            if i == 0:
                lengthMin = len(x)
                rectc1 = show.show2(ax, x, y, a[i], color[i], mark[i], dot[i])
            elif i == 1:
                rectc2 = show.show2_special(ax, x, y, lengthMin, a[i], color[i], mark[i], dot[i])
            else:
                rectc3 = show.show1(ax, x, y, a[i], color[i])
            i = i + 1
        line = inf.readline()   
    inf.close()
    
#    ax.set_title(title)
    bar_width = 0.35
    l = [int(i) for i in x[0:lengthMin]]
    ax.set_xticks(x[0:lengthMin] + bar_width, l)

    return rectc1, rectc2, rectc3

def dealLine(str):
    strlist = str.split(')  (')
    x = np.array([])
    y = np.array([])
    for s in strlist:
        s = s.strip('()')
        slist = s.split(':')
        a = []
        for c in slist:
            c = c.strip()
            a.append(c)
        x = np.append(x, int(a[0]))
        y = np.append(y,float(a[1]))
    return [x, y]

if __name__ == "__main__":
    fig = plt.figure(figsize=(27, 18))
    ax = fig.add_subplot(111)    # The big subplot

    ax1 = fig.add_subplot(5,3,1) #gas1
    ax2 = fig.add_subplot(5,3,2) #out9
    ax3 = fig.add_subplot(5,3,3) #out8
    ax4 = fig.add_subplot(5,3,4) #out8
    ax5 = fig.add_subplot(5,3,5) #out8
    ax6 = fig.add_subplot(5,3,6) #out8
    ax7 = fig.add_subplot(5,3,7) #out8
    ax8 = fig.add_subplot(5,3,8) #out8
    ax9 = fig.add_subplot(5,3,9) #out8
    ax10 = fig.add_subplot(5,3,10) #out8
    ax11 = fig.add_subplot(5,3,11) #out8
    ax12 = fig.add_subplot(5,3,12) #out8
    ax13 = fig.add_subplot(5,3,13) #out8
    ax14 = fig.add_subplot(5,3,14) #out8
    ax15 = fig.add_subplot(5,3,15) #out8
    
    rectc1, rectc2, rectc3 = readFile(ax7,"2-way gcc.txt")
    readFile(ax8,"3-way gcc.txt")
    readFile(ax9,"4-way gcc.txt")
    readFile(ax4,"2-way HSQLDB.txt")
    readFile(ax5,"3-way HSQLDB.txt")
    readFile(ax6,"4-way HSQLDB.txt")
    readFile(ax10,"2-way JFlex.txt")
    readFile(ax11,"3-way JFlex.txt")
    readFile(ax12,"4-way JFlex.txt")
    readFile(ax13,"2-way tcas.txt")
    readFile(ax14,"3-way tcas.txt")
    readFile(ax15,"4-way tcas.txt")
    readFile(ax1,"2-way tomcat.txt")
    readFile(ax2,"3-way tomcat.txt")
    readFile(ax3,"4-way tomcat.txt")

    #set Y labels
    ax1.set_ylabel(r"$Tomcat$")
    ax4.set_ylabel(r"$Hsqldb$")
    ax7.set_ylabel(r"$Gcc$")
    ax10.set_ylabel(r"$Jflex$")
    ax13.set_ylabel(r"$Tcas$")
    ax1.set_title("2-way")
    ax2.set_title("3-way")
    ax3.set_title("4-way")

        
  

# Turn off axis lines and ticks of the big subplot
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')


# Set common labels
    ax.set_xlabel('covered times', fontsize=20)
    ax.set_ylabel('number of schemas', fontsize=20)
    ax.yaxis.set_label_coords(-0.03, 0.5)

    fig.legend([rectc1, rectc2, rectc3], ['ICT', 'SCT', 'FD'], (0.06, 0.96),
           ncol = 3, prop={'size':10})
    plt.tight_layout()
    plt.show()
