from points import *
from scipy.spatial import ConvexHull

# calculate the distance of a point p from the line ab
def distance(a,b,p):
    return abs((p.y-a.y)*(b.x-a.x) - (b.y-a.y)*(p.x-a.x))


def helper(a,b,p,ch):

    right = []

    if(len(p)==0):
        return
    
    # at first get all the points that are on the right of the ab 

    for i in range(len(p)): 
        if(orientation(a,b,p[i])==2):
            right.append(p[i])
    
    if(len(right)==0):
        return 
    
    # get the point with the max distance from ab and add to convex hull

    else:
        dis = -1
        for i in range(len(right)):
            if distance(a,b,right[i]) > dis:
                index = i
                dis = distance(a,b,right[i])

        ai = ch.index(a)
        new_p = right[index]
        ch.insert(ai+1, new_p)

        # continue with the new segments recursively

        helper(a,new_p, right, ch)
        helper(new_p, b, right, ch)    
    
def Quickhull(points):
    
    ch = [] 

    a = min(points, key = lambda k:[k.x, k.y])   # select the leftmost point
    b = max(points, key = lambda k:[k.x, k.y])   # select the rightmost point

    ch.append(a)
    ch.append(b)
    
    # seperate the convehull into two segments the uppermost and the downmost
    # calculate the upper convex hull and then calculate the downer

    helper(a,b,points,ch)
    helper(b,a,points,ch)

    return ch