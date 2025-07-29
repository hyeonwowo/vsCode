import sys
sys.setrecursionlimit(10**6)

def preorder(node):
    res = []
    if node <= n:
        res.append(chr(64 + node))
        res += preorder(node*2)
        res += preorder(node*2+1)
    return res

def inorder(node):
    res = []
    if node <= n:
        res += inorder(node*2)
        res.append(chr(64 + node))
        res += inorder(node*2+1)
    return res

def postorder(node):
    res = []
    if node <= n:
        res += postorder(node*2)
        res += postorder(node*2+1)
        res.append(chr(64 + node))
    return res

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    
    inputInorder = list(map(int, sys.stdin.readline().split()))
    inputPostorder = list(map(int, sys.stdin.readline().split()))
        
    respreorder = preorder(1)
    resinorder = inorder(1)
    respostorder = postorder(1)
    
    resDict = {}
    
    for i in range(n):
        resDict[resinorder[i]] = inputInorder[i]
    
    res = []
    for element in respreorder:
        res.append(resDict[element])
    print(*res)