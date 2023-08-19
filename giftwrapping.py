import random
import time
import matplotlib.pyplot as plt

class Point:
    def __init__(self,x = None,y = None):
        self.x = x
        self.y = y

    def print(self):
        print(int(self.x),",", int(self.y))

def GiftWrapping(points):
    
    if len(points)<= 3:
        print("Not enough Points Given\n")
        return points
    
    leftmost = min(points, key = lambda k:[k.x])

    
if __name__ == '__main__':
    
    convex_hull = []
    
    points_number = 1000
    points = [Point(random.randint(-5000, 5000),random.randint(-5000, 5000)) for i in range(points_number)]  # create random points

    plt.scatter([point.x for point in points], [point.y for point in points], color='blue', marker='o', label='Points')
    plt.show()

    for i in range(len(points)): 
        points[i].print()

    start_time = time.time()

    convex_hull = Graham_s_Scan(points)
    
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

    for i in range(len(convex_hull)):
        plt.plot([convex_hull[i].x, convex_hull[(i+1) % len(convex_hull)].x], [convex_hull[i].y, convex_hull[(i+1) % len(convex_hull)].y], 'k-')

    plt.show()
