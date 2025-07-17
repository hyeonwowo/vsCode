# 📚 기초 흐름
# 백트래킹은 항상 3단계로 작동

# 선택한다.
# 조건을 확인한다.
# 가능성이 있다면: 계속 진행
# 가능성이 없다면: 돌아가기(포기)
# 끝났으면 결과 저장하고 돌아감.

path = []

def backtrack():
    if len(path) == 2:
        print(path)
        return 
    
    for i in [1,2]:
        path.append(i) # 선택한다(진행될수록 깊게 들어감)
        backtrack() # 다음 선택을 하러 간다
        path.pop() # 선택을 취소하고(되돌리고) 다음으로 넘어간다(실패하거나 끝났으면 되돌아가기)
        
backtrack()
print()

path = []
def backtrack():
    if len(path) == 2:
        print(path)
        return 
    
    for element in [1,2,3]:
        if element not in path:
            path.append(element)
            backtrack()
            path.pop()
            
backtrack()
print()

# 📚 재귀 vs 백트래킹의 관계
# ✅ 재귀는 컴퓨터에게 반복적인 구조를 맡기고
# → 우리는 "어떤 단계에서 무엇을 해야 하는지만" 설계하는 것.

# ✅ 백트래킹은 그 재귀를 살짝 더 똑똑하게 써서,
# → "가능성 없으면 빨리 포기하는 조건까지 넣은" 재귀.

# 백트래킹은 재귀를 똑똑하게 쓰는 완전탐색 방법
# ✔️ 재귀처럼 "내가 세부 실행을 하나하나 직접 하지 않고"
# ✔️ "어떤 상황이면 어떻게 하라"만 설계해놓고
# ✔️ 컴퓨터가 알아서 순환하고 되돌리고 진행하는 거예요!


path = []

def backtrack():
    if len(path) == 3:
        print(path)
        return
    for element in [0,1]:
        path.append(element)
        backtrack()
        path.pop()

backtrack()
print()
# [] → [0] → [0,0] → [0,0,0] → 출력
#                        ↳ [0,0,1] → 출력
#         ↳ [0,1] → [0,1,0] → 출력
#                        ↳ [0,1,1] → 출력
# ↳ [1] → [1,0] → [1,0,0] → 출력
#                       ↳ [1,0,1] → 출력
#         ↳ [1,1] → [1,1,0] → 출력
#                       ↳ [1,1,1] → 출력


path = []

def backtrack():
    if len(path) == 3:
        print(''.join(path))
        return 
    for element in ['A','B']:
        path.append(element)
        backtrack()
        path.pop()
        
backtrack()
print()