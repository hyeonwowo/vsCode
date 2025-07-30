import math

def solve():
    # n: 배열의 크기, k: 필요한 세그먼트의 수
    n, k = map(int, input().split())
    # a: 주어진 정수 배열 (0-indexed)
    a = list(map(int, input().split()))

    # 누적 합 (Prefix Sums) 전처리
    # P[i]는 a[0]부터 a[i-1]까지의 합을 저장합니다. P[0]는 0입니다.
    P = [0] * (n + 1)
    for i in range(n):
        P[i+1] = P[i] + a[i]

    # 특정 구간 [L, R] (0-indexed, inclusive)의 합을 반환하는 헬퍼 함수
    def get_sum(L, R):
        if L > R: # 빈 세그먼트인 경우 (논리적으로 발생하지 않아야 함)
            return 0 
        return P[R+1] - P[L]

    # Sparse Table을 이용한 구간 최대값 질의 (RMQ) 전처리
    # max_log_n은 log2(n)의 올림 값으로, Sparse Table의 열 크기를 결정합니다.
    max_log_n = int(math.log2(n)) + 1
    # st[i][j]는 a[i]부터 a[i + 2^j - 1]까지의 최대값을 저장합니다.
    st = [[0] * max_log_n for _ in range(n)]
    
    # Sparse Table의 기본 케이스: 길이가 1인 세그먼트 (2^0)의 최대값은 자기 자신
    for i in range(n):
        st[i][0] = a[i]

    # Sparse Table 구축
    # j는 2의 거듭제곱 (1, 2, 4, ...)을 나타냅니다.
    for j in range(1, max_log_n):
        # i는 시작 인덱스이며, i + 2^j - 1이 배열 범위를 벗어나지 않도록 합니다.
        for i in range(n - (1 << j) + 1):
            # 현재 구간의 최대값은 두 개의 절반 구간의 최대값 중 더 큰 값입니다.
            st[i][j] = max(st[i][j-1], st[i + (1 << (j-1))][j-1])

    # log_table 전처리: log_table[len]은 floor(log2(len))을 저장하여 RMQ 질의에 사용됩니다.
    log_table = [0] * (n + 1)
    for i in range(2, n + 1):
        log_table[i] = log_table[i // 2] + 1

    # 특정 구간 [L, R] (0-indexed, inclusive)의 최대값을 반환하는 헬퍼 함수
    def get_max(L, R):
        if L > R: # 빈 세그먼트인 경우 (논리적으로 발생하지 않아야 함)
            return 0 
        length = R - L + 1
        k_val = log_table[length] # 구간 길이에 해당하는 2의 거듭제곱 지수
        # 두 개의 겹치지 않는 부분 구간의 최대값 중 더 큰 값을 반환합니다.
        return max(st[L][k_val], st[R - (1 << k_val) + 1][k_val])

    current_pos = 0 # 현재 세그먼트의 시작 인덱스 (0-indexed)
    splits = []     # 1-indexed 분할점들을 저장할 리스트 (b1, b2, ..., bk-1)
    prev_s = 0      # 이전에 완료된 세그먼트의 합
    prev_m = 0      # 이전에 완료된 세그먼트의 최대값

    # k-1개의 분할점을 찾기 위한 루프
    # i는 현재 찾고 있는 분할점의 순서 (0부터 k-2까지)
    for i in range(k - 1):
        s_curr = 0 # 현재 구축 중인 세그먼트의 합
        m_curr = 0 # 현재 구축 중인 세그먼트의 최대값
        last_valid_split_point_for_this_segment = -1 # 현재 세그먼트의 가장 오른쪽 유효한 끝 인덱스

        # min_elements_for_future_segments:
        # 현재 세그먼트 이후에 만들어야 할 남은 세그먼트의 최소 개수입니다.
        # 각 세그먼트는 최소 1개의 요소를 가져야 하므로, 이만큼의 요소가 남아있어야 합니다.
        min_elements_for_future_segments = (k - 1) - i 

        # 'j'는 현재 세그먼트의 잠재적인 끝 인덱스입니다.
        # 현재 세그먼트는 a[current_pos ... j]가 됩니다.
        for j in range(current_pos, n):
            s_curr += a[j]
            m_curr = max(m_curr, a[j])

            # 'j'가 미래 세그먼트를 위한 충분한 요소를 남기는지 확인합니다.
            # n - (j + 1)은 인덱스 'j' 이후에 배열에 남아있는 요소의 수입니다.
            if n - (j + 1) < min_elements_for_future_segments:
                # 남은 요소가 부족하다면, 'j'는 현재 세그먼트의 끝이 될 수 없습니다.
                # 'j'를 더 오른쪽으로 이동해도 이 조건은 계속 실패할 것이므로, 루프를 중단합니다.
                break

            # 조건 확인: |s_prev - s_curr| <= max(m_prev, m_curr)
            # 이 조건은 두 번째 세그먼트부터 적용됩니다 (즉, i > 0일 때).
            condition_satisfied = False
            if i == 0: # 첫 번째 세그먼트 (b1을 찾는 중)
                # 비교할 이전 세그먼트가 없으므로, 조건은 항상 만족하는 것으로 간주합니다.
                condition_satisfied = True
            else:
                # 이후 세그먼트의 경우, 주어진 조건을 적용합니다.
                if abs(prev_s - s_curr) <= max(prev_m, m_curr):
                    condition_satisfied = True
            
            # 현재 'j'가 현재 세그먼트의 유효한 끝 인덱스라면 기록합니다.
            # 우리는 세그먼트를 가능한 한 길게 만들기 위해 가장 오른쪽(가장 큰) 'j'를 찾습니다.
            if condition_satisfied:
                last_valid_split_point_for_this_segment = j
        
        # 현재 세그먼트에 대해 유효한 분할점을 찾지 못했다면, 분할이 불가능합니다.
        if last_valid_split_point_for_this_segment == -1:
            print("No")
            return

        # 1-indexed 분할점을 리스트에 추가합니다.
        # 0-indexed로 세그먼트가 'j'에서 끝났다면, 분할점은 'j + 1'입니다.
        splits.append(last_valid_split_point_for_this_segment + 1)
        
        # 다음 반복(다음 세그먼트)을 위해 prev_s와 prev_m을 업데이트합니다.
        # 방금 완료된 세그먼트의 합과 최대값을 사용합니다.
        prev_s = get_sum(current_pos, last_valid_split_point_for_this_segment)
        prev_m = get_max(current_pos, last_valid_split_point_for_this_segment)
        
        # 다음 세그먼트의 시작 위치를 현재 세그먼트의 끝 다음으로 이동합니다.
        current_pos = last_valid_split_point_for_this_segment + 1
    
    # k-1개의 분할점을 모두 찾은 후, 마지막 세그먼트가 비어있지 않은지 확인합니다.
    # current_pos가 n보다 크거나 같다면, 마지막 세그먼트가 비어있게 됩니다.
    if current_pos >= n:
        print("No") # 마지막 세그먼트가 비어있으므로 허용되지 않습니다.
        return

    # 모든 분할점을 찾았고 마지막 세그먼트도 유효하다면 "Yes"와 분할점들을 출력합니다.
    print("Yes")
    print(*(splits))

# 함수 실행
solve()