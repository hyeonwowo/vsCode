import sys # 신발끈 공식 사용

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    point = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    point.append((point[0][0], point[0][1]))
    
    sum1 = 0
    sum2 = 0
    for i in range(1,N+1):
        sum1 += (point[i-1][0] * point[i][1])
        sum2 += (point[i][0] * point[i-1][1])
    
    res = abs(sum1-sum2) / 2
    print(f"{res:.1f}")