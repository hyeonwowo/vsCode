import sys

def modricAlpha(st):
    dictlist = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    for key in dictlist:
        st = st.replace(key," ")
    return len(st.replace(" ","")) + st.count(" ")

if __name__ == "__main__":
    st = sys.stdin.readline().strip()
    print(modricAlpha(st))
