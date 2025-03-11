from queue import PriorityQueue

class Segment:
    def __init__(self, x1, y1, x2, y2):
        assert(x1==x2 or y1==y2) # Accept either a horizontal or vertical segment  
        assert(not (x1==x2 and y1==y2)) # Two end points cannot be equal              

        # Put smaller values in (x1,y1) and larger values in (x2,y2)
        if x1==x2:            
            if y1 < y2: self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
            else: self.x1, self.y1, self.x2, self.y2 = x1, y2, x2, y1
        elif y1==y2:
            if x1 < x2: self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
            else: self.x1, self.y1, self.x2, self.y2 = x2, y1, x1, y2

    def __repr__(self):
        return f"Segment(({self.x1}, {self.y1}), ({self.x2}, {self.y2}))"

def sortPoint(segment_list):
    pq = PriorityQueue()

    # (x1 좌표, 객체) 형태로 삽입
    for segment in segment_list:
        pq.put((segment.x1, segment))

    # 정렬된 결과 출력
    sorted_segments = []
    while not pq.empty():
        _, segment = pq.get()
        sorted_segments.append((segment.x1, segment.y1, segment.x2, segment.y2))

    print(sorted_segments)

# 입력 데이터
input1 = [Segment(0,1,15,1), Segment(1,4,8,4), Segment(3,8,11,8), Segment(9,6,16,6)]

input2 = [Segment(-8,0,8,0), Segment(-7,-1,-7,8), Segment(-6,-2,-6,5), Segment(0,1,0,-10), Segment(5,-3,5,10)]

input3 = [Segment(1,3,6,3), Segment(5,0,5,9), Segment(4,7,9,7), Segment(8,6,8,10),\
    Segment(10,4,13,4), Segment(11,2,17,2), Segment(12,1,12,5), Segment(15,5.5,15,7.5), Segment(14,6.5,16,6.5)]

input4 = [Segment(3,3,8,3), Segment(4,1,4,8), Segment(7,2,7,10), Segment(1,7,12,7)]

input5 = [Segment(0,1,15,1), Segment(14,0,14,2), Segment(1,4,8,4), Segment(6,3,6,7),\
    Segment(2,5,4,5), Segment(3,8,11,8), Segment(9,6,16,6), Segment(13,5.5,13,9.5)]




# 실행
sortPoint(input1)
sortPoint(input2)
sortPoint(input3)
sortPoint(input4)
sortPoint(input5)
