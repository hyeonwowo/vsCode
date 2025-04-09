import math

def find(k):
    n = math.ceil((-1 + math.sqrt(1 + 8 * k)) / 2)
    if n % 2 == 0:
        i = int(n*(n+1) / 2 - k)
        x = n
        y = 1
        return f"{x-i}/{y+i}"   
    else:
        i = int(n*(n+1) / 2 - k)
        x = 1
        y = n
        return f"{x+i}/{y-i}"
    
if __name__ == "__main__":
    k = int(input())
    print(find(k))