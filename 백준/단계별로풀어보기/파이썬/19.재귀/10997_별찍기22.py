import sys
sys.setrecursionlimit(10**6)

def star(n):
    if n == 1:
        return ['*']
    elif n == 2:
        return ['*****',
                '*', # "출력형식이 잘못되었습니다"의 원인. '*     ' -> '*' 로 수정했더니 통과....
                '* ***',
                '* * *',
                '* * *',
                '*   *',
                '*****']
    else:
        prev = star(n-1)
        length = len(prev)
        res = []
        
        # up
        res.append('*' * (length+2))
        res.append('*')
        
        # middle
        for i, row in enumerate(prev): # 이전 요소가 필요한 부분에서만 재귀호출 결과값을 사용한다
            if i == 0:
                res.append('* ' + row + '**')
            elif i == 1:
                res.append('* ' + row + ' ' * (length - len(row) - 2) + ' *')
            else:
                res.append('* ' + row + ' *')
        
        # bottom
        res.append('*' + ' ' * length + '*')
        res.append('*' * (length+2))
        
        return res # 모든 출력 행의 res.strip()을 수행 -> 104ms
                   # 그냥 리턴 -> 40ms
        
    
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print('\n'.join(star(n)))