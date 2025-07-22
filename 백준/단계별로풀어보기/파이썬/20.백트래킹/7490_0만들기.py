import sys

def dfs(index, expression):
    if index == N:
        if eval(expression.replace(' ','')) == 0:
            print(expression)
        return
    else:
        index += 1
        idx = str(index)
        dfs(index, expression + "+" + idx)
        dfs(index, expression + "-" + idx)
        dfs(index, expression + " " + idx)

if __name__ == "__main__":
    t = int(sys.stdin.readline())
    for _ in range(t):
        N = int(sys.stdin.readline())
        dfs(1, "1")
        print()
