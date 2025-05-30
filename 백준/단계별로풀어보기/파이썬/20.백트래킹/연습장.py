import sys

def pellen(st):
    reversed_st = st[::-1]
    if st == reversed_st:
        return "yes"
    return "no"

def main():
    result = []
    while True:
        st = sys.stdin.readline().strip()
        if st == '0': return '\n'.join(result)
        result.append(pellen(st))

if __name__ == "__main__":
    print(main())