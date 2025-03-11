# 선분의 표현 Segment

import math

class Segment:
    def __init__(self,x1,y1,x2,y2): # 선분과 점의 표현
        self.p1 = (x1,y1)
        self.p2 = (x2,y2)
    
    def length(self): # 두 점의 길이
        x1,y1 = self.p1
        x2,y2 = self.p2
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
    
    
seg1 = Segment(1,2,4,6)
print(seg1.length())