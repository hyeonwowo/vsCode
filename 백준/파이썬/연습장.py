arr = [None for i in range(5)]

arr[1:4] = [99] * (4-1)
print(arr)