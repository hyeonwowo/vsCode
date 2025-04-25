# 코드1 : 32ms
import sys
def fasion(n):
    return n * (n-1)
if __name__ == "__main__":
    print(fasion(int(input())))
    
    
# 코드2 : 36ms
import sys
n = int(sys.stdin.readline())
print(n*(n-1))


# 왜 더 복잡해보이는 코드1이 더 빠른가:
# 🔧 주요 차이 분석
# 1. input() vs sys.stdin.readline()
# sys.stdin.readline()이 일반적으로 더 빠릅니다 (여러 줄 입력에서는 확실히).
# 하지만 이 문제는 단일 숫자 1줄 입력이라 input()이 사실 더 가볍게 동작할 수 있습니다.
# input()은 내부적으로 sys.stdin.readline()을 쓰지만, 약간 더 고수준의 처리를 해줍니다.
# 하지만 입력이 작으면 input() 자체가 더 빠른 경우도 존재합니다 (I/O 컨텍스트가 적기 때문에).

# 2. if __name__ == "__main__" 구조
# 이 구조는 파이썬의 실행 흐름을 명확히 제어하게 해줍니다.
# CPython 인터프리터는 __main__ 조건으로 진입할 때, 전역 네임스페이스와 함수 내부 실행을 보다 최적화된 스택으로 관리합니다.
# 즉, 작은 스크립트에서는 main() 안에서 처리하는 쪽이 성능 측면에서 더 유리할 수 있습니다.

# 3. 컴파일러/인터프리터 최적화 영향 (캐시와 파이썬 내부 구조)
# 전역 스코프에 있는 연산은 함수 내부보다 약간 더 많은 컨텍스트 처리 비용이 듭니다.
# 특히 파이썬은 전역 변수, 전역 실행 블록을 함수 내부보다 더 동적으로 추적합니다.
# 함수 내부는 로컬 변수로 처리되고, 더 빠른 참조 방식 (fast locals) 을 사용합니다.

# ✅ 권장
# 성능이 중요한 알고리즘 문제에서는:
# if __name__ == "__main__" 구조 사용하기
# 입력이 많을 땐 sys.stdin.readline() 사용하기
# 단순 입력만 있는 경우엔 input()도 무방


# 리스트 내포 중첩 for문
n = 5
binotree = [[0 for _ in range(1,i+1)] for i in range(1,n+1)] # 주의점 : 리스트 내포 구문에서 중첩 for문 사용시 , for 사이에 다른 코드 사용 불가 ex) [[0 for _ in range(1,i+1)] "i"-사용불가 for i in range(n)]
print(binotree)