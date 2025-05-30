import sys
import re

def modricAlpha(st):
    pattern = re.compile(r'dz=|c=|c-|d-|lj|nj|s=|z=')  # 긴 패턴 먼저!
    result = pattern.sub(" ", st)  # 모두 한 글자로 대체
    return len(result)

if __name__ == "__main__":
    st = sys.stdin.readline().strip()
    print(modricAlpha(st))
