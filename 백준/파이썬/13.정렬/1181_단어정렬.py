import sys

def sortword(n):
    st = set()
    for _ in range(n):
        st.add(sys.stdin.readline().strip())
    lst = list(st)
    sortlst = sorted(lst, key=lambda x:(len(x),x))
    return '\n'.join(sortlst)

if __name__ == "__main__":
    print(sortword(int(input())))