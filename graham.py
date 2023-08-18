import random
import matplotlib.pyplot as plt

class Point:
    def __init__(self,x = None,y = None):
        self.x = x
        self.y = y

    def print(self):
        print(int(self.x),",", int(self.y))


def orientation(p0, p1, p2):

    res = ((p1.x - p0.x)*(p2.y - p0.y))-((p2.x - p0.x)*(p1.y- p0.y))
    if res > 0:     #   CCW
        return 1
    elif res <= 0:
        return 0

def check_orientation(temp):
    if(len(temp)>=3):
        if (orientation(temp[-3], temp[-2], temp[-1])) > 0:
            temp.pop(-2)
            check_orientation(temp)


def Graham_s_Scan(points):
        
    p = []
    Lupper = []
    Llowwer = []
    convex_hull = []    

    if len(points)<= 3:
        print("Not enough Points Given\n")
        return points
    
    p = sorted(points, key = lambda k: [k.x, k.y])    # sort the list of points 

    # CONSTRUCT Lupper

    Lupper.append(p[0])
    Lupper.append(p[1])

    for i in range(2, len(p)):
        Lupper.append(p[i])
        check_orientation(Lupper)

    for i in range(len(Lupper)):
        convex_hull.append(Lupper[i])

    # CONSTRUCT Llower

    Llowwer.append(p[-1])
    Llowwer.append(p[-2])

    for i in range(len(p)-3, -1, -1):
        Llowwer.append(p[i])
        check_orientation(Llowwer)
    
    Llowwer.pop(0)
    Llowwer.pop(-1)

    for i in range(len(Llowwer)):
        convex_hull.append(Llowwer[i])

    return convex_hull

if __name__ == '__main__':
    
    convex_hull = []
    
    points_number = 1000
    points = [Point(random.randint(-5000, 5000),random.randint(-5000, 5000)) for i in range(points_number)]  # create random points

    plt.scatter([point.x for point in points], [point.y for point in points], color='blue', marker='o', label='Points')
    plt.show()

    for i in range(len(points)): 
        points[i].print()
    
    convex_hull = Graham_s_Scan(points)

    print("Convex Hull:")
    print("-------------")
    for i in range(len(convex_hull)): 
        convex_hull[i].print()
    print("-------------")

    plt.scatter([point.x for point in points], [point.y for point in points], color='blue', marker='o', label='Points')

    for i in range(len(convex_hull)):
        plt.plot([convex_hull[i].x, convex_hull[(i+1) % len(convex_hull)].x], [convex_hull[i].y, convex_hull[(i+1) % len(convex_hull)].y], 'k-')
        
    plt.show()
