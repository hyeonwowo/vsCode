import sys

def sumMember():
    while True:
        memberlst = []
        n = int(input())
        
        if n == -1: break
        for i in range(1, n):
            if n % i == 0: memberlst.append(i)
            
        if sum(memberlst) == n:
            result = " + ".join(map(str, memberlst))
            print(f"{n} = "+result)
        else:
            print(f"{n} is NOT perfect.")
        
if  __name__ == "__main__":
    sumMember()