import math

def find(k):
    x = math.ceil((-1 + math.sqrt(1 + 8 * k)) / 2)
    y = 1
    i = k%x
    return f"{x-i-1}/{y+i-1}"

if __name__ == "__main__":
    
    print(find(k))