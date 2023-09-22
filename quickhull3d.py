from scipy.spatial import ConvexHull
import sys
import time
import random
import matplotlib.pyplot as plt


class Point:
    def __init__(self, x = None, y = None, z = None):
        self.x = x
        self.y = y
        self.z = z
    def print(self):
        print(float(self.x),",", float(self.y), ",",float(self.z))



def main(argv):
    
    convex_hull = []
    
    points_number = int(argv[1])

    points = [Point(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)) for _ in range(points_number)]  

    start_time = time.time()
    convex_hull = ConvexHull([(point.x, point.y, point.z) for point in points])
    end_time = time.time()

    print("-------------")
    print("Convex Hull:")
    print("-------------")
    for i in convex_hull.vertices:
        points[i].print()
    print("-------------")

    elapsed_time = end_time - start_time
    print("Elapsed Time:", elapsed_time, "seconds")

    fig = plt.figure()
    ch = fig.add_subplot(111, projection='3d')

    ch.scatter([point.x for point in points], [point.y for point in points], [point.z for point in points], c='b', marker='o', label='Points')
    ch.scatter([points[i].x for i in convex_hull.vertices], [points[i].y for i in convex_hull.vertices], [points[i].z for i in convex_hull.vertices], c='r', marker='o', label='Hull Vertices')

    for simplex in convex_hull.simplices:
        ch.plot([points[i].x for i in simplex], [points[i].y for i in simplex], [points[i].z for i in simplex], 'k-')

    plt.legend()
    plt.show()

if __name__ == '__main__':
    main(sys.argv)





