import sys

def companyLog(n):
    lst = []
    for _ in range(n):
        log = sys.stdin.readline().split()[0]
        if log in lst:
            lst.remove(log)
        elif log not in lst:
            lst.append(log)
    return '\n'.join(sorted(lst, reverse=True))

if __name__ == "__main__":
    print(companyLog(int(input())))