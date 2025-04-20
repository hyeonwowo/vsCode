import sys
def diffstr(str):
    reslset = []
    for start in range(len(str)):
        for end in range(start,len(str)):
            reslset.append(str[start:end+1])
    return sorted(reslset, key=lambda x:(len(x)))
    
if __name__ == "__main__":
    print(diffstr(sys.stdin.readline().strip()))