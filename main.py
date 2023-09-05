from giftwrapping import *
from graham import *
from divide_and_conquer import *
from quickhull import *
import random
import time
import matplotlib.pyplot as plt
import sys


def main(argv):
    convex_hull = []
    points = []

    if len(argv)!=3:
        print("Wrong Arguments!")
        return -1
    
    points_number = int(argv[1])
    algorithm = argv[2]

    while len(points) < points_number:
        new_point = Point(random.randint(-5000, 5000), random.randint(-5000, 5000))
        if new_point not in points:  # Check if the point is not already in the list
            points.append(new_point)


    if algorithm == "Incremental":
        start_time = time.time()
        convex_hull = Graham_s_Scan(points)
        end_time = time.time()

    elif algorithm =="Gift":
        start_time = time.time()
        convex_hull= GiftWrapping(points)
        end_time = time.time()

    elif algorithm =="Divide":
        start_time = time.time()
        convex_hull = Divide_and_Conquer(points)
        end_time = time.time()
    
    elif algorithm =="Quickhull":
        start_time = time.time()
        convex_hull = Quickhull(points, 0)
        end_time = time.time()
    
    elif algorithm =="visual":
        convex_hull = Quickhull(points, 1)
        start_time =1
        end_time = 1
        
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


if __name__ == '__main__':
    main(sys.argv)

