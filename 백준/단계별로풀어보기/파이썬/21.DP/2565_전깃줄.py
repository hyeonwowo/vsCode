import sys

def electroline(line):
    # 올라가는방향 전깃줄 / 내려가는방향 전깃줄 분리 / 수평전깃줄 분리
    down_line = []
    up_line = []
    pall_line = []
    
    for element in line:
        if element[1] < element[0]:
            down_line.append(element)
        elif element[1] > element[0]:
            up_line.append(element)
        else:
            pall_line.append(element)
            
    down_count = len(down_line)      
    up_count = len(up_line)
    pall_count = len(pall_line)
    
    # 올라가는 방향 전깃줄
    dp_down = [0] * down_count
    dp_down[0] = 1
    for i in range(1,down_count):
        maxdpindex = dp_down.index(max(dp_down))
        if down_line[maxdpindex][1] < down_line[i][1]: # 이전 전선값이 아니라, 전깃줄에 포함된 전선값 사용 - max dp 값을 가진 인덱스의 b좌표
            dp_down[i] = dp_down[maxdpindex] + 1


    # 내려가는 방향 전깃줄
    dp_up = [1] * up_count
    dp_up[0] = 1
    for i in range(1,up_count):
        maxdpindex = dp_up.index(max(dp_up))
        if up_line[maxdpindex][1] > up_line[i][1]:
            dp_up[i] = dp_up[maxdpindex] + 1
    
    # 수평인 전깃줄은 어떻게 처리할것인가 ? -> 일단 내려가는전깃줄, 올라가는전깃줄 안겹치게 수 구하기 -> 수평 전깃줄 추가해보기 -> 더 긴 전깃줄 수 리턴 ? -> 올라가는, 내려가는 접근방식이 아닌듯
    return down_line, up_line, dp_down, dp_up

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    line = []
    
    for i in range(n):
        a,b = map(int, sys.stdin.readline().split())
        line.append((a,b))
    
    print(electroline(sorted(line)))