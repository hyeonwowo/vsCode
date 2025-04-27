import sys

def cantoa(n):
    if len(n) == 1: n
    else: 
        length = len(n)
        cantoa(n[:length])
        cantoa(n[(2*length):])
    
if __name__ == "__main__":
    print(cantoa("---"))