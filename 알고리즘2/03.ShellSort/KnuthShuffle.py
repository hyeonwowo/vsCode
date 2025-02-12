import random

def shuffleSort(a):
    r = [] # 랜덤한 값을 저장할 리스트

    # 리스트 a와 같은 길이의 랜덤 숫자 리스트 r 생성
    for _ in range(len(a)): # _ 는 반복 변수이지만 값을 사용하지 않겠다는 의미 : for i in range(len(a)) 라고 써도 되지만, i 가 코드에서 사용되지 않으므로 _ 로 표시하여 의미적으로 "이 변수를 신경쓰지 않는다"라는 의도 전달
        r.append(random.random()) # 0~1 사이의 랜덤 실수를 생성하여 추가
    

    r = [random.random() for _ in range(len(a))] # 이런 방식으로 r 을 선언해도 됨

    # zip(a,r)을 이용하여 (원소, 랜덤값)쌍을 만들고, 랜덤값을 기준으로 정렬
    return [i for i, _ in sorted(zip(a,r), key=lambda x:x[1])] 

# zip(a,r) : a와 r을 한 쌍으로 묶어서 (a[i],r[i]) 형태의 튜플 리스트를 만듦.
# ex) a = [10,20,30] r = [0.5,0.2,0.8] : [(10,0.5),(20,0.2),(30,0.8)]

# sorted(zip(a,r), key=lambda x:x[1]) : 두번째요소(첫번째요소는 [0])을 기준으로 정렬
# [i for i,_ in sorted(...)] : 정렬된 리스트에서 첫 번째 요소만 추출. _ 는 두 번째요소(랜덤숫자)를 무시하기 위한 용도. 
# ex) [(20,0.2),(10,0.5),(30,0.8)] -> [20,10,30]

def knuthShuffle(a):
    for i in range(1, len(a)):
        j = random.randint(0,i) # Randomly select a position among 0 ~ i
        a[i], a[j] = a[j], a[i] # Swap a[i], a[j]

    return a
    
if __name__ == "__main__":
    print(knuthShuffle([5, 1, 3, 2]))
    print(knuthShuffle(["b", "f", "z", "d", "i", "k", "p", "v"]))
    