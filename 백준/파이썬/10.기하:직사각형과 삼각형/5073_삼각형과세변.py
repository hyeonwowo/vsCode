import sys

def tri_area(a,b,c):
    if sum([a,b,c]) - max(a,b,c) <= max(a,b,c): return f"Invalid"
    st = len(set([a,b,c]))
    if st == 1: return f"Equilateral"
    elif st == 2: return f"Isosceles"
    elif st == 3: return f"Scalene"

def mn_area():
    lst = []
    while True:
        a,b,c = map(int, sys.stdin.readline().split())
        if a == b == c == 0: return print_lst(lst)
        result = tri_area(a,b,c)
        lst.append(result)
    
def print_lst(lst):
    for element in lst:
        print(element)    
if __name__ == "__main__":
    mn_area()