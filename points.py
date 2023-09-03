class Point:
    def __init__(self,x = None,y = None):
        self.x = x
        self.y = y

    def print(self):
        print(int(self.x),",", int(self.y))
    
    def same(self, p):
        if(self.x == p.x and self.y == p.y):
            return True
        else:
            return False
        
        
def orientation(p0, p1, p2):

    res = ((p1.x - p0.x)*(p2.y - p0.y))-((p2.x - p0.x)*(p1.y- p0.y))
    if res > 0:     #   CCW
        return 1
    elif res < 0:   #   CW
        return 2
    elif res == 0:
        return 0