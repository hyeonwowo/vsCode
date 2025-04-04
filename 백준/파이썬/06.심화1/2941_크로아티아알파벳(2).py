import sys

def modricAlpha(st):
    dictlist = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    
    for key in dictlist:
        st = st.replace(key, " ")  # 해당 패턴을 공백(또는 한 글자)으로 치환
    
    return len(st.replace(" ", "")) + st.count(" ")  # 실제 글자 수 + 치환된 개수

if __name__ == "__main__":
    st = sys.stdin.readline().strip()
    print(modricAlpha(st))
