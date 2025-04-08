def beeHouse(k):
    count = 1
    max_room = 1
    while k > max_room:
        max_room += 6 * count
        count += 1
    return count

# 코드의 핵심은 다음 점화식
# max_room_n = 1 + 6 × (1 + 2 + ... + (n-1))  
#            = 1 + 6 × (n(n-1)/2) 

