N, B = input().split()
B = int(B)

result = 0
power = 0

for digit in reversed(N):
    if '0' <= digit <= '9':
        value = int(digit)
    else:
        value = ord(digit) - 55
    result += value * (B ** power)
    power += 1

print(result)
