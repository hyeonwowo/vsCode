def starPrint(N):
    for i in range(N-1):
        print(" "*(N-1-i),end="")
        print("*"*(2*i+1))
    for i in range(N,0,-1):
        print(" "*(N-i),end="")
        print("*"*(2*i-1))
        

if __name__ == "__main__":
    n = int(input())
    starPrint(n)