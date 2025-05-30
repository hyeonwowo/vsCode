def reversearr(arr):
    return ' '.join(char for col in zip(*arr) for char in col)

arr = [
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I']
]

print(reversearr(arr))  # 출력: ADGBEHCFI
