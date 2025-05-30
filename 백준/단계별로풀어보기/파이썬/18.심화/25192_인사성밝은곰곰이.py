import sys

def hellobear(n):
    myset = set()
    count = 0
    
    for _ in range(n):
        data = sys.stdin.readline().strip()
        if data == "ENTER":
            count += len(myset)
            myset.clear()
        else:
            myset.add(data)
    return len(myset) + count
        
if __name__ == "__main__":
    print(hellobear(int(input())))