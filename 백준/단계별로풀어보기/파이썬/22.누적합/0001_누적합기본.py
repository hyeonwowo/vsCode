# arr = [1,2,3,4,5]가 주어졌을 때, 누적합을 각 인덱스별 누적합을 구해라 + start,end가 주어졌을 때, 인덱스 start부터 end까지의 합을 구하여라 (2+3+4)
import sys

def stacksum(arr,idx):
    prefix_sum = [0] * (len(arr) + 1)
    for i in range(1, len(arr) + 1):
        prefix_sum[i] = prefix_sum[i-1] + arr[i-1]
    return prefix_sum[idx]

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    idx = int(sys.stdin.readline())
    print(stacksum(arr,idx))