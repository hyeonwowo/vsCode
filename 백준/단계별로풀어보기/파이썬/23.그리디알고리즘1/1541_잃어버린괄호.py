import sys

def losing(st):
    st_minus = st.split("-")
    temp = []
    for element in st_minus:
        if '+' in element:
            lst = map(int, element.split('+'))
            temp.append(sum(lst))
        else:
            temp.append(int(element))
    result = temp[0]
    for i in range(1, len(temp)):
        result -= temp[i]
    return result

if __name__ == "__main__":
    st = sys.stdin.readline().strip()
    print(losing(st))