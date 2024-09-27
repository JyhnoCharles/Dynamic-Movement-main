# Damian C. and Jyhno C.
# 09/29/24
# Plot the data  of the movement Trajectories 
#
# Files needed in same workspace:
# progassign_1.py
# char_trajectory.txt
#

import matplotlib.pyplot as plt
import csv
import math 
     

    
xLineX = [-100, 100]
xLineY = [0,0]
yLineX = [0,0]
yLineY = [-100, 100]
plt.figure(figsize=(10,10))


plt.plot(xLineX, xLineY, color='grey', linestyle='dashed', linewidth = 1)
plt.plot(yLineX, yLineY, color='grey', linestyle='dashed', linewidth = 1)


class mover:
    def __init__(self, behavior ):
        self.z = [] # position z (meters)
        self.x = [] # position x (meters)
        self.vXp = [] # values to plot velocity x (meters per second)
        self.vZp = [] # values to plot velocity z (meters per second)
        self.laXp = [] # values to plot linear acceleration x (meters per secondper second)
        self.laZp = [] # values to plot linear acceleration z (meters per secondper second)
        self.oXp = [] # values to plot orientation in x
        self.oZp = [] # values to plot orientation in z

movers = {}

with open('data.txt', 'r' ) as csvfile:
    csvreader = csv.reader(csvfile)

    for row in csvreader:

        if(row[1] not in movers):
            movers[row[1]] = mover(int(row[9]))

    m = movers[row[1]]
    
    m.x.append(float(row[2]) ) # Position x
    m.z.append(float(row[3]) ) # Position z
    m.vXp.append( (float(row[4]) * 2 ) + float(row[2]) ) # Velocity data ismultiplied by constants to increase visiblity
    m.vZp.append( (float(row[5]) * 2) + float(row[3]) )
    m.laXp.append( (float(row[6])) + float(row[2]) ) # Linear acceleration
    m.laZp.append( (float(row[7])) + float(row[3]) )
    m.oXp.append( (math.cos(float(row[8]) ) ) + float(row[2]) ) # Orientation
    m.oZp.append( (math.sin(float(row[8]) ) ) + float(row[3]) )

for mov in movers:
    m = movers[mov]

    for c in range(0, len(m.x)):
        i = [m.x[c], m.vXp[c]]
        j = [m.z[c], m.laZp[c]] # curreLnt z, current z + z linear acceleration

        plt.plot(i,j, color='blue',linewidth=0.5)





for mover in movers: 
    m = movers[mov]
    if(m.behavior == 1):
        label = "Continue"
    elif(m.behavior == 6):
        label = "Seek"
    elif(m.behavior == 7):
        label = "Flee"
    elif(m.behavior == 8):
        label = "Arrive"

    plt.annotate(label, color='red', xy=(m.x[0] + 2 , m.z[0] - 2))

    plt.plot(m.x[0], m.z[0], color='red', maker='o', markerfacecolor='red',markersize=3)

    plt.plot(m.x[-1], m.z[-1], color='red', marker='o', markerfacecolor='red', markersize=4)

    plt.plot(m.x, m.z, color='red', linewidth=1)

#Legend
plt.plot(0, 0, color='red', label='position')
plt.plot(0, 0, color='green', label='velocity')
plt.plot(0, 0, color='blue', label='linear')
plt.plot(0, 0, color='yellow', label='orientation')

# format plot and save to file
plt.xlabel('x')
plt.ylabel('z')
plt.title('Dynamic Movement PVL Sample')
plt.legend(bbox_to_anchor=(1.0, 0.8), loc='lower right')
plt.xlim(-100, 100)
plt.ylim(100, -100)

plt.savefig("outputPlot.png",dpi=200)
plt.show()


