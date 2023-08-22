from points import *


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



 