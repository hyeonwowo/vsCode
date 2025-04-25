import sys
input = sys.stdin.readline

def main():
    N = int(input())
    structure_types = list(map(int, input().split()))  # A 배열
    initial_values = list(map(int, input().split()))   # B 배열
    
    queue_data = [initial_values[i] for i in range(N) if structure_types[i] == 0]
    queue_data.reverse()  # queuestack의 흐름 보정

    M = int(input())
    input_sequence = list(map(int, input().split()))  # C 배열

    if len(queue_data) >= M:
        print(*queue_data[:M])
    elif len(queue_data) == 0:
        print(*input_sequence[:M])
    else:
        print(*queue_data, end=' ')
        print(*input_sequence[:M - len(queue_data)])

if __name__ == "__main__":
    main()
