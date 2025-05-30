import sys
def diffstr(str):
    reslset = set()
    for start in range(len(str)):
        for end in range(start,len(str)):
            reslset.add(str[start:end+1])
    return len(reslset)
    
if __name__ == "__main__":
    print(diffstr(sys.stdin.readline().strip()))