import sys

def numcard():
    dictinput = {}
    
    _ = int(input())
    inputlst = list(map(int, sys.stdin.readline().split()))
    _ = int(input())
    outputlst = list(map(int, sys.stdin.readline().split()))
    
    for element in inputlst:
        if element not in dictinput:
            dictinput[element] = 1
        elif element in dictinput:
            dictinput[element] += 1
            
    for i in range(len(outputlst)):
        if outputlst[i] not in dictinput:
            outputlst[i] = 0
        else:
            temp = dictinput[outputlst[i]]
            outputlst[i] = temp
        
    return ' '.join(map(str,outputlst))

if __name__ == "__main__":
    print(numcard())