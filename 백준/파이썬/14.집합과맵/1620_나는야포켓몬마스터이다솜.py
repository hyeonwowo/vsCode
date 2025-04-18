import sys

def pocketmon(n, m):
    num_to_name = {}
    name_to_num = {}

    for i in range(1, n + 1):
        name = sys.stdin.readline().strip()
        num_to_name[i] = name
        name_to_num[name] = i

    result = []
    for _ in range(m):
        query = sys.stdin.readline().strip()
        if query.isdigit():
            result.append(num_to_name[int(query)])
        else:
            result.append(name_to_num[query])

    return '\n'.join(map(str, result))

if __name__ == "__main__":
    print(pocketmon(*map(int, sys.stdin.readline().split())))
