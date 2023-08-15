import random
import matplotlib.pyplot as plt


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y


error = Point(-1,-1)

def rotation(p0, p1, p2):

    res = (p1.x - p0.x)*(p2.y - p0.y)-(p2.x - p0.x)*(p1.y- p0.y)
    if(res<0):          #   CW
        return 1
    elif(res>0):
        return 2
    else:
        return 0

def Graham_s_Scan(points):
    
    convex_hull = []

    if len(points)<= 3:
        print("Not enough Points Given\n")
        return points
    


if __name__ == '__main__':
    