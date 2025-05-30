def sugarDelivery(n):
    y = n // 5
    for i in range(y, -1, -1):
        rest = n - (5 * i)
        if rest % 3 == 0:
            x = rest // 3
            return x + i
    return -1
    
if __name__ == "__main__":
    print(sugarDelivery(int(input())))