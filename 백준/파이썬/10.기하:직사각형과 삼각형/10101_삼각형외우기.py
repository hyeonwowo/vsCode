import sys

def triangle(a,b,c):
    if a == b == c == 60:
        return f"Equilateral"
    if a+b+c != 180:
        return f"Error"
    
    set = {a,b,c}
    if len(set) == 3:
        return f"Scalene"
    elif len(set) == 2:
        return f"Isosceles"

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    print(triangle(a,b,c))
    