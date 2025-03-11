from queue import PriorityQueue

class Segment:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

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

# 실행
sortPoint(input1)
sortPoint(input2)
sortPoint(input3)
