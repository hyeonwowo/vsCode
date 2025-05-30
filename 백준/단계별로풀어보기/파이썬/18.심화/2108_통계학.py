import sys

def finddate(n):
    data_lst = []
    result_lst = []
    for _ in range(n):
        data_lst.append(int(sys.stdin.readline()))
    
    data_dict = {}
    for element in data_lst:
        if element not in data_dict:
            data_dict[element] = 1
        else:
            data_dict[element] += 1
        
    lenlst = len(data_lst)
    data_lst.sort()
    
    avg = round(sum(data_lst) / lenlst)
    mid = data_lst[lenlst // 2]
    
    maxvalue = max(data_dict.values())
    maxcandidate = [k for k,v in data_dict.items() if v == maxvalue]
    maxcandidate.sort()
    
    if len(maxcandidate) == 1:
        most = maxcandidate[0]
    else:
        most = maxcandidate[1]
    
    rang = max(data_lst) - min(data_lst)
    
    result_lst.append(avg)
    result_lst.append(mid)
    result_lst.append(most)
    result_lst.append(rang)
    
    return '\n'.join(map(str, result_lst))

if __name__ == "__main__":
    print(finddate(int(sys.stdin.readline())))
