# 큐 (Queue) 활용
# 문제: 큐를 활용하여 최근 5개의 입력값을 저장하는 기능을 구현하세요.
# 마지막 5개 queue 데이터 출력

class RecentValuesQueue:
    def __init__(self):
        self.queue = []

    def add(self, value):
        self.queue.append(value)

    def get_recent(self):
        lista = self.queue[-6:-1] # -5 부터 -1까지
        return lista

if __name__=="__main__":
    queue = RecentValuesQueue()

    queue.add(1)
    queue.add(1)
    queue.add(2)
    queue.add(3)
    queue.add(4)
    queue.add(5)
    queue.add(1)
    queue.add(2)
    queue.add(3)
    queue.add(7)
    queue.add(4)
    queue.add(1)
    queue.add(2)
    queue.add(5)
    queue.add(7)
    queue.add(4)
    queue.add(2)

    print(queue.get_recent())

