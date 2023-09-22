from points import *

def check_orientation(temp):
    while len(temp)>=3 and orientation(temp[-3], temp[-2], temp[-1]) !=1:
        temp.pop(-2)

def Graham_s_Scan(points):
        
    p = []
    Lupper = []
    Llowwer = []
    convex_hull = []    

    if len(points)<= 3:
        print("Not enough Points Given\n")
        return points
    
    # sort the list of points 

    p = sorted(points, key = lambda k: [k.x, k.y])   
    
    # construct Lupper

    Lupper.append(p[0])
    Lupper.append(p[1])

    for i in range(2, len(p)):
        Lupper.append(p[i])
        check_orientation(Lupper)

    for i in range(len(Lupper)):
        convex_hull.append(Lupper[i])

    # construct Llower

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
