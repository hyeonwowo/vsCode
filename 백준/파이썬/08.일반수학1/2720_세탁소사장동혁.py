import sys

def cost(N):
    lst = []
    for _ in range(N):
        money = int(input())
        lst.append((costMondey(money)))
    return lst

def costMondey(money):
    coinQuarter, money = divmod(money, 25)
    coinDime, money = divmod(money, 10)
    coinNickel, money = divmod(money, 5)
    coinPenny, money = divmod(money, 1)
    return f"{coinQuarter} {coinDime} {coinNickel} {coinPenny}"

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    for line in cost(N):
        print(line)