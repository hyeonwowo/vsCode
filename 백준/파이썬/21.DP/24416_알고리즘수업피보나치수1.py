def fibonacci_recursive_count(n):
    global code1_count
    if n == 1 or n == 2:
        code1_count += 1
        return 1
    else:
        return fibonacci_recursive_count(n - 1) + fibonacci_recursive_count(n - 2)

def fibonacci_dp_count(n):
    code2_count = 0
    f = [0] * (n + 1)
    f[1] = f[2] = 1
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
        code2_count += 1
    return code2_count

if __name__ == "__main__":
    n = int(input())
    code1_count = 0
    fibonacci_recursive_count(n)
    code2_count = fibonacci_dp_count(n)
    print(code1_count, code2_count)
