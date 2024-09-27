# Damian C. and Jyhno
# 09/29/24
# Implements and tests the dynamic movement update
# and three dynamic movement behaviors, Seek, Flee, and Arrive.
# Will also plot the movement trajectories
#
# Files needed in same workspace:
# progassign_1.py
# char_trajectory.txt
#


# continue character
class Ch1:
    char_num = 1
    char_id = 2601
    #steering behavior code for continue is 1
    steer_behavior = 1
    position = [0, 0]
    velocity = [0, 0]
    orientation = 0
    MAX_velocity = 0
    MAX_acc = 0
    target = 0
    arrive_radius = 0
    slow_radius = 0
    time_target = 0
    collision = False

time = 0
output = open("char_trajectory.txt","w+")


print(time, Ch1.char_id, Ch1.position[0], Ch1.position[1], Ch1.velocity[0],
        Ch1.velocity[1], Ch1.orientation, Ch1.steer_behavior,
        Ch1.collision, sep=',')