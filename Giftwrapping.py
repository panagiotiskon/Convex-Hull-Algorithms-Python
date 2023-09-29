from points import *


def GiftWrapping(points):
    
    vertexes = []
    # select the leftmost point
    r0 = min(points, key = lambda k:[k.x, k.y])   
    # add r0 to convex hull
    vertexes.append(r0)                 
    
    while True:
        # r is the last vertex to be added 
        r = vertexes[-1]     
        # to make sure the algorithm works always pick the first out of points for u
        u = points[0]       

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



 