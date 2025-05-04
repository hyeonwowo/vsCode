import sys # 50점 부분성공 코드

def humancomp(wd,a,b):
    return str(st[a:b+1].count(wd))

if __name__ == "__main__":
    st = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    
    result = []
    for _ in range(n):
        data = list(sys.stdin.readline().split())
        result.append((humancomp(data[0],int(data[1]),int(data[2]))))

    print('\n'.join(result))
