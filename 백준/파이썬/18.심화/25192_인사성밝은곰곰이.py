import sys

def hellobear(n):
    count = 0
    userlog = set()
    
    for _ in range(n):    
        log = sys.stdin.readline().strip()        
        if log == "ENTER":
            count += len(userlog)
            userlog.clear()
            
        userlog.add(log)
    return count
        
if __name__ == "__main__":
    print(hellobear(int(input())))