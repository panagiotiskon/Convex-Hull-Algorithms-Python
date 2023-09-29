from points import *
from scipy.spatial import ConvexHull

######################################################################################
#                   In this implementation of the algorithmn                         #
#       for a low number of points Scipy's QuickHull algorithm is also used          #
######################################################################################


def get_tanget(chl,chr, ai, bj):
    
    ai2 = ai
    bj2 = bj

    # firstly calculate the upper ai, bj

    flag = 0

    while not flag:
        flag = 1 
        while orientation(chr[bj], chl[ai], chl[(ai+1)%len(chl)])!=1:  # first find ai 
            ai = (ai+1)%len(chl)

        while orientation(chl[ai], chr[bj], chr[(len(chr)+bj-1)%len(chr)])!=2:   # then find bj
            bj = (bj-1)%len(chr)
            flag =0

    # the calculate the lower ai, bj 

    flag2 = 0

    while not flag2:
        flag2 = 1 
        while orientation(chl[ai2], chr[bj2], chr[(bj2+1)%len(chr)])!=1:  # first find ai 
            bj2 = (bj2+1)%len(chr)

        while orientation(chr[bj2], chl[ai2], chl[(len(chl)+ai2-1)%len(chl)])!=2:   # then find bj
            ai2 = (ai2-1)%len(chl)
            flag2 =0
   
    return ai, bj, ai2, bj2

def merge(chl, chr):

    ch = []
    a_index = 0 
    b_index = 0

    # Find the leftmost point in chl and the rightmost point in chr
    ai = max(chl, key=lambda point: point.x)
    bj = min(chr, key=lambda point: point.x)

    # Find ai (leftmost in chl) and bj (rightmost in chr)
    a_index = chl.index(ai)
    b_index = chr.index(bj)
            
    # get final ai and bj both upper and lower

    a_upper, b_upper, a_lower, b_lower = get_tanget(chl, chr, a_index, b_index)  

    # first add ai upper

    ch.append(chl[a_upper])
    
    i = a_upper
    
    # add all the points of chl except ai lower
    
    while i != a_lower:
        i = (i+1) % len(chl)
        ch.append(chl[i])

    # add bj lower

    ch.append(chr[b_lower])
    i = b_lower
    
    # add all the points of chr except bj upper

    while i != b_upper:
        i = (i+1) % len(chr)
        ch.append(chr[i])

    return ch


def Divide_and_Conquer(points):

    # sort the points

    p = sorted(points, key = lambda k:[k.x, k.y])

    n = len(points)
    
    # for a low number of points return ch
    
    if(n<6):
        
        ch = ConvexHull([(point.x, point.y) for point in points])
        hull_points = [points[i] for i in ch.vertices]
        return hull_points
    
    mid =  n // 2
    
    ch = []
    left, right = [], []
    chl, chr = [], []
    
    for i in range(mid):
        left.append(p[i])
        
    for i in range(mid, n):
        right.append(p[i])

    chl = Divide_and_Conquer(left)
    chr = Divide_and_Conquer(right)

    ch = merge(chl, chr)

    return ch
