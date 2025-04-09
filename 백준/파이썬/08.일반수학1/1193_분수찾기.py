import math

def find(k):
    n = math.ceil((-1 + math.sqrt(1 + 8 * k)) / 2)
    i = k - ((n*n - n + 2) // 2)
    x = 1
    y = n
    return f"{x+i}/{y-i}"

if __name__ == "__main__":
    k = 4
    print(find(k))