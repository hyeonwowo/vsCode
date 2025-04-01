def bucket(N,M):
    arr = [0 for i in range(N)] # 바구니 생성
    
    for _ in range(range(M)): # 반복 횟수
        x, y, z = map(int, input("").split())
    
    return arr
    
if __name__ == "__main__":
    print(bucket(5, 4))