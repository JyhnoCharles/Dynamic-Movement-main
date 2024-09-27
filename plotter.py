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
    def __init__(self,behavior):
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

        for cc in range(0, len(m.x)):
            i = [m.x[c], m.vXp[c]]
            j = [m.z[c], m.laZp[c]] # current z, current z + z linear acceleration
    
