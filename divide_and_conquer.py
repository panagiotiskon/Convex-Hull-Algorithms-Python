from points import *
from scipy.spatial import ConvexHull

def get_index(a, ai, ai1):
    num = len(a)
    a1 = 0
    while True:
        if(a1 != ai and a1 != ai1):
            return a1
        else:
            a1+=1


def Divide_and_Conquer(points):

    p = sorted(points, key = lambda k:[k.x, k.y])

    n = len(points)

    mid =  n // 2

    left = p[:mid]
    right = p[mid:]

    vl = ConvexHull([(point.x, point.y) for point in left])
    vr = ConvexHull([(point.x, point.y) for point in right])
    chl = []
    chr = []


    for i in vl.vertices:    # get left convex hull
        chl.append(left[i])

    print("chl----------")
    for i in range(len(chl)):
        chl[i].print()
    print("chl=============")
    for i in vr.vertices:      # get right convex hull
        chr.append(right[i])

    ai = max(chl, key = lambda k:[k.x])
    bj = min(chr, key = lambda k:[k.x])

    a_index = chl.index(ai) % len(chl)
    b_index = chr.index(bj) % len(chr)

    while True:
        next_index = (a_index - 1) % len(chl)
        third_index = get_index(chl, a_index, next_index) % len(chl)

        while(orientation(chl[a_index], chl[next_index], chl[third_index])==1): 
            a_index = (a_index+1) % len(chl)
        while(orientation(chl[a_index], chl[next_index], chr[b_index])==1):
            b_index = (b_index-1) % len(chr)
        
    return chl
