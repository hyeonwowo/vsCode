n = int(input())
count = n * (n - 1) // 2
print(count)
print(2)

# 🧠 코드1 수행 횟수 분석
# 바깥 루프: i = 1 to n - 1 → 총 n - 1번 (n-1 - 1 + 1)
# 안쪽 루프: j = i + 1 to n → n - i번 (n - (i + 1) + 1)

# n-1
#  ∑ (n-i) = (n-1) + (n-2) + (n-3) + ''' + 1 = (n-1) * n / 2
# i=1

 