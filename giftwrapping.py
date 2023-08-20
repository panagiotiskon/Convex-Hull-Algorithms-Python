import random
import time
import matplotlib.pyplot as plt

class Point:
    def __init__(self,x = None,y = None):
        self.x = x
        self.y = y

    def print(self):
        print(int(self.x),",", int(self.y))
    
    def same(self, p):
        if(self.x == p.x and self.y == p.y):
            return True
        else:
            return False
        
def printl(r):
    if (len(r)>0):
        print("-----------------------")
        for i in range(len(r)):
            r[i].print()
        print("+++++-----------------")
    return 
        
def orientation(p0, p1, p2):

    res = ((p1.x - p0.x)*(p2.y - p0.y))-((p2.x - p0.x)*(p1.y- p0.y))
    if res > 0:     #   CCW
        return 1
    elif res < 0:
        return 2
    elif res == 0:
        return 0

def GiftWrapping(points):
    
    vertexes = []

   
    if len(points)<= 3:
        print("Not enough Points Given\n")
        return points
    
    r0 = min(points, key = lambda k:[k.x, k.y])   # select the leftmost point

    vertexes.append(r0)                 # add r0 to convex hull
    
    while True:

        r = vertexes[-1]     # r is the last vertex to be added 
        u = points[0]       # to make sure the algorithm works always pick the first out of points for u

        for t in points:

            if(u.same(t)==True):
                continue
            if(orientation(r,u,t)==2):
                u = t

        if(u.same(r0)==True):
            break
        else:
            r = u
            points.remove(r)
            vertexes.append(r)

    return vertexes


if __name__ == '__main__':
    
    convex_hull = []
    points = []
    points_number = 10000
    
    while len(points) < points_number:
        new_point = Point(random.randint(-5000, 5000), random.randint(-5000, 5000))
        if new_point not in points:  # Check if the point is not already in the list
            points.append(new_point)
    
    for i in range(len(points)): 
        points[i].print()

    start_time = time.time()

    convex_hull = GiftWrapping(points)
    
    end_time = time.time()
    
    print("-------------")
    print("Convex Hull:")
    print("-------------")
    
    for i in range(len(convex_hull)): 
        convex_hull[i].print()
    print("-------------")
    elapsed_time = end_time - start_time
    print("Elapsed Time:", elapsed_time, "seconds")
    plt.scatter([point.x for point in points], [point.y for point in points], color='blue', marker='o', label='Points')
    plt.scatter([point.x for point in convex_hull], [point.y for point in convex_hull], color='red', marker='o', label='Points')

    for i in range(len(convex_hull)):
        plt.plot([convex_hull[i].x, convex_hull[(i+1) % len(convex_hull)].x], [convex_hull[i].y, convex_hull[(i+1) % len(convex_hull)].y], 'k-')
    plt.show()
 