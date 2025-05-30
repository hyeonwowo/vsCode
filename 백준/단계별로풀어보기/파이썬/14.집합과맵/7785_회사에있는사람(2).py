import sys

def companyLog(n):
    log = set()
    for _ in range(n):
        name, status = sys.stdin.readline().split()
        if status == "enter":
            set.add(name)
        else:
            set.discard(name)
    return '\n'.join(sorted(log, reverse=True))

if __name__ == "__main__":
    print(companyLog(int(sys.stdin.readline())))
