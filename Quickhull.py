from points import *
import matplotlib.pyplot as plt

# calculate the distance of a point p from the line ab

def distance(a,b,p):
    return abs((p.y-a.y)*(b.x-a.x) - (b.y-a.y)*(p.x-a.x))

def helper(a,b,p,ch,visual,points):

    right = []

    if(len(p)==0):
        return
    
    # at first get all the points that are on the right of the ab 

    for i in range(len(p)): 
        if(orientation(a,b,p[i])==2):
            right.append(p[i])

    # get the point with the max distance from ab and add to convex hull
    if(len(right)==0):
        return 
    
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
        if visual == 1:
            plt.clf()
            plt.scatter([point.x for point in ch], [point.y for point in ch], color='red', marker='o', label='Points')
            plt.scatter([point.x for point in right], [point.y for point in right], color='magenta', marker='o', label='Points')
            plt.scatter([point.x for point in points], [point.y for point in points], color='blue', marker='o', alpha = 0.3, label='Points')
            plt.plot([a.x, b.x], [a.y, b.y],  color='blue', alpha = 0.7, label='line a b')
            plt.scatter(new_p.x, new_p.y, color ='green', marker='o',label='Points')

            for i in range(len(ch)):
                plt.plot([ch[i].x, ch[(i+1) % len(ch)].x], [ch[i].y, ch[(i+1) % len(ch)].y], 'k-')
            
            plt.pause(1)
            plt.draw()

        helper(a,new_p, right, ch, visual, points)
        helper(new_p, b, right, ch, visual, points)    
    
def Quickhull(points, visual):
    if visual == 1:
        plt.ion()
    ch = [] 

    a = min(points, key = lambda k:[k.x, k.y])   # select the leftmost point
    b = max(points, key = lambda k:[k.x, k.y])   # select the rightmost point

    ch.append(a)
    ch.append(b)
    
    # seperate the convehull into two segments the uppermost and the downmost
    # calculate the upper convex hull and then calculate the downer

    helper(a,b,points,ch,visual,points)
    plt.pause(1)
    helper(b,a,points,ch,visual,points)

    if visual == 1 : 
        plt.ioff()
        plt.show()
        
    return ch