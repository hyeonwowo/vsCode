class Queue:
    def __init__(self):
        self.list = []

    def enqueue(self, element):
        self.list.append(element)

    def dequeue(self):
        if len(self.list) == 0:
            return None
        else:
            return self.list.pop(0)

    def get(self):
        if len(self.list) == 0:
            return None
        else:
            return self.list[0]

    def printQueue(self):
        # 요소들을 문자열로 변환
        strList = list(map(str, self.list))  # map 객체를 리스트로 변환

        # 각 요소를 "[1]" 형식으로 변환
        resultList = []
        for i in range(len(self.list)):  # range(len(self.list))로 수정
            resultList.append(f"[{strList[i]}]")  # append로 요소 추가

        # 공백으로 구분하여 출력
        print("CurrentQueue:", " ".join(resultList))

if __name__ == "__main__":
    queue = Queue()

    listA = [1, 2, 3, 4, 5]

    for element in listA:
        queue.enqueue(element)

    queue.printQueue()
