import math
# distance calculates the distance between two points
# IN : two points x and y
# OUT : distance between x and y
def distance(x1, y1, x2, y2):
    distance = math.hypot(x2 - x1, y2 - y1)
    return distance

# duration calculates the duration between t1 and t2
def duration(t1,t2):
    return t2-t1

# calcul_speed calculates the speed of car from given List
# IN : list of distances and time
# OUT : speed
def calcul_speed(points):
    n = len(points)
    total = 0.0
    totalTime = 0.0
    for i in range (n-1):
        x1 = points[i][0]
        y1 = points[i][1]
        t1 = points[i][2]
        x2 = points[i+1][0]
        y2 = points[i+1][1]
        t2 = points[i+1][2]
        dist = distance(x1,y1,x2,y2)
        time = duration(t1,t2)
        total += dist
        totalTime+=time
    speed = total/totalTime
    return speed

