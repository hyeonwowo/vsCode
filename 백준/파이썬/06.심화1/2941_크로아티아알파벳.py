import sys

def modricAlpha(st):
    stlist = list(st)
    dictlist = ["dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="]  # "dz=" 먼저 처리 필수!
    count = 0

    i = 0
    while i < len(stlist):
        found = False
        for key in dictlist:
            keylen = len(key)
            if ''.join(stlist[i:i+keylen]) == key:
                stlist[i:i+keylen] = [None] * keylen
                count += 1
                i += keylen
                found = True
                break
        if not found:
            i += 1

    chcount = sum(1 for ch in stlist if ch is not None)
    return count + chcount

if __name__ == "__main__":
    st = sys.stdin.readline().strip()
    print(modricAlpha(st))

