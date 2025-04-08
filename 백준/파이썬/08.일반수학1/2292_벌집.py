def beeHouse(k):
    if k == 1:
        return 1

    i = 0
    current_start = 2
    current_end = 7

    while True:
        if current_start <= k <= current_end:
            return i + 2
        i += 1
        current_start = current_end + 1
        current_end = current_start + 6 * (i + 1) - 1

            
if __name__ == "__main__":
    k = int(input())
    print(beeHouse(k))