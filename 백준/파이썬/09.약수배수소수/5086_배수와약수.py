import sys

def mult_div():
    resultlst = []
    while True:
        x,y = map(int, sys.stdin.readline().split())
        if x == y == 0: break
        if y % x == 0: resultlst.append("factor")
        elif x % y == 0: resultlst.append("multiple")
        else: resultlst.append("neither")
    return resultlst

if __name__ == "__main__":
    for element in mult_div():
        print(element)