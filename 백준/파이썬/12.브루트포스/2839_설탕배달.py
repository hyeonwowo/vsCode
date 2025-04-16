def sugerDelivery(n):
    min = float('inf')
    for x in range(2000):
        for y in range(2000):
            if 3*x + 5*y == n and min > x + y:
                min = x+y
    return min if min < float('inf') else -1

if __name__ == "__main__":
    print(sugerDelivery(int(input())))